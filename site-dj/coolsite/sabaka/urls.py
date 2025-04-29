from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contact, name='contact'),
    path('how-to-find/', views.how_to_find, name='how_to_find'),
    path('categories/', views.categories, name='categories'),
    path('all-products/', views.all_products, name='all_products'),
    path('cart/', views.cart, name='cart'),
]