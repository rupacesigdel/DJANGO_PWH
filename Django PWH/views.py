from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This is the data creat by rupesh.")

def paths(request):
    # Display paths of all the blogposts inside the django website
    # fetch all the slugs from the blog post table
    context = {
        'heading': "django tutorial 1",
        'content': "this is the best django tutorial on this entire panet"
    }


    return HttpResponse("This is the another data from paths crate by rupesh.")
    


