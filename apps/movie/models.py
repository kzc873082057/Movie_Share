# coding:itf-8
from django.db import models
from datetime import datetime


# Create your models here.

class Movie_Type(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="movie_主键")
    name = models.CharField(max_length=20, verbose_name="电影类型")
    def __str__(self):
        return self.name

class Movie_Image(models.Model):
    pass



class Movie(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="movie_主键")
    name = models.CharField(max_length=30, verbose_name="电影名称")
    cover = models.ImageField(upload_to="media\\image\\", verbose_name="封面")
    update_time = models.DateTimeField(verbose_name="上传时间", default=datetime.now())
    click_rate = models.IntegerField(default=0, verbose_name="点击量")
    director = models.CharField(max_length=20, verbose_name="导演")
    screenwriter = models.CharField(max_length=50, verbose_name="编剧")
    star = models.CharField(max_length=100, verbose_name="主演")
    region = models.CharField(max_length=20, verbose_name="地区")
    public_time = models.DateField(verbose_name="上映时间")
    movie_time = models.CharField(max_length=10, verbose_name="时长")
    score = models.CharField(max_length=50, verbose_name="评分")
    profile = models.TextField(verbose_name="简介")
    download = models.URLField(verbose_name="下载地址")
    screenshot = models.ImageField(verbose_name="电影截图")
    movie_type = models.ForeignKey(Movie_Type, verbose_name="电影类型")

    def __str__(self):
        return self.name
