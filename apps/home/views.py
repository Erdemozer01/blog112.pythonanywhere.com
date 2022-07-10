from django.shortcuts import render
from apps.home.models.cover import Cover

def index(request):
    covers = Cover.objects.all()
    return render(request, 'home/index.html', {'covers':covers})

