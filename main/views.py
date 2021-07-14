from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View

from main.forms import RegistrationForm
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
    return render(request, 'main/france.html')

def indexrf(request):
    return render(request, 'main/ru.html')
def indextr(request):
    return render(request, 'main/tur.html')
def indexpl(request):
    return render(request, 'main/pol.html')
def client(request):
    return render(request, 'main/client panel.html')
def appp(request):
    return render(request,'main/app.html')

def admin(request):

    return render(request, 'main/panel.html')


def balance(request):
    return render(request,'main/panel.html')


def nft(request):
    return render(request, 'main/nft.html')


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        context = {
            'form': form,
        }
        return render(request, 'registration/index.html', context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)

        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['username']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            user = authenticate(
                username=new_user.username, password=form.cleaned_data['password']
            )
            login(request, user)
            return redirect('verif/')

        context = {
            'form': form,
        }
        return render(request, 'registration/index.html', context)


class VerifView(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'registration/verif.html', {})

    # def post(self, request, *args, **kwargs):
    #
    #         return redirect('client/')


        # return render(request, 'registration/index.html', context)
def panru(request):
    return render(request,'main/clientru.html')
def pantur(request):
    return render(request,'main/clienttr.html')
def panfr(request):
    return render(request,'main/clientfr.html')
def panpol(request):
    return render(request,'main/client pl.html')