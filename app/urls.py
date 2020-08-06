from django.conf.urls import url
from . import views

app_name='app'
urlpatterns = [
    url('result/',views.result,name='result'),
    url('create/',views.createquestion.as_view(),name='create'),
    url('', views.q_list, name='list'),
]
