---
title: "Summary по KyivJS 30.01.16"
date: 2016-01-30T20:01:41.313640+00:00
draft: false
author: MaxymVlasov
email: m.vlasov@post.com
---

<div class="image-wrapper">
    <img src="/images/2016/01/1454185312_7f0a9fcef3ae4daea571a153f54f27f7.jpeg" class="post-image full-img">
</div>

Відвідали [KyivJS](http://kyivjs.org.ua/). Якщо коротко: було весело і цікаво)


А саме, було 4 доповіді: 
* [Євгеній Сафронов: "Scala.JS"](#brscalajs)
* [Павло Пономаренко: "Плагіни для JavaScript ігор"](#brjavascript)
* [Олексій Швайка: "ES6 Classes"](#bres6classes)
* [Денис Зайченко: "Angular best practices"](#brangularbestpractices)

Дві бліц-доповіді:
* [Роман Сенін: "PromisePipe"](#brpromisepipe)
* [Олексій Распопов: "Інженер vs Розробник"](#brvs)

І байки від [@listochkin](https://twitter.com/listochkin)а в перервах :)


<br/>
## Євгеній Сафронов:<br/>Scala.JS


Стара добра [Scala](http://www.scala-lang.org/) тепер доступна і під [JS](http://www.ecma-international.org/publications/standards/Ecma-262.htm)! <br/>
Ще є версія під JVM, а версію під C# дропнули (:

Спікер каже, що Scala — штука проста, порівняно з усілякими Haskell'ями і ClojureScript'ами

>«Ван Гог писав би на Scala, якби був живий»

**Цікавий факт:** понад 300 мов транспілюються у JavaScript.
![Євгеній Сафронов](/images/2016/01/1454187386_efaaac511d7f4e31a64c1b4bb728141b.jpeg)

З хорошого:
* Scala підтримується в IDEшках Intellij і Eclipse
* Вона, цитата: "розширює свідомість"
* Код написаний на [Scala.JS](http://www.scala-js.org/) чудовий

З поганого:
 * Код, транспільований зі Scala.JS в звичайний JS — складний для зневадження
 
![Стандартний приклад Scala.JS](/images/2016/01/1454187699_4bae3320106e42069d1d95e97d222c6c.jpeg)

Де варто використовувати:
* Single-page application
* Великі enterprise-застосунки, де важлива легкість у підтримці коду + довгий термін життя застосунку
* Ігри, де (дуже) багато коду

Ось чому Scala краща  за Javascript:
* [Javascript Fatigue](https://medium.com/@ericclemmons/javascript-fatigue-48d4011b6fc4)
* [wtfjs.com](http://wtfjs.com/)


![WTF JS map ParseInt](/images/2016/01/1454187919_5e540690bef94230832bf4e04714e6e8.jpeg)

Євгеній пропонує спробувати Scala.JS для фронтенду. 

**Питання:** чи є компанії що юзають  Scala.JS на продакшні?<br/>
Ні.


**Безпека**<br/>
ScalaJS безпечна, бо безпечний код зі скали транспілюється у  аналогічний на ES5, тому останній зламати через помилки у JS <span style="text-transform: uppercase">не вдасться</span>.


**Підтримка [ReactJS](https://facebook.github.io/react/)**<br/>
Зараз активно пилять бібліотеку для роботи з react

**Робота з [NodeJS](https://nodejs.org/en/)**<br/>
Я не пробував запускати на ноді, ніхто цього не робить. Проте, згідно документації, це можливо. (але навряд хтось перевіряв)

**Корисні посилання:**
* [Сайт проекту](http://www.scala-js.org/)
* [Github](https://github.com/scala-js/scala-js)
* [Чат у Гіттері](https://gitter.im/scala-js/scala-js)
* Євгеній Сафронов: [Github](https://github.com/javacodegeek) | [Twitter](https://twitter.com/javacodegeek)


<br/>
##  Павло Пономаренко:<br/>Плагіни для JavaScript ігор

>«[Ця людина](https://habrahabr.ru/users/TheShock/) — легенда frontend: єдина людина, яка писала на Хабр статті про JS у часи коли там цього більш ніхто не робив.»<br/>
>— © Лісточкін

**Як писати плагіни?**
* Використання обмеженого API
    * Зміна картинок чи звуків
* Підписка на події
* Агресивне втручання в код
    * Логіка на сервері
    * Критичні частини (логін, донат) виносяться у окремі мікросервіси, недоступні для редагування

Турбота про користувачів, які пишуть плагіни, призвела до поліпшення якості коду в самому проекті.

>«Якщо десь можна було відправити невалідні данні так, щоб це зламало сервер — ці данні будуть відправлені.» — констатував [Паша](https://github.com/theshock).

Зробити систему для написання плагінів — півсправи. А от як їх публікувати? Шляхом спроб і помилок команда Павла дійшла до практики використання [GitLab](https://gitlab.com/).

Імхо, доповідь була найцікавішою, і якби я (*прим.:* Макс) не сидів з напіврозтуленим (в думках) ротом і раніше мав з чимось схожим справу, то записав би явно на порядок більше)

Натомість, раджу переглянути [слайди презентації](http://slides.com/theshock/javascript-plugins), адже у них дуже багато цікавих моментів


<br/>
## Олексій Швайка:<br/>ES6 Classes

Доповідь була англійською.<br/>
Олексій розповідав про різницю між прототипами і класами в JS (спойлер — різниця у назві). Проте, реалізація класів відрізняється від реалізації функцій.

>«Second most popular code reuse technique — inheritance. First one — copy paste.»

**Корисні посилання:**
* [extend-array](https://github.com/shvaikalesh/extend-array/blob/master/extend-array.js)
* Олексій Швайка: [Github](https://github.com/shvaikalesh) |  [Twitter](https://twitter.com/shvaikalesh)





<br/>
## Денис Зайченко:<br/>Angular best practices

Всі замовники в Україні хочуть спеців на AngularJS, а всі розробники хочуть кодити на ReactJS, і таке неподобство триватиме.

Передбачення від Лісточкіна: в Україну може прийти купа замовників на Angular 2. Справа в тому, що багато проектів в США написаних на Angular 1 не стали переходити на React, а вирішили почекати з рішенням на що переходити до виходу Angular 2.

![Денис Зайченко](/images/2016/01/1454201201_cef39b157ad042b182b9bed5163bfb5d.jpeg)

**Корисні посилання:**
* [Angular Style Guide](https://github.com/johnpapa/angular-styleguide) by John Papa
* Денис Зайченко: [Github](https://github.com/MrZaYaC) | [Twitter](https://twitter.com/MrZaYaC)
* Проект: [Angular Material Boilerplate](https://github.com/MrZaYaC/angular-material-boilerplate)


<br/>
## Роман Сенін:<br/>PromisePipe

Рома розказав про крос-процесні гомогенні ланцюги Promise'ів на прикладі бібліотеки [Ельдара Джафарова](https://github.com/edjafarov). Доповідь переросла у дискусію з того, як працює PromisePipe на клієнті та сервері, і механізми взаємодії останніх двох.

![Роман Сенін](/images/2016/01/1454195188_f536e014ca814fe9b66a712d61d97585.jpeg)

**Корисні посилання:**
* [Презентація PromisePipe](http://rastopyr.github.io/promise-pipe-kyivjs/)
* [PromisePipe](https://github.com/edjafarov/PromisePipe)
* Роман Сенін: [Github](https://github.com/Rastopyr) | [Twitter](https://twitter.com/rastopyr_ua)


<br/>
## Олексій Распопов:<br/>Інженер vs Розробник

Стаття [Make Yourself Irrelevant](http://readwrite.com/2013/07/11/make-yourself-irrelevant-how-engineers-can-really-spur-innovation) для справжніх інженерів і тих, хто пише код.

Ознака інженера — доводити проект до кінця.<br/>
Тому автор [Javascript Fatigue](https://medium.com/@ericclemmons/javascript-fatigue-48d4011b6fc4#.txi1othsi) — слабак.

**Корисні посилання:**
* [Презентація](http://alexeyraspopov.github.io/engineer-vs-developer/#)
* Книга [Thinking, Fast and Slow](https://vk.com/doc96849502_437241501) | [російською](https://vk.com/doc96849502_437241520)
* Олексій Распопов: [Github](https://github.com/alexeyraspopov) | [Twitter](https://twitter.com/alexeyraspopov)

<br/>
## Фан і офтоп
Лісточкін розповідав, що в Скандинавії жебраки приймають пожертви  через термінали для кредитних карток :)

<small></small>
>«xxx: Ну, доклад по Angular вряд ли кому-то был бы интересен <br/>
>yyy: Я старовер — мне было интересно :)»

<small></small>
>«John Papa — это спец по Ангуляру<br/>
>Papa John — это пицца»

<small></small>
>«Рассказы о будущем ES7 на #kyivjs напоминают технический вариант сериала "Санта-Барбара" )»
>― © @jsunderhood via @chorna_kiwka

<small></small>
Щодо толку, коли Лісточкін розповідав про Мінськ і те, що там нема чого їсти:
>«KyivJS — спонсор рассказов про драники»

<small></small>
>«90% библиотек в мире фронтенда пишутся потому, что автор не осилил уже существующие решения.»

[Ember в Angular-cli](https://github.com/angular/angular-cli/search?utf8=%E2%9C%93&q=ember)
[![Angular-cli](/images/2016/01/1454196139_03a6c0b688544d7689ece1c00d239755.png)](https://github.com/angular/angular-cli/search?utf8=%E2%9C%93&q=ember)

>«Кстати, так мило, что у Babel проблема с миграцией с 5.x на 6.0. То есть, с 6to5v.5 to 6to5v.6»

Підказка від Лісточкіна куди валити:
>«healthcare, government. Фінанси і так пів-України пилиль, а результату у грошовому еквіваленті не видно.
>
> ...
>
> Валіть до Мінська, там скрізь дранніки і їсти більше нічого. Проте там сидять мільйонери з Viber.»

***Співавтор: [Святослав Сидоренко aka webknjaz](https://twitter.com/webknjaz)***<br/>
*<sub>Добра частина інфи була взята з твіттера за хештеґом [#kyivjs](https://twitter.com/hashtag/KyivJS?src=itkpi).</sub><br/> 
<sup>Дякуємо усім, хто щось із ним постив.</sup>*

Tags: JS, edu, kyivjs

