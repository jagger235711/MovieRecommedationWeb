# Create your tests here.
from django.contrib.auth.models import User
from django.test import TestCase, Client

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

    class MyLoginViewTest(TestCase):
        def setUp(self):
            self.client = Client()

        def test_form_invalid_with_errors(self):
            # 创建一个POST请求并传递无效的登录数据
            response = self.client.post('/login/', {'username': '', 'password': ''}, follow=True)

            # 检查请求的响应状态码是否是200
            self.assertEqual(response.status_code, 200)

            # 检查模板是否使用了正确的模板名称
            self.assertTemplateUsed(response, 'userWeb/registration/login.html')

            # 检查模板变量是否包含错误消息
            self.assertIn('some_message', response.context)
            self.assertEqual(response.context['some_message'], 'field is required')

        def test_form_invalid_without_errors(self):
            # 创建一个POST请求并传递有效的登录数据
            response = self.client.post('/login/', {'username': 'testuser', 'password': 'testpassword'}, follow=True)

            # 检查请求的响应状态码是否是200
            self.assertEqual(response.status_code, 200)

            # 检查模板是否使用了正确的模板名称
            self.assertTemplateUsed(response, 'userWeb/registration/login.html')

            # 检查模板变量是否不包含错误消息
            self.assertNotIn('some_message', response.context)
