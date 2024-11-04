from django.shortcuts import render


# Create your views here.
def sportic(request):
    title_h1 = 'Главная страница'
    context = {
        'title_h1': title_h1
    }
    return render(request, 'fourth_task/sportic.html', context)


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
    return render(request, 'fourth_task/sport_kids.html', context)


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
    return render(request, 'fourth_task/sport_adults.html', context)
