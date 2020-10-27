---
title: "C# + XAML = Hamburger Menu. Part 1"
date: 2016-02-09T18:15:25.630357+00:00
draft: false
author: Maksym Khamrovskyi
email: maksim36ua@gmail.com
---

<div class="image-wrapper">
    <img src="/images/2016/02/1455040006_9be46c66a8c141c6a677192a0e547db8.gif" class="post-image full-img">
</div>

>Іконка гамбургера — це класика. Навіть якщо ви не знаєте її під цим ім'ям, то три чорні смуги настільки ж знайомі, як курсор миші — постійний супутник нашого інтернет-серфінгу з того дня, як ви отримали комп'ютер. 
>
[Gizmodo](http://gizmodo.com/who-designed-the-iconic-hamburger-icon-1555438787)

Кнопка "Hamburger" зустрічається майже усюди. Від Android-додатків до мобільних версій знаменитих сайтів. Хтось зве її антипатерном UI, хтось боготворить за зручність і зрозумілість. 

Так чи інакше, кнопка з трьома горизонтальними рисками у нашому житті надовго. І сьогодні ми навчимось готувати гамбургер самостійно. 

Ключові інгредієнти страви:

- [Visual Studio 2015 Community](https://www.visualstudio.com/en-us/downloads/download-visual-studio-vs.aspx)
- Багато терпіння, щоб подужати статтю
- [Книга по розробці під Windows 10 від Маргарити Остапчук і Сергія Байдачного](https://vk.com/wall-88116812_364)
- Трохи розуміння C# (опціонально)
- Трохи розуміння XAML (опціонально)

Дві ремарки перед тим, як почнемо:
 - в деяких місцях форматування коду поїхало, бо не влізає по ширині. При копіюванні у Visual Studio все красиво, тому feel free to use Ctrl+C and Ctrl+V
 - текст, що виділений як цитата, надає додаткову інформацію. Його можна не читати. 

Отже, поїхали. 

Велика подорож починається з першого кроку, а написання крутого додатку  — зі створення проекту. 
Обираємо  Blank App і тиснемо «Ok».

![](/images/2016/02/1455039768_79c6308620ea497abebe6cb5df1ec387.jpg)

Оберіть дві картинки на свій смак і перетягніть їх в папку Assets. Згодом ми будемо міняти їх місцями, перемикаючи пункти нашого «Hamburger» меню.

![](/images/2016/02/1455039807_7bd702b00f084470b3b1952703658d29.jpg)

Картинки помістимо на окремі XAML-сторінки і будемо переключати їх всередині фрейму. Про це в деталях трохи згодом, зараз просто додаємо дві порожні сторінки в проект.  Натискаємо правою кнопкою миші на назві проекту, `Add  => New Item`. Обираємо Blank Page, задаємо ім’я і клацаємо «Ок»

![](/images/2016/02/1455040109_8627e6d3c2b144268f4c943d2704b1b2.jpg)

![](/images/2016/02/1455040109_63d9b232ef5b43f3b6ec228efe868e8a.jpg)

В HTML сторінка складається з двох частин. Тег <head> містить атрибути, які допомагають браузеру коректно відображати вміст. В той же час <body> зберігає сам контент, який необхідно показати. 

Якщо провести аналогію, то XAML-сторінку можна умовно розбити на частину з оголошенням просторів імен і, власне, контентом. Вгорі сторінки міститься стовпець xmlns–тегів, що вказують на різні схеми. Якщо спростит — в цих схемах міститься інформація про елементи керування (controls), їх властивості, правила створення об’єктів з XAML-коду і все-все-все. Ці штуки краще не займати, а якщо дуже хочеться хоч трохи зрозуміти їх призначення — можна почитати [тут](https://msdn.microsoft.com/ru-ru/library/ff633576(v=vs.110).aspx) або [в книзі](https://vk.com/wall-88116812_364) Маргарити Остапчук і Сергія Байдачного про розробку під Windows 10 тут (сторінка 27).

Нижче під просторами імен побачите елемент керування `<Grid>`. Він розбиває видимий простір на сітку з рядків і стовпців. Додаємо зображення до `<Grid>` на сторінках IT\_KPI.xaml та MS\_KPI.xaml. 

Для цього використовується тег `<Image>`. Атрибут Source вказує шлях до картинки, а VerticalAlignment прив'язує зображення до верху сторінки.

Додаємо наступний код всередину тега `<Grid>`:

    <Image Source="Assets/НАЗВА_ЗОБРАЖЕННЯ.jpg" VerticalAlignment="Top" />

В результаті маємо:

    <Grid Background="{ThemeResource ApplicationPageBackgroundThemeBrush}">
      <Image Source="Assets/1.jpg" VerticalAlignment="Top" />
    </Grid>

Ще один важливий момент: за замовчуванням у нашому додатку буде висвічуватись лічильник FPS.

![](/images/2016/02/1455041094_6f048a648e06497a8633b7516766b556.png)

Часто дуже корисна штука, але не вписується в наш космічний дизайн. Щоб позбутись від нього мусимо перейти в App.xaml.cs і видалити наступний шматок коду.

![](/images/2016/02/1455041128_dd63abcbf6c74048ba4c7a4e0fb44275.jpg)

Підготовчий етап завершено, приступаємо до найцікавішого. Йдемо в MainPage.xaml і розбиваємо сторінку на дві стрічки. Як вже згадували, для цього служить `<Grid>`. Кількість рядків і стовпців задається властивостями (property) під назвою `<Grid.RowDefinitions>` та `<Grid.ColumnDefinitions>`. Ми хочемо розбити сторінку на два горизонтальні рядки, тому додаємо відповідні теги. 

Маємо наступний код:

    <Grid Background="{ThemeResource ApplicationPageBackgroundThemeBrush}">
        <Grid.RowDefinitions>
            <RowDefinition Height="Auto"/>
            <RowDefinition Height="*"/>
        </Grid.RowDefinitions>
    </Grid>

>`Height="Auto"` говорить про те, що висота елементу буде визначатись висотою його вмісту. Якщо всередину першого рядка помістити кнопку з властивістю `Height="50"`, то висота рядка також буде 50 пікселів.

>`Height="*"` говорить рядку: «Займи весь вільний простір, який знайдеш». Певно, схожа команда є всередині браузера Google Chrome і стосується оперативної пам'яті.

Нижче додамо `<RelativePanel>`, яка зберігатиме кнопку гамбургера, кнопку «Назад» і панель пошуку.

>`<RelativePanel>` — це контейнер для взаємного позиціонування елементів керування один відносно одного. Застосовуючи прикріплені властивості (attached properties) можна розташувати один елемент відносно іншого, або приліпити елемент до самої панелі. Детальніше [тут](https://msdn.microsoft.com/library/windows/apps/windows.ui.xaml.controls.relativepanel.aspx#attachedmembers).

Ще нижче додамо `<SplitView>`, в якому буде знаходитись саме тіло меню. Нащо він треба і як працює буде описано, коли до нього дійде черга. Зараз просто допишемо його під `<RelativePanel>` і заб’ємо.

На даному етапі код виглядає так: 

    <Grid Background="{ThemeResource ApplicationPageBackgroundThemeBrush}">
        <Grid.RowDefinitions>
            <RowDefinition Height="Auto" />
            <RowDefinition Height="*" />
        </Grid.RowDefinitions>

        <RelativePanel>
        </RelativePanel>

        <SplitView>
        </SplitView>
    </Grid>

Всередину `<RelativePanel>` додаємо головну кнопку з трьома горизонтальними рисками, на честь якої і назвали дизайн меню. Також покладемо туди кнопку «Назад», текстовий блок з назвою сторінки і панель пошуку, роль якої буде виконувати поле та кнопка.

Код `<RelativePanel>`.  Також необхідно дати імена усім нашим елементам. 

    <RelativePanel>
       <Button Name="HamburgerButton" />     
       <Button Name="BackButton"/>          
       <TextBlock Name="TitleTextBlock"/>    
       <TextBox Name="SearchTextBox"/>       
       <Button Name="SearchButton" />             
    </RelativePanel>

Як було сказано, `<RelativePanel>` служить для відносного позиціонування своїх дочірніх елементів. «Гамбургер» знаходиться зліва. Кнопка «Назад» буде знаходитись праворуч від «Гамбургера». Назва сторінки — праворуч від «Назад», меню пошуку потрібно розмістити справа відносно панелі. Для цього задаємо відповідні властивості.

Тепер код має наступний вигляд:

    <RelativePanel>
            <Button Name="HamburgerButton" 
                    RelativePanel.AlignLeftWithPanel="True"/>    
         
            <Button Name="BackButton"
                    RelativePanel.RightOf="HamburgerButton"/>  
          
            <TextBlock Name="TitleTextBlock"
                       RelativePanel.RightOf="BackButton"/>      

            <TextBox Name="SearchTextBox" 
                     RelativePanel.LeftOf="SearchButton"/>

            <Button Name="SearchButton" 
                    RelativePanel.AlignRightWithPanel="True"/>
    </RelativePanel>

Властивості можна переміщати на наступну стрічку для покращення читабельності. Синтаксис це дозволяє.

Тепер головне — призначаємо знамениту іконку «Hamburger». Для відображення трьох горизонтальних рисок на кнопці використовується спеціальний шрифт, що зветься `«Segoe MDL2 Assets»`. Символи цього шрифту можна знайти у всіх сучасних програмах Microsoft і не тільки.

Щоб глянути всі доступні символи та їх коди достатньо запустити програму «Таблиця символів» (Character map). Вона стандартна, застосуйте пошук по комп'ютеру. 

![](/images/2016/02/1455043471_2d910e164854485c8fc7911e2bdaeb9b.jpg)

Нас же цікавить код кнопки «Меню», «Назад» та «Пошук»

![](/images/2016/02/1455043501_78dabe0ffdd24b0584d9a326f2a61016.jpg)

Для присвоєння символу кнопці пишемо наступні властивості:

    FontFamily="Segoe MDL2 Assets"
    Content="&#xCODE;"

Де `CODE` – код кнопки. Для менюхи, «назад» і «пошук» коди `E700`, `E0C4` та `E1A3` відповідно.

Розмір шрифту задається властивістю FontSize. Ставимо його рівним 36.

    FontSize="36"

Також для кожної кнопки додаємо обробник події, що реагує на натискання. Коли користувач тикне на кнопку ми хочемо, щоб відбувались певні дії. Ці дії і будуть визначатись обробником Click.
 
Вставляємо в кнопки «Меню» і «Назад» властивість

    Click="НАЗВА_КНОПКИ_Click"

Для кнопки пошуку обробник не потрібен, в нас же нічого шукати.
 
Вміст `<RelavivePanel>` виглядає так:

     <RelativePanel>
            <Button Name="HamburgerButton" 
                    RelativePanel.AlignLeftWithPanel="True"
                    FontFamily="Segoe MDL2 Assets"
                    FontSize="36"
                    Content="&#xE700;"
                    Click="HamburgerButton_Click"/> 
            
            <Button Name="BackButton"
                    RelativePanel.RightOf="HamburgerButton"
                    FontFamily="Segoe MDL2 Assets"
                    FontSize="36"
                    Content="&#xE0C4;"
                    Click="BackButton_Click"/>
            
            <TextBlock Name="TitleTextBlock"
                       RelativePanel.RightOf="BackButton"
                       FontSize="28"/>``            
                 
            <TextBox Name="SearchTextBox" 
                     RelativePanel.LeftOf="SearchButton"
                     Height="48" 
                     Width="200"
                     FontSize="24"
                     PlaceholderText="Search"/>

            <Button Name="SearchButton" 
                    RelativePanel.AlignRightWithPanel="True"
                    FontFamily="Segoe MDL2 Assets"
                    FontSize="36"
                    Content="&#xE1A3;"/>
     </RelativePanel>

Настав час підпалити проект. Тикаємо F5 і маємо наступний результат:

![](/images/2016/02/1455047535_061f37c72f984605ad4bb13e5b8cabca.jpg)

[Продовження епопеї читайте тут](http://itkpi.pp.ua/hamburger-menu-2)

Tags: dotNet, csharp

