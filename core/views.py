from django.shortcuts import render


# Create your views here.
def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'Новый контакт!\n{name} ({email}) написал: {message}\n')
    return render(request, 'core/contacts.html')


def home(request):
    return render(request, 'core/home.html')
