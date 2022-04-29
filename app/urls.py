from django.urls import path

from . import views
from .views import LandingPage, AddDonation, Login, Register, Logout, Confirmation

app_name = 'app'

urlpatterns = [
    path('', LandingPage.as_view(), name='landingPage'),
    path('addDonation/', AddDonation.as_view(), name='addDonation'),
    path('addDonation/confirmation/', Confirmation.as_view(), name='confirmation'),
    path('signIn/', Login.as_view(), name='loginPage'),
    path('signUp/', Register.as_view(), name='registerPage'),
    path('logout/', Logout.as_view(), name='logout'),
]