from django.shortcuts import render

from blog.models import Blog
from main.models import Service, Category


# Create your views here.
def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'Новый контакт!\n{name} ({email}) написал: {message}\n')
    return render(request, 'core/contacts.html')


def home(request):
    blog_top = Blog.objects.all().values('title', 'body', 'preview', 'pk', )[:3]
    service = Service.objects.filter(is_available=True, category_id=38)
    context = {
        'blog': blog_top,
        'service': service
    }
    return render(request, 'core/home.html', context)
