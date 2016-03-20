from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse

# Create your views here.

def index(request):
    user = request.user
    context = {'user': user}
    template = 'index.html'
    return render(request, template, context)
