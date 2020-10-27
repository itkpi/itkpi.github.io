---
title: "C# Interactive Window для експериментів і тестування API"
date: 2016-01-22T05:48:22.398196-05:00
draft: false
author: itkpi
email: it@kpi.pp.ua
---

<div class="image-wrapper">
    <img src="/images/2016/01/1453457008_147b6e55953a40ed9a50ac0b77c459b2.jpg" class="post-image full-img">
</div>

Знайомтесь, [C# Interactive Window](https://github.com/dotnet/roslyn/wiki/Interactive-Window) - оболонка для швидких експериментів з C#. 

За визначенням це [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) (Read–eval–print loop), яка дозволяє швидко протестувати нове API, обчислити результати виразу або просто запустити невеликий шмат коду. 

Відкрити вікно з консоллю можна в один клік. Йдемо шляхом: 
```View > Other Windows > C# Interactive```

![](/images/2016/01/1453457939_6c9180cfc047443bb7640c3058a3acd8.jpg)

В результаті відкриється вікно з середовищем, де вже можна сповіщати світ про появу нового .NET-програміста.

![](/images/2016/01/1453458094_255246371d164bbab4c932e3a56ed8f6.jpg)

C# Interactive Window підтримує основні фішки звичайної Console App. Окрім дебагу, звісно ж, проте розробники обіцяють додати його найближчим часом. В комплекті є IntelliSense, підсвітка синтаксису і навігація по командам. Більш детальний опис можливостей на [сторінці проекту в GitHub](https://github.com/dotnet/roslyn/wiki/Interactive-Window).

![](/images/2016/01/1453458641_71e5e082394a4b5eb19adcef6b8c64a8.jpg)
![](/images/2016/01/1453458641_b99f7b82075043f5a9e7ea0dc85ca1fc.jpg)

C# Interactive Window незамінне при навчанні. Можна взяти шматок коду з MSDN, вставити у вікно і забути про TestConsoleApp18, якими забита вся папка Projects. Ідеально для експериментів і запуску шматків коду з книги, наприклад.

![](/images/2016/01/1453458884_457c190980014ecb9e076e5e7ecc44fc.jpg)
![](/images/2016/01/1453458884_0f9dbd0828634e5baecdc90166f6f72c.jpg)

А навчатись дійсно весело, адже є підтримка LINQ, директив і усього синтаксичного цукру C# 6.0. От вам приклад string interpolation.

![](/images/2016/01/1453459079_64a4a91ef3f54f11a8dcf7c31b39d7fa.jpg)

Дозволено підключати різні простори імен і вивчати класові бібліотеки .NET

![](/images/2016/01/1453459176_8e2d0cd43bb64a5e9f4ca55969398f62.jpg)

Підтримка виключних ситуацій дуже згодиться під час навчання. 

![](/images/2016/01/1453459344_c589552d530c49c18bffc7added040a9.jpg)

Якщо вже дістало кожного разу створювати новий Console App для того, щоб запустити невеликий шмат коду з MSDN - C# Interactive Window для вас.

Tags: dotNet, csharp

