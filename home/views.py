from django.shortcuts import render
from django.http import HttpResponse
from .models import Problems
# Create your views here.


def problemList(request):
    p_list = Problems.objects.all()
    return render(request, 'index.html', {'p_list': p_list})
