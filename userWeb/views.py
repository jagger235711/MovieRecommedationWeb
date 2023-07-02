# todo 引入自带的contribAPP做用户登录登出等操作

from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic

from MovieRecommedationWeb import forms


# Create your views here.
class IndexView(generic.ListView):
    template_name = "userWeb/movies/home.html"
    # 记得要把APP添加到settings.py的的INSTALLED_APPS中不然系统不知道这个app，就不会在这里找templates
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        # return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
        #        :5
        #        ]
        return


class MovieView(generic.ListView):
    template_name = "userWeb/movies/home.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """

        return


class UserView(generic.ListView):
    template_name = "userWeb/users/profile.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """

        return


class MyLogoutView(LogoutView):
    template_name = 'userWeb/registration/logout.html'


class MyLoginView(LoginView):
    template_name = 'userWeb/registration/login.html'
    success_url = ''

    # def form_invalid(self, form):
    #     # 执行登录失败后的额外操作
    #     # 这里可以记录登录失败日志或显示错误消息等操作
    #     # ...
    #
    #     # # 将表单验证错误信息转换为JSON字符串
    #     # errors_json = form.errors.as_json()
    #     #
    #     # # 解析JSON字符串
    #     # errors_data = json.loads(errors_json)
    #     # errors_data = errors_data{all}{code}
    #     errors_data = form.error_messages
    #     # 将错误信息传递给模板
    #     context = self.get_context_data(form=form, some_message=errors_data)
    #
    #     return self.render_to_response(context)


class MyPasswordResetView(PasswordResetView):
    template_name = 'userWeb/registration/password_reset.html'


def admin(request):
    return None


class RegisterView(generic.FormView):
    template_name = 'userWeb/registration/register.html'
    form_class = forms.RegistrationForm
    success_url = 'userWeb:index'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        return redirect('userWeb:login')  # 跳转到login页面
