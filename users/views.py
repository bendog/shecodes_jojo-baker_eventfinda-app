from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
class Register(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"


class EditProfile(generic.UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("eventFinderApp:account")
    template_name = "registration/editprofile.html"

    def get_object(self, queryset=None):
        return self.request.user
