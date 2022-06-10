from django.urls import path
from api_view.api_views import PostListAPIView,PostDetailAPIView

urlpatterns = [
	path('', PostListAPIView.as_view()),
	path('<int:pk>', PostDetailAPIView.as_view()),
	# path('', PostCreateAPIView.as_view()),
]