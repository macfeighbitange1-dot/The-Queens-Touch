from django.urls import path
from . import views

urlpatterns = [
    # The main website page
    path('', views.home, name='home'),

    # The tracking gateway for WhatsApp bookings
    path('book-now/', views.track_whatsapp, name='track_whatsapp'),
]