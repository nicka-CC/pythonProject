from django.urls import path

from . import views
app_name = 'news'
urlpatterns = [
    path("", views.index, name="index"),
    path("item/<int:pk>", views.detail, name="news_item"),
]