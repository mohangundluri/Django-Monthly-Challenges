from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:month_number>',views.month_text_by_number),
    path('<str:month_name>', views.month_text_by_str, name="challege_by_str"),
]