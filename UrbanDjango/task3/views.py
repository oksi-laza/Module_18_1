from django.shortcuts import render


# Create your views here.
def sportic(request):
    title_h1 = 'Главная страница'
    menu_dict = {
        'Спорт для всех. Главная.': '#',
        'Спортивные секции для детей': '/sportic/sport_kids',
        'Спортивные секции для взрослых': '/sportic/sport_adults'
    }
    context = {
        'title_h1': title_h1,
        'menu_dict': menu_dict
    }
    return render(request, 'third_task/sportic.html', context)


def sport_kids(request):
    title_h1 = 'Спортивные секции для детей'
    menu_kids_list = [
        'Баскетбол',
        'Футбол',
        'Художественная гимнастика',
        'Спортивно-бальные танцы',
        'Плавание',
        'Карате',
        'Самбо'
    ]
    main_page = '/sportic'
    context = {
        'title_h1': title_h1,
        'menu_kids_list': menu_kids_list,
        'main_page': main_page
    }
    return render(request, 'third_task/sport_kids.html', context)


def sport_adults(request):
    title_h1 = 'Спортивные секции для взрослых'
    menu_adults_list = [
        'Бадминтон',
        'Баскетбол',
        'Бокс',
        'Футбол',
        'Айкидо',
        'Йога',
        'Фитнес',
        'Фехтование',
    ]
    main_page = '/sportic'
    context = {
        'title_h1': title_h1,
        'menu_adults_list': menu_adults_list,
        'main_page': main_page
    }
    return render(request, 'third_task/sport_adults.html', context)
