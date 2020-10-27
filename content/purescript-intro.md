---
title: "PureScript — функціональний JavaScript"
date: 2016-01-23T20:12:53.112007-05:00
draft: false
author: MaxymVlasov
email: m.vlasov@post.com
---

<div class="image-wrapper">
    <img src="/images/2016/01/1453592617_2a720c08b9d04c39970037289646d665.jpg" class="post-image full-img">
</div>

Чули про Haskell? А тепер уявіть, що вся його сила прибуває в JS, не привносячи при цьому весь той brainfuck, на якому він побудований.

Уявили? Ну так от, PureScript - це якраз воно. 
* Статично типізований
* Підтримує Haskell-код
* Дружить з JS-кодом
* Компілюється в JS

А також має:
* [Вивід типів](https://uk.wikipedia.org/wiki/%D0%92%D0%B8%D0%B2%D1%96%D0%B4_%D1%82%D0%B8%D0%BF%D1%96%D0%B2)
* [Високо-видовий поліморфізм](https://en.wikipedia.org/wiki/Type_class#Higher-kinded_polymorphism)
* Підтримку основних типів Javascript
* Розширюваність [структур](https://uk.wikipedia.org/wiki/%D0%A1%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0_%28%D1%82%D0%B8%D0%BF_%D0%B4%D0%B0%D0%BD%D0%B8%D1%85%29)
* Розширюваність ефектів
* Оптимізовані правила для генерації ефективного JS-коду
* [Порівняння з прикладом](https://en.wikipedia.org/wiki/Pattern_matching)
* Простий FFI
* Модулі
* [Rank N Types](https://en.wikipedia.org/wiki/Parametric_polymorphism#Rank-n_.28.22higher-rank.22.29_polymorphism)
* [Do нотації](https://en.wikibooks.org/wiki/Haskell/do_notation)
* [Хвостову рекурсію](https://uk.wikipedia.org/wiki/%D0%A5%D0%B2%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B0_%D1%80%D0%B5%D0%BA%D1%83%D1%80%D1%81%D1%96%D1%8F)
* [Type Classes](https://en.wikipedia.org/wiki/Type_class)
* багато ще чого

Якщо більше половини з описаного для вас в новинку - нічого страшного, всі колись з цього починали)

А прокачати скіли вам допоможуть:
* Книжка по PureScript:  [в .pdf](http://vk.cc/4GLYx4) | [онлайн](https://leanpub.com/purescript/read#leanpub-auto-functional-javascript)
* [Сайт PureScript](http://www.purescript.org/learn/)
* [Wiki PureScript](https://github.com/purescript/purescript/wiki)
* [Чат в Гіттері](https://gitter.im/purescript/purescript)
* Сам PureScript
```
$ npm install -g purescript
```
* І [Pulp](https://github.com/bodil/pulp#-pulp) - білдер для PureScript
```
$ npm install -g pulp
```
<br/>

Перевірити підтримку PureScript вашим редактором/IDE можна [тут](https://github.com/purescript/purescript/wiki/Editor-and-tool-support). Там же знаходиться список усіх найбільш корисних тулзів.

І, звісно, глянути онлайн, як PureScript працює, можна на [try.purescript.org](http://try.purescript.org/)

### Замість висновку:
PureScript - жирнюча мова, яка має усі шанси стати достойним конкурентом таким монстрам ФП, як Haskell і F# і точно вже обійти [elm](http://elm-lang.org/).
Як то кажуть, stay tuned, і не забудьте облазити [репу PureScript] - чи не найбільший кладезь знань по PureScript (:


Також, висловлюю подяку [Григорію Шехету](https://vk.com/id_a_gambit), що став натхненником цього посту.

Tags: JS, edu, func_prog, purescript

