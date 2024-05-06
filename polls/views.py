from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, worldd, You're at the polls index.")
