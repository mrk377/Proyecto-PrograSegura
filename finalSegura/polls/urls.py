from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.feed, name='feed'),
    path('registro/', views.registro, name='registro'),
    path('login/', LoginView.as_view(template_name='polls/login.html'), name='login'),
    path('token/',views.token,name='token'),
    path('Ingresar/', views.ingresar, name='ingresar'),
    path('credenciales/', views.credenciales, name='credenciales'),
    path('registrar_credencial', views.registrar_credencial, name='registrar_credencial'),
    path('listar', views.credenciales_list, name='credenciales_list'),
    path('logout', views.logout, name='logout'),
    path('registro/info.html', views.info, name='info'),
    ]