from . import views
from django.urls import path

app_name = "chating"


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('account/', views.account, name='account'),
]