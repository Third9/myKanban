from django.conf.urls import url
import views
from views import ListView, CardView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', ListView.as_view(), name='list'),
    url(r'^card/$', CardView.as_view(), name='card'),
]
