from annoying.decorators import render_to
from django.contrib.auth.models import User


# @render_to('hello/home.html')
# def home(request):
#     users = User.objects.filter()
#     return {'users': users}
from django.views.generic import ListView
from django_hello_world.hello.models import Person


class PersonView(ListView):
    """
    Viwing person data on page
    """
    model = Person
    template_name = "main_page.html"