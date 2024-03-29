from django.shortcuts import render,redirect
from .forms import LoginForm 
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from .models import CustomUser
from .forms import CustomUserCreationForm ,UserProfileForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():

            fusername = form.cleaned_data['username']
            femail = form.cleaned_data['email']
            
            if CustomUser.objects.filter(username=fusername).exists() :
             
                messages.error(request, "Bu Kullanıcı adı zaten kullanılıyor.")
            elif CustomUser.objects.filter(email=femail).exists():
                messages.error(request, "Bu e-posta adresi zaten kullanılıyor.")

            else:
                user = form.save()
                user.profile_photo = "profile_photos/DefaultProfileIcon.png"
                user.save()
                login(request, user)
                messages.success(request, "Başarıyla kayıt oldunuz.")
                return redirect("/")

    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
            "form" : form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı")
            return render(request,"login.html",context)

        messages.success(request,"Başarıyla Giriş Yaptınız")

        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)


def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla çıkış yaptınız.")
    return redirect("index")

@login_required
def profile_edit(request):

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profiliniz başarıyla güncellendi.')
    else:
        form = UserProfileForm(instance=request.user)

    context = {
        'form': form
    }

    return render(request, "profile_edit.html", context)

def profile(request, id):
    profile_user = CustomUser.objects.get(id=id)
    print(profile_user.username)
    favorite_adverts = profile_user.favorites.all() if profile_user.id == request.user.id else None
    context = {
        'profile_user': profile_user,
        'favorite_adverts': favorite_adverts,
    }
    return render(request, "profile.html", context)



def index(request):
    return render(request,"index.html")