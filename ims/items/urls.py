from django.urls import path
from .views import home,post_list,post
urlpatterns = [
    path('', home, name='home'),
    path('<int:pk>/', post, name='post'),
    path('post-list/', post_list, name='post_list'),
    
]