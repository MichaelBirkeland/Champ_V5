from django.shortcuts import render

# Create your views here.

def index(request):
    context_dict = {"text":"hello world", "numbers": 100}
    return render(request, 'my_app/index.html', context_dict)

def base(request):
    return render(request, 'my_app/base.html')

def other(request):
    return render(request, 'my_app/other.html')
