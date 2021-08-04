from django.conf import settings
from django.db import models


class Search(models.Model):
    keyword1 = models.CharField('キーワード1', max_length=128)
    keyword2 = models.CharField('キーワード2', max_length=128)
    keyword3 = models.CharField('キーワード3', max_length=128)
    
    created_at = models.DateTimeField("作成日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    def __str__(self):
        return self.keyword1
