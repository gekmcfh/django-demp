#pages/urls.py
from django.urls import path
from .views import HomePageView,AboutPageView,MainPageView

urlpatterns = [
    path ('about/',AboutPageView.as_view(),name='about'), #new
    path ('main/',MainPageView.as_view(),name='main'),
    path ('',HomePageView.as_view(),name='home'),
]