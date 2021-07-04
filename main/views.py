from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'main/index.html')
def indexen(request):
    return render(request,'main/inen.html')
def client(request):
    return render(request,'main/client panel.html')