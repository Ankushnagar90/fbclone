from django.urls import path

from .import views
# from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
# from django.contrib.auth.decorators import login_required


app_name = 'myapp'
urlpatterns = [
    path('',auth_views.LoginView.as_view(template_name = 'myapp/login.html'),name='login'),
    path('signup/', views.SignUpView.as_view(),name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('upload/',views.PhotoUploadView.as_view(),name='upload'),
    path('home/',views.PostList.as_view(),name='home'),
    path('delete/<int:pk>/', views.PostDelete.as_view(),name='delete'),
    path('home/update/<int:pk>/', views.PostUpdate.as_view(),name='update'),

]