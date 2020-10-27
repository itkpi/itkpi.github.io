---
title: "\"Записки сумасшедшего\", или \"Знакомимся с ItemTouchHelper в Android\""
date: 2016-01-23T15:24:29.261540-05:00
draft: false
author: Artyom Dorosh
email: artem.dorosh@itkpi.pp.ua
---

<div class="image-wrapper">
    <img src="/images/2016/01/1452285262_40773849f9c54505bbbb1084f8bfdc90.jpg" class="post-image full-img">
</div>

**Дисклеймер**: статья наполнена как технической информацией, так и простой *болью* из жизни Andoid-разработчика. Если вам нужно коротко и по существу, то смело начинайте читать с раздела “**Разбор полётов**”. Если же вы хотите всем сердцем посопереживать и поддержать автора, то прочтите её полностью. 

![](/images/2016/01/1453580527_77710c1310f64d31b90ec2f066ea06a2.png) 

##  Пролог 
Хотя было весьма холодно, зимний день обещал быть не из плохих. Придя на работу, я, как всегда, заварил чай, и вот, усевшись попивать тёплый чаёк с печеньками, я был прерван тимлидом, который собирался показать мне обновленный дизайн проекта. Тут-то мне и стоило *заподозрить неладное*. 

На меня положили задачу переписывания адаптера для главного экрана приложения. И всё было бы хорошо, если бы он не был таким комплексным. Скриншоты самого дизайна я показать вам не могу с ясных причин, но могу вкратце описать проблематику: некоторые данные могут *группироваться* в *группах*(`Xzibit.jpeg`). Но если большее множество разработчиков знает, как это можно реализовать, то следущая задача была на порядок сложнее. 

##  Идея 
Большинство знает о паттерне **swipe-to-dismiss**. Его можно встретить в двух из каждых трёх приложений(*прим.* - не игр), устрановленных на вашем планшете или смартфоне. И так, вы берете итем в адаптере, “тащите” его в правую или левую сторону, и он тащится за вашим пальцем. Исходя из направления, в котором вы потащили итем, вызывается соответствующий обработчик: удаляете, архивируете, отмечаете выполненным, вызываете диалог с действиями, и т.д. 

В моём же задании при свайпе вправо событие отмечается выполненным, но вот действия при свайпе влево куда сложнее. Для них нужно знать величину смещения итема от левого края, причём сам итем не двигается, а надвигается “плашка” поверх итема. 

##  Первые потери и свет в конце туннеля 
Android-разработчики — существа ленивые, впрочем, как и все разработчики. Они не очень-то и любят писать сложное поведение UI вручную, когда можно найти подобную либу на *Android Arsenal*. Только тут есть одна проблема: я работаю c `RecyclerView` почти с самого его анонса, и вам советую на него переходить, если вы ещё каким-то чудом не начали его использовать. 

Для `RecyclerView`, ИМХО, существует всё ещё мало хороших стабильных библиотек, созданных сообществом. Лично моя некогда любимая библиотека, [Advanced RecyclerView](https://github.com/h6ah4i/android-advancedrecyclerview), к чертям поменяла своё API, и мне пришлось потратить пару часов своей жизни просто на миграцию на более новую версию. Таковы причуды открытого сообщества разработчиков, ага. 

Пересмотрев “*обилие*” подходящих решений, я убедился, что придется чуть ли не самому вешать на каждый итем свой `OnTouchListener` с нужными мне обработчиками. Но оставалась последняя надежда. 

Загуглив очередной раз, я наткнулся на некий `ItemTouchHelper`, который умел всё то, что я искал. И самое главное, что сам класс есть в библиотеке `com.android.support:recyclerview-v7`, которую наша любимая *Android Studio* по-умолчанию добавляет в блок зависимостей `build.gradle`, или же вы сами добавляете ее при использовании `RecyclerView`. 

##  Разбор полётов 
Для начала стоит заметить, что сам ItemTouchHelper практически никак не связан c реализацией адаптера. Он скорее связан с вашей реализацией `ViewHolder`-а. 

Для того, чтобы воспользоваться всеми достоинствами хелпера, нам нужно создать собственный `ItemTouchHelper.Callback`. Это интерфейс, позволяющий приложению следить за тем, как пользователь “свайпает” или переставляет итемы между собой. Перемещение я рассматривать не буду, хотя его реализация весьма проста. 

Рассмотрим нужные нам методы “коллбека”: 
``` 
int getMovementFlags(RecyclerView, ViewHolder) 

void onChildDraw(Canvas, RecyclerView, ViewHolder, float, float, int, boolean) 

boolean onMove(RecyclerView, ViewHolder, ViewHolder) 

void onSwiped(ViewHolder, int) 
``` 
Ну и ещё парочку тех, которые нам нужно переопределить: 
``` 
boolean isLongPressDragEnabled() 

boolean isItemViewSwipeEnabled() 
``` 
1 . `getMovementFlags` — позволяет вам задавать флаги движения для каждого итема в `RecyclerView`, который представленный его `ViewHolder`-ом. 

Зададим возможность свайпать только если это обычный итем, а не заголовок в группе. 
```
@Override
public int getMovementFlags(RecyclerView recyclerView, RecyclerView.ViewHolder viewHolder) {
	// Задайте флагам значение 0, если они не должны перемещаться
	int swipeFlags = 0;
	int dragFlags = 0;
	// Если имеем дело с обычным итемом, то задаём флаги движения вправо и влево
	if (viewHolder instanceof TestAdapter.ItemViewHolder)
		int swipeFlags = ItemTouchHelper.START | ItemTouchHelper.END;

	// Используем стандартный метод для создания битмаски флагов движения
	return makeMovementFlags(dragFlags, swipeFlags);
}
```
Наш адаптер же выглядит примерно так: 
```
public class TestAdapter extends RecyclerView.Adapter<RecyclerView.ViewHolder> {

	. . .

	public static class HeaderViewHolder extends RecyclerView.ViewHolder {
		. . .
	}

	public static class ItemViewHolder extends RecyclerView.ViewHolder {
		. . .
	}
}
``` 

Заранее не забудем, что нужно “*включить*” возможность свайпа итемов и “*отключить*” возможность их перемещения между собой: 
```
@Override
public boolean isLongPressDragEnabled() {
    return false;
}

@Override
public boolean isItemViewSwipeEnabled() {
    return true;
}
```

Метод `onMove` нам не понадобится в силу неиспользования возможности перемещать итемы между собой: 
```
@Override
public boolean onMove(RecyclerView recyclerView, RecyclerView.ViewHolder viewHolder, RecyclerView.ViewHolder target) {
	return false;
}
```

2 . `onSwiped()` — метод, который вызывается после того, как итем был конечно перемещён вправо или влево. Тут можно запросто узнать направление свайпа и вызвать нужный нам метод: 
```
@Override
public void onSwiped(RecyclerView.ViewHolder viewHolder, int direction) {
	if (viewHolder instanceof TestAdapter.ItemViewHolder) {
		TestAdapter.ItemViewHolder holder = (TestAdapter.ItemViewHolder) viewHolder;
		// 32 — вправо, а 16 - влево. Определено эксперементальным путём
		if (direction == 32) {
			// вызываете ныжные вам методы
			holder.onSwipedRight();
			. . .
		} else {
			. . .
		}
	}
}
```3 . Ну и на десерт самое вкусное — `onChildDraw()`. Этот метод вызывается тогда, когда вы свайпаете или перемещаете итемы между собой в границах `RecyclerView`. Именно он даёт вам целый полигон для кастомизации: анимации, разные вьюшки, буквально всё, что может придти в голову вашему дизайнеру. 

Не буду демонстрировать что-то сложное на этом примере, лучше просто распишу значения некоторых параметров для большей ясности. 
``` 
```
@Override
public void onChildDraw(Canvas c, RecyclerView recyclerView,  RecyclerView.ViewHolder viewHolder, float dX, float dY, int actionState, boolean isCurrentlyActive) {
	// просто cдвигаем итем в направлении свайпа
	viewHolder.itemView.setTranslationX(dX);
}
```
И так, о параметрах: 
1. `Canvas c` - *канвасы* для отрисовки. 
2. `float dX` - смещение итема относительно оси `X` в пикселах. 
3. `float dY` - смещение итема относительно оси `Y` в пикселах. 
4. `int actionState` - представлеяет какое действие сейчас происходит. Может принимать значения `ACTION_STATE_SWIPE`, `ACTION_STATE_DRAG` и `ACTION_STATE_IDLE`. 
5. `boolean isCurrentlyActive` - `true`, если итем двигает человек, `false`, если итем двигается программно. 

В конце концов, после создания вашего *коллбека*, вам нужно “навесить” сделанный вами обработчик на вашу `RecyclerView`. Делается это очень просто: 
``` 
ItemTouchHelper.Callback callback = new MyItemTouchHelperCallback(); 
ItemTouchHelper touchHelper = new ItemTouchHelper(callback); 
touchHelper.attachToRecyclerView(recyclerView); 
``` 
Ну вот и всё, ваш свайп готов, можно жать на “*Run*” и идти пить чай. 

##  P.S. 
Статью меня попросили написать в нашем ламповом
Android-диалоге в Telegram. Заходите к [нам](https://telegram.me/joinchat/AASSeDxeFHSAkKO4rydImg), там уютно. 

Если же у вас есть вопросы, то вы можете оставлять их здесь в комментариях, в нашем Android-чате в Telegram, или писать [мне](https://vk.com/dorosh_artem) в личку в VK. 

Ну а если вы хотите поделиться своим опытом у нас в блоге, то смело обращайтесь ко мне, или к другим администраторам “ІТ КПІ”. Помните, у вас всегда есть такая возможность!

![](/images/2016/01/1453581556_4704904265344a2a9f66b1a81ea2b30f.png)

Tags: Android, Java, Design

