# todo 引入自带的contribAPP做用户登录登出等操作


from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
from django.db import transaction
from django.forms import model_to_dict
from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic

from MovieRecommedationWeb import forms as my_forms
from MovieRecommedationWeb.forms import RegistrationForm
from userWeb.models import Profile


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


class UserProfileView(generic.DetailView):
    model = User
    template_name = "userWeb/users/profile.html"
    context_object_name = "user"

    def get(self, request, *args, **kwargs):
        user = self.get_object()  # 获取User对象
        user_values = model_to_dict(user)
        print(user_values)
        # profile = Profile.objects.get(user=user)  # 获取关联的Profile对象
        #
        # print(profile)
        exclude_fields = ['password', 'last_login', 'is_superuser', 'groups', 'user_permissions']
        filtered_user_values = {key: value for key, value in user_values.items() if key not in exclude_fields}

        context = {
            "user": user,
            "filtered_user_values": filtered_user_values,
            # "profile": profile,
        }
        return render(request, self.template_name, context)


class MyPasswordResetView(PasswordResetView):
    template_name = 'userWeb/registration/password_reset.html'
    success_url = 'userWeb:login'
    form_class = my_forms.MyPasswordResetForm

    def form_valid(self, form):
        email = form.cleaned_data['email']
        user_name = form.cleaned_data['user_name']

        try:
            user = get_object_or_404(User, email=email, username=user_name)
            self.request.session['reset_password'] = True
            messages.success(self.request, "修改成功！")
            return redirect('userWeb:login')  # 跳转到重置密码页面
        except Http404:
            messages.error(self.request, '用户不存在，请重新输入。')
            return redirect('userWeb:password_reset')  # 用户不存在时，重定向回到表单页面并显示错误消息


def admin(request):
    return None

    # class RegisterView(generic.FormView):
    #     template_name = 'userWeb/registration/register.html'
    #     form_class = forms.RegistrationForm
    #     success_url = 'userWeb:index'
    #
    #     def form_valid(self, form):
    #         user = form.save()
    #         login(self.request, user)
    #         return super().form_valid(form)
    #
    #     def form_invalid(self, form):
    #         return redirect('userWeb:login')  # 跳转到login页面


def register_request(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = form.save()
                    user_profile = Profile.objects.create(user=user, is_first_login=1)
                    login(request, user)
                    messages.success(request, "注册成功！")
                    return redirect("userWeb:index")
            except Exception as e:
                messages.error(request, str(e))

    else:
        form = RegistrationForm()

    context = {"register_form": form}

    if form.errors:
        context["error_form"] = form
        messages.error(request, "注册失败！")

    return render(request=request, template_name="userWeb/registration/register.html", context=context)
