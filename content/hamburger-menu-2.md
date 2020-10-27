---
title: "C# + XAML = Hamburger Menu. Part 2"
date: 2016-02-09T19:58:55.981636+00:00
draft: false
author: Maksym Khamrovskyi
email: maksim36ua@gmail.com
---

<div class="image-wrapper">
    <img src="/images/2016/02/1455101294_03ba9e36e09d4ea5af55010fbbc06d2c.jpg" class="post-image full-img">
</div>

[Перша частина тут](http://itkpi.pp.ua/hamburger-menu-1/). Якщо ви це читаєте, значить приступаємо до наповнення сторінки контентом.
 
Нижче від `<RelativePanel>` у нас знаходиться `<SplitView>`. 

>`<SplitView>` грає роль контейнера з двома вікнами. В`<SplitView.Pane>` поміщається навігаційне меню, яке зазвичай приховане або не повністю відображається. Її вміст може ставати видимим або ховатись в залежності від властивостей, які задамо. `<SplitView.Content>` містить весь контент сторінки (вибачте за каламбур).

Ми розбили сторінку на дві стрічки. У верхній – кнопки «Меню», «Назад» і панель пошуку. В нижній будуть розташовані пункти меню. Якщо не вказано стрічку, в якій буде знаходитись елемент – він розміщується в першій за замовчуванням. Нумерація починається з «0», варто мати це на увазі. `<RelativePanel>` автоматично помістилась у першу за порядком і нульову за номером стрічку.

Наш SplitView поміщаємо в другу стрічку, тому задаємо прикріплену властивість (attached property) `Grid.Row="1"`

Код такий: 

    <SplitView Grid.Row="1">

            <SplitView.Pane>                
            </SplitView.Pane>

            <SplitView.Content>                
            </SplitView.Content>

    </SplitView>

Щоб зразу наповнити сторінку контентом — додаємо `<Frame>`, у який вставимо наші IT\_KPI.xaml та MS\_KPI.xaml Також задаємо ім’я. 

>`<Frame>` відображає екземпляри сторінок, підтримує навігацію на нові сторінки і містить навігаційну історію щоб надати можливість переміщатись туди-сюди по сторінкам. По суті, призначення цього елементу таке ж, як і в HTML: відображати всередині себе шматок іншої сторінки.  

Код:

    <SplitView Grid.Row="1">

            <SplitView.Pane>                
            </SplitView.Pane>

            <SplitView.Content>
                <Frame Name="MyFrame">
                </Frame>
            </SplitView.Content>

    </SplitView>

Для пунктів меню скористаємось елементом керування <ListBox>. 

>` <ListBox>` зазвичай слугує для відображення списків. Елемент являє собою блок, всередині якого розміщуються стрічки з пунктами, з-поміж яких користувач може обирати один або декілька. 

Елементи `<ListBox>` задаються тегом `<ListBoxItem>`, які будуть слугувати пунктами меню.

В кожному пункті нам потрібно два елементи: іконка (зліва) та назва пункту (справа). Для того, щоб помістити послідовно два елементи скористаємось елементом `<StackPanel>` і вкажемо її орієнтацію як горизонтальну. 

>`<StackPanel>` багато в чому схожа на ` <ListBox>`, але має більше властивостей і ширше застосування. Призначена для того, щоб розташовувати різні елементи один над іншим, а не лише стрічки. Орієнтацію можна змінити на горизонтальну.

    <SplitView Grid.Row="1">

            <SplitView.Pane> 
                <ListBox> <!-- Меню -->

                    <ListBoxItem> <!-- Пункт меню -->
                        <StackPanel Orientation="Horizontal">
                        </StackPanel>
                    </ListBoxItem>

                    <ListBoxItem>
                        <StackPanel Orientation="Horizontal">
                      </StackPanel>
                    </ListBoxItem>

                </ListBox>
            </SplitView.Pane>

            <SplitView.Content>
                <Frame Name="MyFrame">
                </Frame>
            </SplitView.Content>

     </SplitView>

В кожен тег `<StackPanel>` вставляємо два текстові блоки і вписуємо в них іконки. Також дамо назви кожному `<ListBoxItem>`, щоб можна було достукатись до них з обробника подій. Задамо два атрибути для `<ListBox>`:

    SelectionMode="Single" SelectionChanged="ListBox_SelectionChanged"

>`SelectionMode="Single"` говорить про те, що в кожен момент часу лише один елемент меню може бути обраний.
 
>`SelectionChanged="ListBox_SelectionChanged"` – це обробник події, що реагує на переключання пункту меню

Не забудемо про `<SplitView>` і додамо йому кілька атрибутів. Ім’я, режим відображення та розміри панелі у відкритому і закритому станах.

    DisplayMode="CompactOverlay" CompactPaneLength="56"            
    OpenPaneLength="200"

Зараз код виглядає так:

    <SplitView Grid.Row="1"
           Name="MySplitView"
           DisplayMode="CompactOverlay"
           CompactPaneLength="56"
           OpenPaneLength="200">

            <SplitView.Pane>
            <ListBox SelectionMode="Single"
                SelectionChanged="ListBox_SelectionChanged">

                <ListBoxItem Name="IT_KPI">
                    <StackPanel Orientation="Horizontal">
                        <TextBlock FontFamily="Segoe MDL2 Assets"
                            FontSize="36"
                            Text="&#xE80F;"/>
                        <TextBlock FontSize="24">IT KPI</TextBlock>
                    </StackPanel>
                </ListBoxItem>

                <ListBoxItem  Name="MS_KPI">
                    <StackPanel Orientation="Horizontal">
                        <TextBlock FontFamily="Segoe MDL2 Assets"
                            FontSize="36"
                            Text="&#xE1CE;"/>
                        <TextBlock FontSize="24">MS KPI</TextBlock>
                    </StackPanel>
                </ListBoxItem>

            </ListBox>
            </SplitView.Pane>

            <SplitView.Content>
                <Frame Name="MyFrame">
                </Frame>
            </SplitView.Content>

    </SplitView>

Перш ніж запустити проект – мусимо додати останній штрих. 
Гортаємо код вгору до нашої кнопки «Гамбургер», ставимо курсор на назву обробника події у властивості Click і тиснемо F12.

![](/images/2016/02/1455047587_3e326a78c4674446aeecea7616087985.jpg)

Відкриється файл MainPage.xaml.cs, який містить обробники подій з нашої головної XAML-сторінки. В методі HamburgerButton_Click прописуємо одну єдину стрічку, що інвертує стан панелі `<SplitView.Pane>`.

    MySplitView.IsPaneOpen = !MySplitView.IsPaneOpen;

Тепер можна запускати проект і дивитись, що вийшло.

![](/images/2016/02/1455047633_0b1a63ee13c74143b28a574341c02814.jpg)

Текст трохи виглядає з меню. На щастя, це легко пофіксити, вказавши атрибут `Margin="20,0,0,0"` для другого `<TextBlock>`. Це змусить його посунутись на 20 пікселів праворуч. 

    <TextBlock FontSize="24" Margin="20,0,0,0">IT KPI</TextBlock>
    …
    <TextBlock FontSize="24" Margin="20,0,0,0">MS KPI</TextBlock>

Тепер маємо робочий приклад меню, який реагує на натискання кнопки «Hamburger». Час йти далі і написати трохи логіки.

Коли додаток стартує ми хочемо, щоб завантажувалась одна з XAML-сторінок і назва сторінки вгорі змінювалась. Для цього в конструкторі MainPage() прописуємо наступне:

    MyFrame.Navigate(typeof(НАЗВА_СТОРІНКИ)); 
    TitleTextBlock.Text = "НАЗВА_СТОРІНКИ";

При першому запуску з'являється головна сторінка, тому не треба, щоб кнопка «Назад» відображалась. 

Приховуємо її стрічкою:

    BackButton.Visibility = Visibility.Collapsed; 

Оголошуємо про те, що сторінка IT_KPI.xaml тепер активна

    IT_KPI.IsSelected = true;

В мене конструктор виглядає так:

    public MainPage()
        {
            this.InitializeComponent();
            MyFrame.Navigate(typeof(IT_KPI));
 	       TitleTextBlock.Text = "IT KPI";
            BackButton.Visibility = Visibility.Collapsed;
            IT_KPI.IsSelected = true;
        }

Змінимо вміст ListBox_SelectionChanged так, щоб він реагував на переключення пунктів меню і показував бажану сторінку.

        private void ListBox_SelectionChanged
              (object sender, SelectionChangedEventArgs e)
        {
            if (IT_KPI.IsSelected)
            {
                MyFrame.Navigate(typeof(IT_KPI));
                TitleTextBlock.Text = "IT KPI";
            }
            else if (MS_KPI.IsSelected)
            {
                MyFrame.Navigate(typeof(MS_KPI));
                TitleTextBlock.Text = "Microsoft KPI Group";
            }
        }

БДЩ, тепер наш додаток реагує на перемикання пунктів меню!

![](/images/2016/02/1455047777_dc24e7d28c324ac2a90135d8e8393ab5.jpg)

Задамо невеликий відступ між кнопкою «Назад» і назвою сторінки. Йдемо в MainPage.xaml, знаходимо `<TextBlock>` на ім’я TitleTextBlock і дописуємо йому `Margin="20,5,0,0"`. Ще не зайвим буде додати відступ у 10 пікселів для `<Frame>` у самому низу:

    <Frame Name="MyFrame" Margin="10">
    </Frame>

Виглядає явно красивіше.

![](/images/2016/02/1455047835_153788d21816476dbc876c2cea1f071d.jpg)

Кнопка «Назад» повинна вести на головну сторінку і зникати на ній. Натомість мусить відображатись на всіх інших сторінках. Це робиться відносно просто.

Повертаємось до нашого методу ListBox_SelectionChanged і додаємо дві стрічки, що приховують і відображають кнопку в залежності від того, на якій сторінці зараз користувач.

    private void ListBox_SelectionChanged
                   (object sender, SelectionChangedEventArgs e)
        {
            if (IT_KPI.IsSelected)
            {
                MyFrame.Navigate(typeof(IT_KPI));
                TitleTextBlock.Text = "IT KPI";
                BackButton.Visibility = Visibility.Collapsed;
            }
            else if (MS_KPI.IsSelected)
            {
                BackButton.Visibility = Visibility.Visible;
                MyFrame.Navigate(typeof(MS_KPI));
                TitleTextBlock.Text = "Microsoft KPI Group";
            }
        }


Єдине, що лишилось – вдихнути трохи життя в кнопку «Назад». Прямуємо до методу BackButton_Click і наповнюємо його:

    private void BackButton_Click
                   (object sender, RoutedEventArgs e)
        {
            if (MyFrame.CanGoBack)
            {
                MyFrame.GoBack();
                IT_KPI.IsSelected = true;
            }
        }


Код всіх трьох методів разом з конструктором:

    public MainPage()
        {
            this.InitializeComponent();
            MyFrame.Navigate(typeof(IT_KPI));
            TitleTextBlock.Text = "IT KPI";
            BackButton.Visibility = Visibility.Collapsed;
            IT_KPI.IsSelected = true;
        }

        private void HamburgerButton_Click
                   (object sender, RoutedEventArgs e)
        {
            MySplitView.IsPaneOpen = !MySplitView.IsPaneOpen;
        }

        private void BackButton_Click
                   (object sender, RoutedEventArgs e)
        {
            if (MyFrame.CanGoBack)
            {
                MyFrame.GoBack();
                IT_KPI.IsSelected = true;
            }
        }

        private void ListBox_SelectionChanged
                   (object sender, SelectionChangedEventArgs e)
        {
            if (IT_KPI.IsSelected)
            {
                MyFrame.Navigate(typeof(IT_KPI));
                TitleTextBlock.Text = "IT KPI";
                BackButton.Visibility = Visibility.Collapsed;
            }
            else if (MS_KPI.IsSelected)
            {
                BackButton.Visibility = Visibility.Visible;
                MyFrame.Navigate(typeof(MS_KPI));
                TitleTextBlock.Text = "Microsoft KPI Group";
            }
        }


Тепер можна запустити додаток і оцінити, що у нас вийшло. На цьому все, дякую за увагу! Сподіваюсь, було корисно.

![](/images/2016/02/1455047910_4f84c01d95f9412a927eb6458f7a9d4e.jpg)



![](/images/2016/02/1455047911_9ab4db5c25d7466f998a60d5bab1b933.jpg)

Tags: dotNet, csharp

