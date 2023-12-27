from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('hello_html/', views.show_hello),
    path('hello_html_dynamic/', views.show_hello_dynamic)
]