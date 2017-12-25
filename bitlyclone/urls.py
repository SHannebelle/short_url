from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.liste, name='url_liste'),
    url(r'^new$', views.new, name='url_new'),
    url(r'^(?P<code>\w{6})/$', views.redirection, name='url_redirection'),

]