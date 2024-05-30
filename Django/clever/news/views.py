from django.shortcuts import render
from .models import News

def index(request):
    news = News.objects.all()
    title = "Главная страница"
    return render(request, 'news/news_list.html', {'title': title, 'news': news})

def detail(request, pk):
    news = News.objects.get(pk=pk)
    title = news.title
    return render(request, 'news/news_item.html', {'title': title, 'news': news})