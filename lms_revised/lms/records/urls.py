from django.urls import path, include
from records import views

urlpatterns = [
    path('', views.record_form),
]
