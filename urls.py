from django.conf.urls import url

from plugins.adverts import views


urlpatterns = [
    url(r'^manager/$', views.manager, name='adverts_manager'),
]
