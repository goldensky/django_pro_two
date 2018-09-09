from  django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/$', views.users, name='users'),
    url(r'^users/new/$', views.user_new, name='user_new'),

    url(r'^users/(?P<pk>\d+)/$', views.user_detail, name='user_detail'),
    url(r'^users/(?P<pk>\d+)/edit/$', views.user_edit, name='user_edit'),


]