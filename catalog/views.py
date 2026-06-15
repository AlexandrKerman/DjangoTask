from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def contacts(request):
    if request.method == 'POST':
        print(f'Данные успешно отправлены методом POST.\n'
              f'Содержимое:\n'
              f'{[i for i in request.POST.items() if i[0] != 'csrfmiddlewaretoken']}')
    return render(request, 'contacts.html')