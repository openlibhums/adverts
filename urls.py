from django.urls import re_path

from plugins.adverts import views


urlpatterns = [
    re_path(r'^manager/$', views.manager, name='adverts_manager'),
]
