from django.urls import path
from . import views

urlpatterns = [
    path('cookie/set', views.set_cookie, name='set_cookie'),
    path('cookie/get/<str:name>', views.get_cookie, name='get_cookie'),
    path('header/set', views.set_header, name='set_header'),
    path('header/get', views.get_header, name='get_header'), 
]
