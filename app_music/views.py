
from django.shortcuts import render
from app_music.models import Album,Track, Artist, Tag
def home(request):
    ctx={}
    return render(request, 'home.html', {'album':Album.objects.first()})