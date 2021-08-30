from django.urls import path
from .views import my_posts

urlpatterns = [
    path('', my_posts),
]