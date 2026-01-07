from django.urls import path
from agency import views


urlpatterns = [
    path('', views.home, name='home'),
    path('packages/', views.packages, name='packages'),
    path('destinations/', views.destinations, name='destinations'),
    path('booking/', views.booking, name='booking'),
    path('booking-success/', views.booking_success, name='booking_success'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout_view'),
    path('services/', views.services, name='services'),
    path('tariff/', views.tariff, name='tariff'),
    path('reviews/', views.reviews, name='reviews'),
    path('delete-review/<int:id>/', views.delete_review, name='delete_review'),
]
