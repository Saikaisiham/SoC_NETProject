from django.urls import path
from .views import (
    create_post,
    # like_post,
    # posts
)

app_name = 'Post'

urlpatterns = [
    path('', create_post, name='create_post'),
    # path('post/<int:pk>/like/', like_post, name='like_post'),
    # path('post', posts, name='posts')
]