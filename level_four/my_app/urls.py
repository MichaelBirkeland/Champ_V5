from django.conf.urls import url
from my_app import views


app_name = 'my_app'

urlpatterns = [
    url('other/', views.other, name='other'),
    url('base/', views.base, name='base'),


]

