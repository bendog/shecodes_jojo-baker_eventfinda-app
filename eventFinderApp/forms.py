from django.forms import ModelForm, SplitDateTimeField
from .models import Event, Category, Account
from django.contrib.admin import widgets


class EventForm(ModelForm):
    start_time = SplitDateTimeField(widget=widgets.AdminSplitDateTime())
    end_time = SplitDateTimeField(widget=widgets.AdminSplitDateTime())

    class Meta:
        model = Event
        exclude = ["host"]


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ["first_name", "surname", "email"]
