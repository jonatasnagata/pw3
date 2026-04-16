from django.http import HttpResponse


def index(request):
    return HttpResponse("Texto que vai aparecer")