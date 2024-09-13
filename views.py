import views 
from django.http import HttpResponse 
def AboutUs(request): 
 return HttpResponse("Welcome to EDGE Project")
def ContactUs(request): 
 return HttpResponse("<h1>Md. Mosarraf Hossain, \nMobile: 01700709716\nEmail: hossain55@gmail.com </h1>")

def ContactDetails(request, ContactId): 
 return HttpResponse(ContactId) 
from django.shortcuts import render 
def HomePage(request): 
 return render(request, "index.html") 
data={ 
'title':'Title: Home Page', 
'caption':'Welcome to EDGE Project' 
} 