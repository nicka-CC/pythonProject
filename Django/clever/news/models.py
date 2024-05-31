from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class News(models.Model):
    title = models.CharField(max_length=200,verbose_name="Название события")
    content = models.TextField(verbose_name="Содержание события")
    date_published = models.DateTimeField(default=timezone.now,verbose_name="Дата публикации")
    image = models.ImageField(upload_to="images/",verbose_name="Изображение")
    author = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="Автор", null=True, blank=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("news:news_item", kwargs={"pk": self.pk})
class Comments(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name="Новости")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", null=True, blank=True)
    text = models.TextField(verbose_name="Содержание")
    date_published=models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")
    def __str__(self):
        return str(self.text)
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural="Комментарии"