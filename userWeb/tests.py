from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User

from .models import Movie, Profile


class MovieModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # 创建一个电影实例用于测试
        Movie.objects.create(
            movie_id=1,
            name='下一任：前任',
            directors='Director 1',
            release_date='2022-01-01'
        )

    def test_movie_string_representation(self):
        movie = Movie.objects.get(movie_id=1)
        expected_string = '下一任：前任------导演：Director 1, 上映日期：2022-01-01'
        self.assertEqual(str(movie), expected_string)

    # def test_get_baidu_cover(self):
    #     movie = Movie.objects.get(movie_id=1)
    #     cover = movie.get_baidu_cover(movie.name)
    #     self.assertIsNotNone(cover)
    #
    # # 真实电影名才可能插入不为空
    # def test_get_cover(self):
    #     movie = Movie.objects.get(movie_id=1)
    #     movie.get_cover()
    #     self.assertIsNotNone(movie.cover)


class ProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # 创建一个用户用于测试
        user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        Profile.objects.create(user=user)

    def test_profile_string_representation(self):
        profile = Profile.objects.get(user__username='testuser')
        expected_string = 'testuser'
        self.assertEqual(str(profile), expected_string)

    def test_favorite_movies(self):
        profile = Profile.objects.get(user__username='testuser')
        movie = Movie.objects.create(movie_id=2, name='Test Movie 2')
        profile.favorite_movies.add(movie)

        self.assertEqual(profile.favorite_movies.count(), 1)
        self.assertIn(movie, profile.favorite_movies.all())

    def test_is_first_login(self):
        profile = Profile.objects.get(user__username='testuser')
        self.assertTrue(profile.is_first_login)
