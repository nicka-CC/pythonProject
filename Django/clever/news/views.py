from datetime import datetime

from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import News, Comments
from .forms import NewsModelForm, CommentModelForm

def index(request):
    news = News.objects.all()
    search = request.GET.get("search")
    if search:
        news = news.filter(title__icontains=search)
    paginator= Paginator(news, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    title = "Главная страница"
    return render(request, 'news/news_list.html', {'title': title, 'page_obj': page_obj})

def detail(request, pk):
    newss = News.objects.all()
    news = newss.get(pk=pk)
    title = news.title

    first = newss.first().id
    last = newss.last().id
    count = str(request.GET.get("post"))
    comments = Comments.objects.filter(news=news).order_by("-date_published")
    if count == 'prev':
        if news.id == first:
            return redirect('news:news_item',pk=last )
        prev_news = newss.filter(id__lt=news.id).last()
        return redirect('news:news_item',pk=prev_news.id)
    if count == 'next':
        if news.id == last:
            return redirect('news:news_item', pk=first)
        next_news = newss.filter(id__gt=news.id).first()
        return redirect('news:news_item', pk=next_news.id)
    context = {
        "news": news,
        "title": title,
        "comments": comments
    }
    if request.method == "POST":
        form = CommentModelForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.news = news
            new_comment.save()
            return redirect("news:news_item", pk=pk)
    else:
        form = CommentModelForm()
    context["form"] = form
    return render(request, 'news/news_item.html', context)

def create_news(request):
    title = "Создание новости"
    action = "Создать"
    if request.method == "POST":
        form = NewsModelForm(request.POST, request.FILES)
        if form.is_valid():
            new_news = form.save(commit=False)
            new_news.author = request.user
            new_news.date_published = datetime.now()
            new_news.save()
            return  redirect("item:index")
    else:
        form = NewsModelForm()
    return render(request, 'news/update_news.html', {"title": title, "form": form, "action": action})

def update_news(request, pk):

    action = "Изменить"
    news = News.objects.get(pk=pk)
    title = f'Редактирование {news.title}'
    if request.method == "POST":
        form = NewsModelForm(request.POST, request.FILES,instance=news)
        if form.is_valid():
            form.save()
            return redirect("news:news_item", pk=pk)
    else:
        form = NewsModelForm(instance=news)
    return render(request, 'news/update_news.html', {"title": title, "form": form, "action": action})
