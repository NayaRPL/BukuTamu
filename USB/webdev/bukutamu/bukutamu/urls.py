
from django.contrib import admin
from django.urls import path
from registrasi.views import buku
# from django.http import HttpResponse
#from django.shortcuts import render


# def daftar(req):
#     return render(req,'index.html')

urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('buku/',buku)
]
