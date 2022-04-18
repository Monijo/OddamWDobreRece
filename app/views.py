from django.shortcuts import render
from django.views import View

from app.models import Donation


class LandingPage(View):
    def get(self, request):
        all_donation = Donation.objects.all()
        bugs_num = 0
        supported_institutions = []
        for donation in all_donation:
            bugs_num += donation.quantity
            if donation.institution not in supported_institutions:
                supported_institutions.append(donation.institution)
        institution_numb = len(supported_institutions)

        return render(request, "app/index.html", {"bugs_num": bugs_num, "institution_numb": institution_numb})



class AddDonation(View):
    def get(self, request):
        return render(request, "app/form.html")


class Login(View):
    def get(self, request):
        return render(request, "app/login.html")


class Register(View):
    def get(self, request):
        return render(request, "app/register.html")
