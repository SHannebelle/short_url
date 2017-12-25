from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.ShortUrlListAPIView.as_view(), name='url_liste'),
    url(r'^(?P<pk>[0-9]+)/$',views.ShortUrlDetailAPIView.as_view(), name='detail')
#    url(r'^new$', views.new, name='url_new'),
#    url(r'^(?P<code>\w{6})/$', views.redirection, name='url_redirection'),

]