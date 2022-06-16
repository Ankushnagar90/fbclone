from django.urls import path
from api_view.api_views import PostListAPIView,PostDetailAPIView,UserLoginAPI,UserLogoutAPI,UserProfileUpdateView,DeleteAPIView

urlpatterns = [
	path('', PostListAPIView.as_view()),
	path('login/', UserLoginAPI.as_view(), name='login'),
	path('logout/', UserLogoutAPI.as_view(), name='logout'),
	path('update/', UserProfileUpdateView.as_view(), name='update'),
	path('delete/', DeleteAPIView.as_view(), name='delete'),
	path('<int:pk>', PostDetailAPIView.as_view()),
]