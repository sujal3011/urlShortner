from django.urls import path
from . import views

app_name="urlShortener"
urlpatterns = [
    path('',views.home,name='home'),
    path('<str:slugs>',views.redir,name='redirect'),
]