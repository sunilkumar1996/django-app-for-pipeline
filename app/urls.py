from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexPageView.as_view(), name="home"),
]
