from django.shortcuts import render
from .models import *
# from django.http import HttpResponse
 
# Create your views here.

def First(request):
    return render (request, 'home.html')


def update(request):
    return render (request, 'update.html')




def create2(request):
    if request.method == 'POST':
        Name = request.POST.get('HName')
        Email = request.POST.get('HEmail')
        Age = request.POST.get('HAge')
        Adress = request.POST.get('HAdress')
        Phone = request.POST.get('HPhone')
        Date_of_birth = request.POST.get('HDate_of_birth') #
        Gender = request.POST.get('HGender')
        Religion = request.POST.get('HGeligion')
        Image = request.FILES.get('HImage')
        
        prof = profile(name=Name,email=Email,age=Age,adress=Adress,phone=Phone,date_of_birth=Date_of_birth,gender=Gender,religion=Religion,image=Image)
        prof.save()

        #print(Image,Religion,Gender,Phone,Date_of_birth,Adress,Age,Email,Name)
    return render (request, 'create2.html')
