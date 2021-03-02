from django.shortcuts import render
from django.views.generic import CreateView,DeleteView,ListView,UpdateView
from .models import Trabajo
# Create your views here.

class Listar(ListView):
    model=Trabajo
    template_name='buscador.html'
    queryset=Trabajo.objects.all()


def index(request):
    print(request.GET)
    return render(request,'index.html')