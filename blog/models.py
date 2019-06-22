from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField('タイトル', max_length=200)
    text = models.TextField('本文')
    created_date = models.DateTimeField('作成日時', default=timezone.now)
    published_date = models.DateTimeField('公開日時', blank=True, null=True)


    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title