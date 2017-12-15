from django.conf.urls import url
from django.urls import path
from vid import views
urlpatterns = [
    path('video/<int:video_id>/', views.video, name='video_detail'),
    url(r'^$', views.index, name='index'),
]
