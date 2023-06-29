from django.views import generic


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


def register(request):
    return None


def login(request):
    return None