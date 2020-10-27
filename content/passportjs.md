---
title: "Аутентифікація з Passport.js"
date: 2016-01-19T13:47:04.325368-05:00
draft: false
author: MaxymVlasov
email: m.vlasov@post.com
---

<div class="image-wrapper">
    <img src="/images/2016/01/1453229201_c538744e3a764b3eaae872adba48666e.png" class="post-image full-img">
</div>

PassportJS є [middleware](https://uk.wikipedia.org/wiki/%D0%9F%D1%96%D0%B4%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BD%D0%B5_%D0%B7%D0%B0%D0%B1%D0%B5%D0%B7%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%BD%D1%8F) між вашою NodeJS-програмою і сайтом. Він виконує усі рутинні операції, що робить ваш код більш лаконічним та дає змогу зосередитись на написанні більш важливих речей. 
<br/><br/>
Має більше 300 стратегій аутентифікації, включно з ВК, ФБ, G+  і навіть  [Tumblr](https://www.youtube.com/watch?v=jEe2fjVqa6I)!<br/>
Їх перелік знаходиться на [passportjs.org](http://passportjs.org/).

Серед фіч passport варто виділити: 
* Єдиний вхід в систему за допомогою OpenID і OAuth
* Легкість відловлювання успіху / невдачі операції
* Підтримка постійних сесій
* Підтримка користувацьких стратегій
* Відсутність потреби прописувати маршрути в додатку
* Простота коду

На сайті PassportJS доступна  детальна [документація](http://passportjs.org/docs).

Якщо кому цікаво, як воно працює, рекомендую прочитати статтю [«Как работает Passport.js»](http://habrahabr.ru/post/201206/).

І да, встановлення:
```
$ npm install passport
```

Tags: JS, nodejs

