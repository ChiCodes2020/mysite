from django.http import HttpResponse
from django.shortcuts import render
from app.models import Teacher

def listing(request):
    data = {
        "teachers": Teacher.objects.all(),
    }

    # here we're passing the data to our template 
    # we can use tags in our template to display our data
    return render(request, "index.html", data)
