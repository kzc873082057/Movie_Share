# coding:itf-8
from django.db import models
from datetime import datetime

# Create your models here.

class Movie(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="movie_主键")
    name = models.CharField(max_length=30, verbose_name="电影名称")
    cover = models.ImageField(verbose_name="封面")
    time = models.DateTimeField(verbose_name="上传时间",default=datetime.now())


