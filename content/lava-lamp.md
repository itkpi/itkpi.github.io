---
title: "Історія однієї команди (англійською)"
date: 2016-01-06T07:58:52.866824-05:00
draft: false
author: Roman Rader
email: roman.rader@gmail.com
---

<div class="image-wrapper">
    <img src="/images/2016/01/1452085233_0df8c978a3c4420287e29bb75a12ea9c.jpg" class="post-image full-img">
</div>

Як зацікавити програмістів швидко виправляти баги? Підключіть лава-лампу до системи неперервної інтеграції!

Код, що не працює, не має довго знаходитись у репозиторії. Його треба виправляти якнайшвидше, щоб інші члени команди працювали із стабільним кодом. Це всі знають, але програмісти - ліниві істоти та часто не дивляться на результати тестів.

До вашої уваги історія боротьби за стабільність коду однієї команди у 2006-2007 роках.

> Around 2006-2007, it was a bit of a fashion to hook lava lamps up to the build server. 
Normally, the green lava lamp would be on, but if the build failed, it would turn off and the red lava lamp would turn on. 

>By coincidence, I've actually met, about that time, (probably) the first person to hook up a lava lamp to a build server. 
It was Alberto Savoia, who'd founded a testing tools company 
(that did some very interesting things around generative testing that have basically never been noticed). 
Alberto had noticed that people did not react with any urgency when the build broke. 
They'd check in broken code and go off to something else, 
only reacting to the breakage they'd caused when some other programmer pulled the change and had problems.

>So Alberto hooked up the build server to the lava lamps, which he put in the middle of the large U-shaped table configuration 
that the people worked at. (About the same number of programmers we have, maybe a little more.) 
This solved the problem, but Alberto noticed something additional and interesting.

>It turns out that lava lamps take about 15-20 minutes to get warm enough for the wax bubbles to start floating upward. 
What was interesting was that it became a competition among programmers: 
as soon as the red lava lamp turned on, the person who'd broken the build *really* *really* wanted to fix it 
before the bubbles started rising.

>This was another of my Aha! moments: 
Everyone knew broken builds should be fixed quickly. 
No one did it. Introduction of a *completely irrelevant* stimulus/challenge caused people to behave correctly. 
Reason could not counteract unreasonable natural inclination, but a *different* unreasonable natural inclination could.

>Huh.

[*Джерело*](https://gist.github.com/marick/3ec112bc38b2af267e15)

Tags: fun

