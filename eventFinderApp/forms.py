from django.forms import ModelForm
from .models import Event, Category, Account
from django.contrib.admin import widgets


class EventForm(ModelForm):
    class Meta:
        model = Event
        exclude = ['host']
        widgets = {
            'start_time': widgets.AdminSplitDateTime,
            'end_time': widgets.AdminSplitDateTime,
        }



class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = [
            'first_name',
            'surname',
            'email'
        ]
