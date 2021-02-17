from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('news/', views.news, name='news'),
    path('news/<int:id>', views.newspage),
    path('contact/', views.contact),
    path('metal/', views.metal),
    path('windlass/', views.windlass),
    path('ejector/', views.ejector),
    path('product/<int:id>', views.productpage),
    path('search/', views.search, name='search')
    ]