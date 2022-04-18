from django.shortcuts import render
from django.views import View

from app.models import Donation, Institution


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

        all_foundations = Institution.objects.filter(type="foundation")
        all_order_organizations = Institution.objects.filter(type="order_organization")
        all_local_collections = Institution.objects.filter(type="local_collection")

        context = {
            "bugs_num": bugs_num,
            "institution_numb": institution_numb,
            "all_foundations": all_foundations,
            "all_order_organizations": all_order_organizations,
            "all_local_collection": all_local_collections
        }

        return render(request, "app/index.html", context)



class AddDonation(View):
    def get(self, request):
        return render(request, "app/form.html")


class Login(View):
    def get(self, request):
        return render(request, "app/login.html")


class Register(View):
    def get(self, request):
        return render(request, "app/register.html")
