from django.shortcuts import render
from django.views.generic import CreateView,DeleteView,ListView,UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from apps.persona.forms import RegistroForm
from django.contrib.auth.views import LoginView,LogoutView
from django.shortcuts import redirect




# Create your views here.
def index(request):
    return render(request,'index.html')

def buscar(request):
    return render(request,'buscador.html')
    
def oferta(request):
    return render(request,'oferta.html')
class RegistroUser(CreateView):
    model = User
    template_name = "login.html"
    form_class = RegistroForm
    success_url = reverse_lazy('index')
    
    def dispatch(self,request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)
 


class LoginUser(LoginView):
    template_name= 'login.html'


    def dispatch(self,request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)

