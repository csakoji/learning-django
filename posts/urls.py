from django.urls import path
from .views import ViewAllPosts, ViewPostDetails, UpdatePost, DeletePost, CreatePost

urlpatterns = [
    path('', ViewAllPosts.as_view(), name='home'),
    path('<int:pk>/details/', ViewPostDetails.as_view(), name='post_details'),
    path('<int:pk>/update/', UpdatePost.as_view(), name='update_post'),
    path('<int:pk>/delete/', DeletePost.as_view(), name='delete_post'),
    path('create_post/', CreatePost.as_view(), name='create_post'),
]
