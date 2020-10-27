---
title: "Звіт по JavaScript Framework Day"
date: 2016-04-21T16:10:07.896846+00:00
draft: false
author: MaxymVlasov
email: m.vlasov@post.com
---

<div class="image-wrapper">
    <img src="/images/2016/07/1468750997_07355533850d496f88dfcf0fa978cb17.jpg" class="post-image full-img">
</div>

Відвідали на [#js #fwdays](https://twitter.com/search?q=%23fwdays%20since%3A2016-04-16%20until%3A2016-04-18&src=typd).

TL;DR: Нам сподобалось)


## Місце проведення і дорога
Відбувалось все в готелі Ramada Encore, що на півдні Києва. Так як туди нічим особливо не доберешся, тож був організований підвоз від м.Видубичі на бусику, біля якого зустрічав привітний в міру вгодований волонтер у самому розквіті сил.

В Ramada Encore на реєстрації нас зустріли не менш привітні,  чуйні і гарні волонтерши, видали роздатку і бейджики, після чого нас перемкнуло з волонтерш на Wi-Fi.
![](https://pbs.twimg.com/media/CgObtiRUMAAwn4x.jpg:large)


## Лекції
### Life of a pixel: Web rendering performance - Martin Naumann [eng]
Все почалось зі вступної лекції від  Мартіна Наумана про продуктивність веб-рендерингу.

Охочих послухати було так багато, що не всі вмістились в залу.

![](https://pbs.twimg.com/media/CgOqLjZXEAAEA5k.jpg:large)

Use http://csstriggers.com  to figure out what happens when you apply certain CSS rules

WebGL unlike canvas gives you access to programming GPU and parallel pixels processing

[Презентація](http://www.slideshare.net/fwdays/martin-naumann-life-of-a-pixel-web-rendering-performance) | [Twitter](https://twitter.com/g33konaut) | [Github](https://github.com/AVGP) | [FWDays](http://frameworksdays.com/event/js-frameworks-day-2016/review/web-rendering-performance)

Далі був маленький брейк, під час якого InfoPulse розігрував флешки і  power-bank'и, за кидання кілець)
Виграли флешку.


### Spec driven development in Microservices - Микита Галкін

Микита взявся порівнювати RAML, Swageer і API Blueprint. Кожен з них має свої плюси:

* У Swageer велике ком'юніті
* В Blueprint чудові комерційні продукти 
* RAML кристується вельмишановний спікер

Специфікація RAML зберігається у yaml файлах. Більше [в репах Микити](http://github.com/galk-in)

Далі пішла мова про мікросервіси. Вирішили вихдити з того, що мікросервіс можна переписати максимум за місяць силами однієї людини. Інакше - це вже не мікросервіс.

Зважте на те, що версія застосунку, версія сервера і версія протоколу обміну даними - <b>це три різних версії</b>. Якщо перші дві підтримують  третю - то усе інше вже не важливо.


Лайфхак "як змустити кастомера заплатити за фічу, яка спрощує життя девам":

Робіть беклог багів в продакшині, і замість того щоб шукати винного, шукайте що треба зробити, аби ситуація не повторилася.

Коли замовник бачить цифри збитків і опис чим їх мінімізувати - йому можна продати функціонал, за який він спочатку б не платив.


[Бенчмарк і порівняння JSON валідаторів](https://github.com/ebdrup/json-schema-benchmark): jsonschema - один з найповільніших.

[Презентація](http://www.slideshare.net/fwdays/spec-driven-development-in-microservices) | [Github](https://github.com/galk-in) | [Twitter](https://twitter.com/galk_in) | [Facebook](https://www.facebook.com/nikita.galkin) | [FWDays](http://frameworksdays.com/event/js-frameworks-day-2016/review/spec-driven-development-microservices)




### Workshop: Behind the terminal - Євген Обрезков
Після виграшу флешки в @Infopulse_ua йдемо дивитися як рендерити зображення для терміналу в ASCII.
![](https://pbs.twimg.com/media/CgO5l_1UAAAKJs1.jpg:large)

[Eugene Obrezkov](https://twitter.com/ghaiklor) показав [перезенташки в терміналі](https://github.com/ghaiklor/terminal-canvas)

[Презентація](http://www.slideshare.net/fwdays/behind-the-terminal) | [Facebook](https://www.facebook.com/ghaiklor) | [Twitter](https://twitter.com/ghaiklor) | [Github](https://github.com/ghaiklor) | [FWDays](http://frameworksdays.com/event/js-frameworks-day-2016/review/behind-the-terminal)




### Acceptance Testing in NodeJS: Tools & Approaches - Михайло Боднарчук

Доповідь розпочалась з історії Михайла, який оповів про те, як ще його дід з бабою писали софт для допотопних махін. І плавно перейшла у тестування найуспішнішого стартапу України - шоколадну фабрику:)

Запропонуйте вашим QA писати тести на тій же мові що і проект - це дозволить вам один одного краще розуміти і допомагати. Причому невідомо, хто кому більше допомагатиме - ви QA, чи він вам. У будь-якому випадку, почнеться синергія.

Cloud Testing - дозволяють тестувати софт на абсолютно різних платформах. SauseLabs, BrowserStack, TestingBot

Єдине, у cloud testing є проблема з кількістю помилок. Якщо десь там упав браузер - вам прийде лог. А розгрібати таки логи - ой як не цікаво.
А ще ціна кусається.

Не забувайте ізолювати тести. А то деякі QA люблять робити "божественний тест" що вміє у тестування всього І якщо щось десь впало - не зрозуміло в чому проблема.

CodeceptJS - така собі мегаштука, що переводить сценарії в синхроному коді в асинхроний (проміси). Дуже компактний.

[CodeceptJS](http://codecept.io/): 
* Має інтерактивний шел 
* Базується на Mocha
* Схожий на Cucumber
* Працює на ES6
* Має генератор тестів Codecept.io

Тулзи для тестування:
* Selenium webdriver
* PhanthomJS
* Nightmare
* ZombieJS (старе)
* CasperJS (ще старіше)

В реальній практиці варто використовувати тільки Selenium. via [Alexey Raspopov](https://twitter.com/alexeyraspopov/status/721637736919252992)

Кросбраузерні тести - не працюють :/ 

Проте можна тестувати все на хромі,  а для базового функціоналу написати тести для IE і т.д.

Тестування емейли: MailDev, MailCather, MailHog, MailTrap 

Тестуйте мейли через REST API 





### Native JavaScript на мобільних пристроях від Єлени Жукової
В Phonegap усі тяжкі обчислення варто виносити на сервер

<b>Недоліки моб розробки:</b> 
- Складно кастомізувати архітектуру 
- На кожну ОС потрібна свої деви 
- Нема шарингу коду JS обходить їх 

<b>Phonegap:</b>
- Ідея: браузер є всюди 
- Він є на 13 платформах 
- Можна використовувати будь-який фреймворк 
- Можна зробити будь-який UI
- Дуже велике ком'юніті, тому, якщо щось не реалізовано в браузері, швидш за все вже є плагін 
- Незалежить від версії ОС
Використовуємо коли потрібно не тільки іОС і андроїд

<b>Titanium mobile:</b>
- Залежить від версії ОС 
- Весь час змінюють підход до архітектури 
- Мале ком'юніті 
- Починався як Phonegap(в браузері)
Використовуємо якщо потрібен Back end as a Service

<b>React Native:</b>
- Залежить від версії ОС 
- многа букаф :)
Використовуємо якщо ви юзаєте стек реакту

<b>Native Script:</b> 
- Відрізняється від усіх інших 
- Можна юзати npm (як і в реакт) 
- Що 3 місяці нові версії 
- Ком'юніті впливає на фічі
Використовуємо якщо потрібні якісь нативні фічі і не задовбує писати MVVM

Усі тяжкі обчислення варто виносити на сервер.

-як тестувати все це (мобайл)? 
<br>-ручками




### ES6 - Just Do It - Олексій Косинський
Ця лекція була швидше оглядовою, тому варто взяти презентацію, і погуглити кожен невідомий елемент.

Не забудьте звернути увагу на деструктори в ES2015. Сильна фіча.

Ця доповідь трохи  відрізнялась від інших тим, що спікер роздавав футболки за швидке виконання мікрозавдань, таких як "хто перший помітить картинку" або "який буде результат виконання коду"

[Презентація](http://slides.com/alexeykosinski/just-do-it#/) | [Github]() | [Twitter]() |[Facebook]() | [FWDays](http://frameworksdays.com/event/js-frameworks-day-2016/review/es6-just-do-it)





### Боротьба з асинхронністю в JS від Максима Клімішина


В середньому розробник витрачає 50-70% на читання коду і розуміння системи, а не на написання коду. Тому у наших же цілях писати код так, аби його можна було легко зрозуміти.

Для спрощення асинхронної розробки  було придумано багато чого, і далеко не вчора, як це може здатися на перший погляд.

Наприклад, проміси придумали 40 років тому. 40 років тому, КАРЛ!
<br>А async/await всього лиш 19 років тому. До слова, найсвіжіша концепція.

Ще є Actor model (Erlang), CSP (Go, Clojure, ліба js-csp) 

Далі мова піде про кавайність CSP і те, як же його юзати в js.

Отже, js-csp - це ліба, яка реалізує математичну модель CSP в JS. Проміси теж у якійсь мірі мат. модель, проте на рівень нижче. Тому давайте юзати js-csp ^_^

Фічі js-csp:
- буферінг 
- poll values 
- alts 
- І купа екстра-фіч, в тому числі transducers (композиції reduce)

[Презентація](http://www.slideshare.net/fwdays/js-61225351) | [Twitter](https://twitter.com/maxmaxmaxmax) | [FWDays](http://frameworksdays.com/event/js-frameworks-day-2016/review/asynchrony-battle-in-js)




### Боти: можливо, вам не потрібен UI -  Андрій Лісточкін

>Боти всюди. Куди не плюнь всюди розумні боти, які настільки розумні, що нічого не роблять.

Трохи сумної статистики: 80% ботів жодного разу не завантажуються.

Вам не обов’язково робити бота, головне: <b>давайте юзерам максимум корисної інфи, забираючи у них мінімум часу</b>

Вебсайти вантажаться 2сек, а потім 20сек вантажаться кльові шрифти! (Відсилка до назви доповіді)

Stream застарів. Зараз актуальні push-сповіщення

Починайте з процесів компанії. Процеси між людьми і технікою. По суті, відсилка до Internet of Everything (IoE)

Використовуйте Human as an API - HaaA (:

Погугліть: 
- Chris Messina 
- a16z WeChat 
- http://botlist.co  
- Slack App 
- Bot Framework 

[Презентація](http://www.slideshare.net/fwdays/js-61225351) | [Twitter](https://twitter.com/maxmaxmaxmax) | [FWDays](http://frameworksdays.com/event/js-frameworks-day-2016/review/asynchrony-battle-in-js)

![](https://pbs.twimg.com/media/CgQFYZZWQAAwK-B.jpg:large)


### Интерактивные декларативные графики на React+D3
[Презентація](https://rosko.github.io/slides/2016-04-declarative-charts/#/?_k=m11wb2)

[Спікер](https://twitter.com/roskoalexey)


## Фан (развлекаловка)
Футболки за фотку зі стікерами
![](https://pbs.twimg.com/media/CgObxyEWQAAkqZz.jpg:large)

Mortal Combat на 2-му поверсі
![](https://pbs.twimg.com/media/CgOe7LsWwAABfax.jpg:large)

Правильная футболка frontend-разработчика via [Олексій Распопов](https://twitter.com/alexeyraspopov/status/721645604946976769)
![](https://pbs.twimg.com/media/CgPM0xGW4AA-fIi.jpg:large)

До обіду 360 сходинок або черга на ліфт via [Андрій Шумада](https://twitter.com/eagleeye_s/status/721647720759496704)

![](https://pbs.twimg.com/media/CgPppoaWIAEd1yj.jpg:large)

Обід

![](https://pbs.twimg.com/media/CgO8ZAuWsAACrDJ.jpg:large)

![](https://pbs.twimg.com/media/CgPOZbWXIAEvvex.jpg:large)
[Звідси](http://alexeyraspopov.github.io/es-async-future/#)

У Sigma Software був прикольний монстрик. А в самому кінці конфи, на сцену виліз веселий пузатий дядько з цієї ж фірми, і почав роздавати призи)
![](https://pbs.twimg.com/media/CgO896TXIAI1asQ.jpg:large)

дев-конференції - єдине місце, де черги в чоловічий туалет, а не жіночий via [Terry](https://twitter.com/terrysahaidak/status/721675065310502912)

В залі з 400 людей двоє не знає російську. Спікер вирішує виступати англійською. Всім норм. via [Ігор Кевін](https://twitter.com/IhorKevin)

### Other 
Max Klymyshyn  [вот про это вот говорил](https://github.com/papers-we-love/papers-we-love)

Tags: JS, fwdays

