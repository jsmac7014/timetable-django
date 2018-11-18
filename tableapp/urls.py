from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^make', views.make, name='make'),
    url(r'^delete/(?P<day>[ㄱ-ㅣ가-힣]*)/(?P<id>\d+)/$', views.delete, name='delete'),
    url(r'^table/(?P<day>[ㄱ-ㅣ가-힣]*)/$', views.table, name='index'),

    url(r'^signup', views.signup, name='signup'),
    url(r'^login', auth_views.LoginView.as_view(template_name='tableapp/login.html',redirect_authenticated_user=True), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view
         (template_name='tableapp/login.html'), name='logout')
]

