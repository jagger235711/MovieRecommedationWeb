"""
存放models
用于设定对象的属性和操作
"""

# Create your models here.

from django.contrib.auth.models import User
from django.db import models


class Movie(models.Model):
    movie_id = models.IntegerField(unique=True)
    name = models.TextField()
    alias = models.TextField(null=True)
    actors = models.TextField(null=True)
    cover = models.TextField(null=True)
    directors = models.TextField(null=True)
    douban_score = models.FloatField(null=True)
    douban_votes = models.IntegerField(null=True)
    imdb_id = models.TextField(null=True)
    languages = models.TextField(null=True)
    mins = models.IntegerField(null=True)
    official_site = models.TextField(null=True)
    regions = models.TextField(null=True)
    release_date = models.TextField(null=True)
    storyline = models.TextField(null=True)
    genres = models.CharField(max_length=100, null=True)

    def __str__(self):
        if self.release_date and self.directors and self.genres:
            return f'{self.name}------导演：{self.directors}, 类型：{self.genres}, 上映日期：{self.release_date}'

        else:
            return self.name

    class Meta:
        '''
        Meta 类是用于定义模型的元数据。元数据是关于模型的一些附加信息，如排序方式、数据库表名称等。这些信息不是模型中的字段或方法，而是与模型本身相关的配置选项。
        '''
        ordering = ['-douban_votes', '-douban_score']


class Profile(models.Model):
    '''
    用户的其他资料，与基础模型user一对一关联
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_movies = models.ManyToManyField(Movie, related_name="users_who_like", blank=True)
    # 由于genres没有独立的模型，所以存储电影电影
    is_first_login = models.BooleanField(default=True)  # 标志用户是否为第一次登陆

    def __str__(self):
        res = f'{self.user.username} ------ 账户创建时间： {self.user.date_joined}'
        if self.is_first_login:
            return res + f', 是否为新用户： {self.is_first_login}'

        else:
            return res
