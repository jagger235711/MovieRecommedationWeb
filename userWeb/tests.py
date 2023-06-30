from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Movie, Profile

class MovieModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # 在每个测试方法之前执行的方法，用于创建测试数据
        Movie.objects.create(
            movie_id=1,
            name="Movie 1",
            directors="Director 1",
            genres="Genre 1",
            douban_votes=10,
            douban_score=8,
            release_date="1.1.1"
        )

    def test_str_representation(self):
        movie = Movie.objects.get(movie_id=1)
        self.assertEqual(str(movie), "Movie 1------导演：Director 1, 上映日期：1.1.1, 类型：Genre 1")

    def test_ordering(self):
        movie = Movie.objects.get(movie_id=1)
        self.assertEqual(Movie._meta.ordering, ['-douban_votes', '-douban_score'])


class ProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # 创建一个用户用于测试
        User.objects.create_user(username='testuser', password='testpassword')
        Profile.objects.create(user=User.objects.get(username='testuser'), is_first_login=True)

    # def test_str_representation(self):
    #     profile = Profile.objects.get(user__username='testuser')
    #     self.assertEqual(str(profile), "testuser ------ 账户创建时间： 2022-01-01 00:00:00, 是否为新用户： True")

    def test_favorite_movies(self):
        profile = Profile.objects.get(user__username='testuser')
        movie = Movie.objects.create(
            movie_id=2,
            name="Movie 2",
            directors="Director 2",
            genres="Genre 2",
            douban_votes=5,
            douban_score=7
        )
        profile.favorite_movies.add(movie)
        self.assertEqual(profile.favorite_movies.count(), 1)
        self.assertTrue(movie in profile.favorite_movies.all())

    def test_first_login_flag(self):
        profile = Profile.objects.get(user__username='testuser')
        self.assertEqual(profile.is_first_login, True)
        profile.is_first_login = False
        profile.save()
        self.assertEqual(Profile.objects.get(user__username='testuser').is_first_login, False)