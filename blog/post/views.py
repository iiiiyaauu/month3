from django.shortcuts import render
from django.http import HttpResponse
import  random
# Create your views here.

def random_number(request):
    return HttpResponse(f"Random number: {random.randint(1, 100)}")