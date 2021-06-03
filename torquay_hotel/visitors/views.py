from django.shortcuts import render, HttpResponseRedirect
from datetime import datetime
from .models import Hotel
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