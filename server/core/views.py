from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def index(request):
    return render(request, 'home.html',{'title':'Cleo Portal'})

class AboutView(TemplateView):
    template_name = 'about.html'