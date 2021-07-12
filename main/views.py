from django.shortcuts import render
from profiles.models import Profile


def main_view(request, *args, **kwargs):
    code = str(kwargs.get('ref_code'))
    try:
        profile = Profile.objects.get(code=code)
        request.session['ref_profile'] = profile.id
    except:
        pass
    return render(request, 'main.html', {})


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def indexen(request):
    return render(request, 'main/ru.html')
def indexfra(request):
    return render(request, 'main/france.html')
def indexpol(request):
    return render(request, 'main/pol.html')
def indextr(request):
    return render(request, 'main/tur.html')
def client(request):
    return render(request, 'main/client panel.html')


def admin(request):

    return render(request, 'main/panel.html')

def balance(request):
    return render(request,'main/panel.html')

def nft(request):
    return render(request, 'main/nft.html')
def app(request):
    return render(request, 'main/app.html')
