from django.shortcuts import render
from .models import *

# Create your views here.
def main_views(request):
    context = {}
    image = Images.objects.get(id=1)
    context['image'] = image
    
    return render(request, 'app1/index.html', context)