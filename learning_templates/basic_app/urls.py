from django.conf.urls import url
from . import views

#template tegging
app_name = 'basic_app'

urlpatterns = [
    url(r'^relative',views.relative, name='relative'),
    url(r'^other', views.other, name='other'),
]
