from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Organisation(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель записи',blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50, null=True, verbose_name='Название')
    schedule  = models.TextField(null=True, verbose_name='График работы')
    owner = models.CharField(max_length=50, null=True, verbose_name='Владелец')
    contacts = models.TextField(null=True, verbose_name='Контакты')
    address = models. CharField(max_length=200, null=True, verbose_name='Адрес')
    # active = models.BooleanField(default=True,verbose_name='Организация активна')

    class Meta:
        verbose_name =  'Организация'
        verbose_name_plural = 'Организации'

    def __str__(self):
        return self.name

class Comments(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, verbose_name='Организация',blank=True, null=True, related_name='comments_org')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария',blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)
    text  = models.TextField(null=True, verbose_name='Текст комментария')
    status = models.BooleanField(default=False,verbose_name='Видимость комментария')