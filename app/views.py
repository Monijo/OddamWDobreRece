from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from app.forms import CustomUserCreationForm, CustomUserChangeForm, UserLogInForm
from app.models import Donation, Institution, CustomUser, Category


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


class AddDonation(LoginRequiredMixin, View):
    login_url = reverse_lazy("app:loginPage")

    def get(self, request):
        all_categories = Category.objects.all()
        all_institutions = Institution.objects.all()
        return render(request, "app/form.html", {"categories": all_categories, "institutions": all_institutions})


class Login(View):
    def get(self, request):
        form = UserLogInForm()
        return render(request, "app/login.html", {'form': form})

    def post(self, request):
        email = request.POST.get("email")
        user = authenticate(email=email, password=request.POST.get("password"))
        if user is not None:
            login(request, user)
            return redirect("app:landingPage")
        if not CustomUser.objects.filter(email=email):
            return redirect("app:registerPage")
        else:
            form = UserLogInForm()
            return render(request, "app/login.html", {'form': form})


class Register(View):

    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, "app/register.html", {"form": form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user_reg = form.save(commit=False)
            user_reg.save()
            login(request, user_reg)
            return redirect('app:loginPage')
        return render(request, "app/register.html", {"form": form})


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect("app:landingPage")

