from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.shortcuts import render
from .models import Event, Account
from .forms import EventForm, AccountForm
from django.contrib.auth.decorators import login_required

class IndexView(generic.ListView):
    template_name = 'eventFinderApp/index.html'
    context_object_name = 'events_list'

    def get_queryset(self):
        '''Return the events.'''
        return Event.objects.all()


class EventView(generic.DetailView):
    model = Event
    template_name = 'eventFinderApp/event.html'

class AccountView(generic.DetailView):
    model = Account
    template_name = 'eventFinderApp/account.html'

def account(request):
    accountform = AccountForm()
    return render(request, 'eventFinderApp/account.html', {'accountform': accountform})

@login_required(login_url='login')
def add_event(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EventForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # get the new event from the form but don't save it yet
            new_event = form.save(commit=False)
            # add the host
            new_event.host = request.user
            # save the event
            new_event.save()
            # this is working but apparently should save the event twice, without it it doesn't save the categories
            form.save()
            # return to the index
            return HttpResponseRedirect(reverse('eventFinderApp:index'))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = EventForm()
    # return the invalid or new form to the template
    return render(request, 'eventFinderApp/add-event.html', {'eventform': form})
