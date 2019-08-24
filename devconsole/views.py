from django.shortcuts import render

def index(request):
    return render(request, 'devconsole/index.html', {})
# Create your views here.
