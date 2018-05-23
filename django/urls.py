from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$',views.index,name='index'),
        url(r'^getMp3$',views.getMp3,name='getMp3'),
        url(r'^download/(?P<file_name>.+)$',views.download,name='download'),
    ]
