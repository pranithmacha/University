from django.conf.urls import url
from commons import views as commons_views


urlpatterns = [
    url(r'^registration/$', commons_views.registration, name='registration'),
]
