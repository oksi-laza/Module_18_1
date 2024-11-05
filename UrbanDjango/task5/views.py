from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


# Create your views here.
def sign_up_by_html(request):
    users = ['Max', 'Alex', 'Rita', 'Liza', 'Den']
    info = {}
    if request.method == 'POST':
        # Получаем данные
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        # Проверим выводом в консоли, что данные, отправленные пользователем, обработаны и получены сервером (для себя)
        print(f'Username: {username}. Password: {password}. Repeat_password: {repeat_password}. Age: {age}.')

        if password == repeat_password and int(age) >= 18 and username not in users:
            return HttpResponse(f'Приветствуем, {username}!')
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
    return render(request, 'fifth_task/registration_page.html', {'info': info})


def sign_up_by_django(request):
    users = ['Max', 'Alex', 'Rita', 'Liza', 'Den']
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            # Проверим выводом в консоли, что данные, отправленные пользователем, обработаны и получены сервером (для себя)
            print(form.cleaned_data)

            if password == repeat_password and int(age) >= 18 and username not in users:
                return HttpResponse(f'Приветствуем, {username}!')
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
    else:    # Если это GET-запрос
        form = UserRegister()
    return render(request, 'fifth_task/registration_page_django.html', {'info': info, 'form': form})
