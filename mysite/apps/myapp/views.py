
# Create your views here.

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView ,TemplateView
from myapp.forms import SignUpForm,LoginForm

# Sign Up View
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('myapp:login')
    template_name = 'myapp/signup.html'


# class LoginView(CreateView):
#     form_class = LoginForm
#     # template_name = 'myapp/login.html'


class ProfileTemplateView(TemplateView):

    template_name = 'myapp/profile.html'




