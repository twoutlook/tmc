from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import render

from django.urls import reverse_lazy
from .models import City
from .models import Person
from .forms import PersonForm

def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'hr/city_dropdown_list_options.html', {'cities': cities})
class PersonListView(ListView):
    model = Person
    context_object_name = 'people'

class PersonCreateView(CreateView):
    model = Person
    # fields = ('name', 'birthdate', 'country', 'city')
    form_class = PersonForm
    success_url = reverse_lazy('person_changelist')

class PersonUpdateView(UpdateView):
    model = Person
    # fields = ('name', 'birthdate', 'country', 'city')
    form_class = PersonForm
    success_url = reverse_lazy('person_changelist')