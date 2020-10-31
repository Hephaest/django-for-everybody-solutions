from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. 7d5c5d75 is the polls index.")