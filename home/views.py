from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    # return HttpResponse("This is my homepage (/)")
    context = {'name': 'Rupesh','course': 'Django'}
    return render(request, 'home.html', context)


def about(request):
    # return HttpResponse("This is about myself (about)")
    return render(request, 'about.html')


def project(request):
    # return HttpResponse("This is my project (/project)")
    return render(request, 'project.html')


def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        # print(name, email, phone, desc)
        contact = Contact(name=name, email=email, phone =phone, desc=desc)
        contact.save()
        print("The data has been written to database.")
    # return HttpResponse("This is my contact (/contact)")
    return render(request, 'contact.html')

