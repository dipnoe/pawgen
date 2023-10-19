from main.models import Category


def dropdown(request):
    context = {
        'categories': Category.objects.all()
    }
    return context
