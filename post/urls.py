from django.conf import urls
from django.urls.conf import path
from . import views
app_name='post'
urlpatterns = [
    path('', views.all_posts),
    path('post/<int:pk>', views.post, name='post'),
    path('create/', views.createPost, name='createPost'),
    path('post/<int:pk>/edit', views.editPost, name='editPost'),
]
