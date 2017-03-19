from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
# from django.views.generic import TemplateView
from university import views

# url(r'^user/', include('django.contrib.auth.urls')),


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='home'),
    url(r'^user/login/$', auth_views.login,
        {'template_name': 'login.html'}, name='login'),
    url(r'^user/logout/$', auth_views.logout, {'template_name': 'logout.html'}, name='logout'),
    url(r'^user/registration/$', auth_views.logout, {'template_name': 'studentReg.html'}, name='registration'),
    url(r'^user/login_successful$', views.login_success, name='login_success'),
    url(r'^student/upload_profile_pic', views.upload, name='register'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^about$', views.about, name='about'),
    url(r'^commons/', include('commons.urls')),
]
