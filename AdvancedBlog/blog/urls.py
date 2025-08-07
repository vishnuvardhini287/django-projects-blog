from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # this matches "/en/"
    path('create/', views.create_post, name='create_post'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('', views.home, name='home'),  # This is matched by /en/, /es/, etc.
]
    


