from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Person

app = 'chained'
def getHtml(html):
    return app+'/'+html+'.html'

# class PersonListView(ListView):
#     model = Person
#     context_object_name = 'people'

def index(request):
    list1 = Person.objects.all()
    context = {'list1': list1}
    return render(request,getHtml('person_list') , context)

def person_changelist(request):
    list1 = Person.objects.all()
    context = {'list1': list1}
    return render(request,getHtml('person_list') , context)


# class person_list(request):
#     list1 = Person.objects.all()
#     context = {'list1': list1}
#     return render(request,getHtml('people_list') , context)

class PersonCreateView(CreateView):
    model = Person
    fields = ('name', 'birthdate', 'country', 'city')
    success_url = reverse_lazy('person_changelist')

class PersonUpdateView(UpdateView):
    model = Person
    fields = ('name', 'birthdate', 'country', 'city')
    success_url = reverse_lazy('person_changelist')