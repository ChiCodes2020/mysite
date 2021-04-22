from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# view using loader()
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

# view using render()
# def index(request):
#     return render(request, 'index.html')