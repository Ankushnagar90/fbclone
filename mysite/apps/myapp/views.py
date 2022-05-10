
# Create your views here.

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, DeleteView,UpdateView
from myapp.forms import SignUpForm,LoginForm,NewPostForm
from myapp.models import Post



# Sign Up View
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('myapp:login')
    template_name = 'myapp/signup.html'



class ProfileView(TemplateView):
    template_name = 'myapp/profile.html'



class PhotoUploadView(CreateView):
    form_class = NewPostForm
    template_name = 'myapp/upload.html'
    success_url = reverse_lazy('myapp:home')



class PostList(ListView):
    model = Post
    template_name = 'myapp/home.html'
    queryset = Post.objects.all()


class PostDelete(DeleteView):
    model = Post
    template_name = 'myapp/confirm_del.html'
    success_url = reverse_lazy('myapp:home')

class PostUpdate(UpdateView):
    model = Post
    fields = [
        "title",
        "description",
    ]
    template_name = 'myapp/postupdate.html'
    success_url = reverse_lazy('myapp:home')






















# class PhotoDetailView(DetailView):
#     form_class = NewPostForm
#     template_name = 'myapp/upload.html'
#     context_object_name = 'posting'
#     success_url = reverse_lazy('myapp:upload')





    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['image'] = Post.objects.all()
    #     return context



# class NewPostView(CreateView):
#     form_class = NewPostForm
#     # success_url = reverse_lazy('post_list')
#     template_name = 'myapp/dashboard.html'


# class LoginView(CreateView):
#     form_class = LoginForm
#     # template_name = 'myapp/login.html'