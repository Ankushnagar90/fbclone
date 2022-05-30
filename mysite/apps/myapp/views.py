
from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, DeleteView,UpdateView, DetailView
from myapp.forms import SignUpForm,LoginForm,NewPostForm
from myapp.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.models import User
from django.template.loader import render_to_string
try:
    from django.utils import simplejson as json
except:
    import json

from django.http import JsonResponse
# from django.contrib.auth.decorators import login_required
# from django.views.decorators.http import require_POST
# from django.contrib.auth.decorators import login_required


# Sign Up View

class index(TemplateView):
    template_name='myapp/fb_index.html'

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('myapp:login')
    template_name = 'myapp/signup.html'


    def your_signup(request):
        if request.user.is_authenticated():
            return HttpResponseRedirect('myapp:home')


class ProfileView(LoginRequiredMixin,DetailView):
    model = User
    template_name = 'myapp/profile.html'
    login_url = '/login/'


class UserUpdate(UpdateView):
    model = User
    fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            ]
    template_name = 'myapp/user_update.html'
    success_url = reverse_lazy('myapp:home')


class CreatePostView(LoginRequiredMixin,CreateView):
    form_class = NewPostForm
    template_name = 'myapp/create_post.html'
    success_url = reverse_lazy('myapp:home')
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostList(LoginRequiredMixin,ListView):
    form_class = NewPostForm
    template_name = 'myapp/home.html'
    queryset = Post.objects.all()
    login_url = '/login/'


class PostDelete(DeleteView):
    model = Post
    template_name = 'myapp/confirm_del.html'
    success_url = reverse_lazy('myapp:home')

class PostUpdate(UpdateView):
    model = Post
    fields = [
        "title",
        "description",
        "pic",
        ]
    template_name = 'myapp/post_update.html'
    success_url = reverse_lazy('myapp:home')


class PostDetail(DetailView):
    model = Post
    template_name = 'myapp/post_detail.html'

    # def get_context_data(self, **kwargs):
    #     data = super().get_context_data(**kwargs)

    #     likes_connected = get_object_or_404(Post, id=self.kwargs['pk'])
    #     liked = False
    #     if likes_connected.likes.filter(id=self.request.user.id).exists():
    #         liked = True
    #     data['number_of_likes'] = likes_connected.number_of_likes()
    #     data['post_is_liked'] = liked
    #     return data

class UserPostListView(ListView):
    model = Post
    template_name = 'myapp/user_post_detail.html'
    context_object_name = 'user_posts'
    ordering = ['-date_posted']

    def get_queryset(self):
        author_username = self.request.user.username
        return Post.objects.filter(author__username=author_username).order_by("-date_posted")


# @login_required
# @require_POST

# class like_post(DetailView):
#     model = Post
#     # template_name = MainApp/BlogPost_detail.html
#     # context_object_name = 'object'

#     def get_context_data(self, **kwargs):
#         data = super().get_context_data(**kwargs)

#         likes_connected = get_object_or_404(Post, id=self.kwargs['pk'])
#         liked = False
#         if likes_connected.likes.filter(id=self.request.user.id).exists():
#             liked = True
#         data['number_of_likes'] = likes_connected.number_of_likes()
#         data['post_is_liked'] = liked
#         return data

        #Demo like post 

# def like_post(request,post_id):
#     import pdb; pdb.set_trace()  
#     if request.method == "POST":
#         id = post_id
#         U_id = request.user.id
#         is_liked = False
#         if Post.objects.filter(U_id).exists():
#             Post.objects.remove(U_id)
#             is_liked = False
#         else: 
            
#                 Post.objects.add(U_id)  
#                 is_liked = True

#                 context ={
#                     'post': Post,
#                     'is_liked': is_liked,
#                     'total_likes': Post.objects.count(),
#                     }
#         html = render_to_string('myapp/like_section.html', context, request=request)
#         # return render(request,'myapp/like_section.html' ,{'post': Post})

    

def like_post(request,pk):
    # import pdb; pdb.set_trace()
    if request.method == "POST":
        # import pdb; pdb.set_trace()
        
        # id = int(request.POST.get('pk'))
        post = get_object_or_404(Post,id=request.POST.get('post_id',pk))
        id=pk
        is_liked = False
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user.id)
            is_liked = False   
            post.save()
        else:
            post.likes.add(request.user.id)
            is_liked = True
            post.save()
   
        total_dict = {"total_likes" : post.total_likes() ,'is_liked':is_liked}
        return JsonResponse(total_dict)  

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