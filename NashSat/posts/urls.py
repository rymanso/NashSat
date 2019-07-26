from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # url(r'^page/(?P<id>\d+)/$', views.page, name='page')
    #path('page/<int:page>/', views.page),
]
