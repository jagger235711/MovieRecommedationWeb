"""
存放models
用于设定对象的属性和操作
"""

# Create your models here.
import string
import json
import requests
from urllib.parse import quote

from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import get_object_or_404


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

    def __str__(self):
        if self.release_date and self.directors:
            return f'{self.name}------导演：{self.directors}, 上映日期：{self.release_date}'

        else:
            return self.name
# 这是属于数据获取的内容，不应该放在models里面
    # @staticmethod
    # def get_baidu_cover(self):
    #     if self.cover:
    #         return self.cover
    #
    #     name = self.name.replace(' ', '+')
    #     suffix = '电影海报'
    #     count_time_out = 0
    #
    #     while True:
    #         print(name + suffix)
    #         url_path = f"https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={name}{suffix}cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word={name}{suffix}"
    #         url_path = quote(url_path, safe=string.printable)
    #
    #         response = requests.get(url_path)
    #         source = response.text
    #
    #         try:
    #             data = json.loads(source)
    #             break
    #         except json.JSONDecodeError:
    #             suffix = ['海报', '图片', '电影', '', '百度', ' ',
    #                       '。', '+豆瓣', '+海报', '+图片', '百度图片'][count_time_out]
    #             count_time_out += 1
    #             if count_time_out == 12:
    #                 raise TimeoutError("图片找不到")
    #             continue
    #
    #     for dict_imgs in data['data']:
    #         img_url = dict_imgs.get('thumbURL')
    #         if img_url:
    #             img_response = requests.get(img_url)
    #             if img_response.status_code == 200:
    #                 self.cover = img_url
    #                 self.save()
    #                 return img_url
    #
    #     raise get_object_or_404(TimeoutError, "图片找不到")
    #
    # def get_cover(self):
    #     if not self.cover:
    #         self.cover = self.get_baidu_cover(self)
    #         self.save()

    class Meta:
        '''
        Meta 类是用于定义模型的元数据。元数据是关于模型的一些附加信息，如排序方式、数据库表名称等。这些信息不是模型中的字段或方法，而是与模型本身相关的配置选项。
        '''
        ordering = ['-douban_votes', '-douban_score']


from PIL import Image


class Profile(models.Model):
    '''
    用户的其他资料，与基础模型user一对一关联
    '''
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # image = models.ImageField(default=None, upload_to="./")
    # favorite_movies = models.ManyToManyField('Movie', default=None)
    # is_first_login = models.BooleanField(default=True)  # 标志用户是否为第一次登陆
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_movies = models.ManyToManyField(Movie, related_name="users_who_like", blank=True)
    is_first_login = models.BooleanField(default=True)  # 标志用户是否为第一次登陆

    def __str__(self):
        # movie_list = [movie.name for movie in self.favorite_movies.all()]
        # movie_string = ", ".join(movie_list)
        # return f"{self.user.username}喜欢的电影: {movie_string}"
        return self.user.username
