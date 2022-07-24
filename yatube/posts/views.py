from django.http import HttpResponse


def index(request):
    return HttpResponse('Стартовая страница')


def group_posts(request, slug):
    return HttpResponse('Посты пользователя-ля-ля')
