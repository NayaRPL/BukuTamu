from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def buku(req):
    return HttpResponse('Halaman Daftar')