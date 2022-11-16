from django.shortcuts import render, redirect

from .models import Theme, Translation


def index(request):
    color_bg = color_fg = color_win = ''
    title = dropdown = slide11 = slide12 = slide21 = slide22 = slide31 = slide32 = ''
    figure11 = figure12 = figure21 = figure22 = figure31 = figure32 = figure41 = figure42 = ''
    article_title = article_column1 = article_column2 = llc = language = ''

    if Theme.objects.filter(user=request.user.username).exists():
        color_bg = Theme.objects.get(user=request.user.username).color
        if color_bg == '#212529':
            color_fg = '#ffffff'
            color_win = '#1E1F1F'
        elif color_bg == '#ffffff':
            color_fg = '#212529'
            color_win = '#EEEEEE'

    if Translation.objects.filter(user=request.user.username).exists():
        language = Translation.objects.get(user=request.user.username).language

        if language == 'english':
            title = 'Business card'
            dropdown = 'Language'

            slide11 = 'Software product development'
            slide12 = 'Writing websites on the Django framework with PostgreSQL'
            slide21 = 'Interest in UX/UI design'
            slide22 = 'Creating interfaces on Figma and also Adobe Illustrator'
            slide31 = 'Publication of a scientific article on the topic'
            slide32 = 'Implementation of IT in education as a means of increasing efficiency'

            figure11 = 'Website for writing records'
            figure12 = 'github.com/thekarenovich/improved_web_page_psql'
            figure21 = 'Website for viewing blog articles'
            figure22 = 'github.com/thekarenovich/my_blog'
            figure31 = 'Business card website'
            figure32 = 'github.com/thekarenovich/business_card'
            figure41 = 'Telegram bot'
            figure42 = 'github.com/thekarenovich/Projects/tree/main/bot'

            article_title = 'Vibrant city photography that never sleeps'

            article_column1 = '''Welcome to the home of royalty-free, high-quality city photos. 
            Here, you can browse and download a vast array of professionally shot city snaps. 
            You’ll find pictures of groups socializing, busy construction workers, tourist attractions, 
            skyscraper-filled skylines, and picturesque cityscapes. 
            You’ll find images of the inner city, commercial office towers, bridges, residential roads, 
            and even alleyways with graffiti. Moreover, 
            our photographers have gone out of their way to capture cities during the four seasons of the year, 
            capturing the beauty of the summer, winter, autumn, and spring in the city. W
            hether you’re a student working on a project, a construction company, a property agency, or a travel blogger, 
            our city images will meet your requirements.'''

            article_column2 = '''My name is Eric Karenovich Khachatryan, I am 20 years old and I am a Python developer, actively developing products on the Django framework, storing project data on the PostgreSQL DBMS and visualizing them using HTML and CSS, while having experience working with modules such as: asyncio, bs4, requests, socket, numpy, matplotlib and with many others. Also, during the design and training, I mastered and applied MySQL, MongoDB and Git version control systems, BPMN diagrams and others, data processing structures and algorithms in Python, jQuery (JavaScript library). In addition to programming, fragments were also designed on the Figma service for a clear representation of the front part of the product, and a scientific article was written, after the publication of which work began immediately next.'''

            llc = 'LLC'

        elif language == 'russian':
            title = 'Визитная карточка'
            dropdown = 'Язык'

            slide11 = 'Разработка программного продукта'
            slide12 = 'Написание сайтов на фреймворке Django c PostgreSQL'
            slide21 = 'Интерес к UX/UI дизайну'
            slide22 = 'Создание интерфейсов на Figma и Adobe Illustrator'
            slide31 = 'Публикация научной статьи на тему'
            slide32 = 'Внедрение ИТ в образование, как средство повышения эффективности'

            figure11 = 'Сайт для написания записей'
            figure12 = 'github.com/thekarenovich/improved_web_page_psql'
            figure21 = 'Сайт для просмотра блога статей'
            figure22 = 'github.com/thekarenovich/my_blog'
            figure31 = 'Сайт-визитка'
            figure32 = 'github.com/thekarenovich/business_card'
            figure41 = 'Телеграм-бот'
            figure42 = 'github.com/thekarenovich/Projects/tree/main/bot'

            article_title = 'Я занимаюсь веб-дизайном и созданием сайтов'

            article_column1 = '''Добро пожаловать в дом бесплатных высококачественных фотографий города.
            Здесь вы можете просмотреть и загрузить огромное количество профессионально снятых снимков города.
            Вы найдете фотографии общающихся групп, занятых строителей, туристических достопримечательностей, 
            небоскребов и живописных городских пейзажей. Вы найдете изображения внутреннего города, 
            коммерческих офисных башен, мостов, жилых дорог и даже переулков с граффити. 
            Более того, наши фотографы приложили все усилия, чтобы запечатлеть города в течение четырех сезонов года, 
            запечатлев красоту лета, зимы, осени и весны в городе. 
            Являетесь ли вы студентом, работающим над проектом, строительной компанией, 
            агентством недвижимости или блогером о путешествиях, наши изображения городов будут соответствовать вашим требованиям.'''

            article_column2 = '''Меня зовут Хачатрян Эрик Каренович, мне 20 лет и я являюсь Python-разработчиком, активно разрабатывая продукты на фреймворке Django, храня данные проектов на СУБД PostgreSQL и визуализирую их при помощи HTML и CSS, при этом имея опыт работы с такими модулями, как: asyncio, bs4, requests, socket, numpy, matplotlib и со многими другими. Также в ходе проектирования и обучения мною были освоены и применены команды MySQL, MongoDB и системы контроля версий Git, диаграммы BPMN и другие, структуры и алгоритмы обработки данных на Python, JQuery(библиотека JavaScript). Помимо программирования были также спроектированы фрагменты на сервисе Figma для четкого представления фронтальной части продукта, а также была написана научная статья, после публикации которой началась работа сразу следующей.'''

            llc = 'ООО'

    return render(request, 'main/index.html', {'color_bg': color_bg, 'color_fg': color_fg, 'color_win': color_win,
                                               'title': title, 'dropdown': dropdown,
                                               'slide11': slide11,  'slide12': slide12,
                                               'slide21': slide21,  'slide22': slide22,
                                               'slide31': slide31,  'slide32': slide32,
                                               'figure11': figure11, 'figure12': figure12,
                                               'figure21': figure21, 'figure22': figure22,
                                               'figure31': figure31, 'figure32': figure32,
                                               'figure41': figure41, 'figure42': figure42,
                                               'article_title': article_title,
                                               'article_column1': article_column1,
                                               'article_column2': article_column2,
                                               'llc': llc, 'language': language
                                               })


def theme(request):
    color = request.GET.get('color')

    if color == 'dark':
        if Theme.objects.filter(user=request.user.username).exists():
            user_theme = Theme.objects.get(user=request.user.username)
            user_theme.user = request.user.username
            user_theme.color = '#212529'
            user_theme.save()
        else:
            user2 = Theme(user=request.user.username, color='black')
            user2.save()

    elif color == 'light':
        if Theme.objects.filter(user=request.user.username).exists():
            user_theme1 = Theme.objects.get(user=request.user.username)
            user_theme1.user = request.user.username
            user_theme1.color = '#ffffff'
            user_theme1.save()
        else:
            user4 = Theme(user=request.user.username, color='white')
            user4.save()

    return redirect('/')


def translation(request):
    language = request.GET.get('language')

    if language == 'russian':
        if Translation.objects.filter(user=request.user.username).exists():
            user_translation = Translation.objects.get(user=request.user.username)
            user_translation.user = request.user.username
            user_translation.language = 'russian'
            user_translation.save()
        else:
            user2 = Translation(user=request.user.username, language='russian')
            user2.save()

    elif language == 'english':
        if Translation.objects.filter(user=request.user.username).exists():
            user_translation1 = Translation.objects.get(user=request.user.username)
            user_translation1.user = request.user.username
            user_translation1.language = 'english'
            user_translation1.save()
        else:
            user4 = Translation(user=request.user.username, language='english')
            user4.save()

    return redirect('/')
