from django.urls import path

from . import views
app_name = 'news'
urlpatterns = [
    path("", views.index, name="index"),
    path("item/<int:pk>", views.detail, name="news_item"),
    path("create/", views.create_news, name="create_update_news"),
    path("update/<int:pk>/", views.update_news, name="update_news")
]