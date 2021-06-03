from django.shortcuts import render, HttpResponseRedirect,get_object_or_404
from django.urls import reverse_lazy
from datetime import datetime
from .models import Hotel, Guest, CustomerMessage
from django.views import generic
from django.contrib.auth.decorators import login_required
# from .forms import SearchData

# Create your views here.
def index(request):        
    return render(request, 'index.html')

def visitors_home(request):
    hotel = Hotel.objects.get()
    today = datetime.now()
    return render(request, 'visitors_home.html', {'hotel': hotel, 'today': today})

def vacancies(request):
    if request.method == "POST":
        form = SearchData(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()

        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = SearchData()

    return render(request, "vacancies.html", {"form": form})


class GuestCreateView(generic.CreateView):
    model = Guest
    fields = '__all__'
    template_name = 'addguest.html'
    success_url = reverse_lazy('listguests')


class GuestListView(generic.ListView):
    model = Guest
    fields = '__all__'
    template_name = 'listguests.html'
    context_object_name = 'guests'


class MessageCreateView(generic.CreateView):
    model = CustomerMessage
    fields = '__all__'
    template_name = 'addmessage.html'
    success_url = reverse_lazy('listguests')

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Guest, id = id_)

    