# todo 引入自带的contribAPP做用户登录登出等操作
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views import generic
from django.views.generic import FormView

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


def logout(request):
    return None


def admin(request):
    return None


# def register(request):
#     if request.method == 'POST':
#         form = forms.RegistrationForm(request.POST)
#         if form.is_valid():
#             user = User.objects.create_user(form.save())
#             return redirect('userWeb:home')
#     else:
#         form = forms.RegistrationForm()
#     return render(request, 'registration/register.html', {'form': form})
class RegisterView(generic.FormView):
    template_name = 'registration/register.html'
    form_class = forms.RegistrationForm
    success_url = 'userWeb:index'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        return redirect('userWeb:login')  # 跳转到login页面
