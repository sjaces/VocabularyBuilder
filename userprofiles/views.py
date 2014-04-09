from django.shortcuts import render
from .forms import UserCreationEmailForm, EmailAuthenticationForm, AuthenticationForm
from django.views.decorators.cache import never_cache
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate



@never_cache
def signup(request):
    form = UserCreationEmailForm(request.POST or None)

    mensaje = form

    if form.is_valid():
        form.save()

    return render(request, 'signup.html', { 'form' : form , 'mensaje' : mensaje })


# @never_cache
def signin(request):
    form = EmailAuthenticationForm(request.POST or None)
    mensaje = request.POST
    mensaje = form.get_user()
    if form.is_valid():
        # login(request, user)
        # login(request, user)
        # form.login()
        login(request, form.get_user())
        mensaje = "login ok"
        request.User = form.get_user()
        # return render(request, 'signin.html', { 'form' : form , 'mensaje': "Error de logueo %s" % mensaje})
        return HttpResponseRedirect("/")
    else:
        return render(request, 'signin.html', { 'form' : form , 'mensaje': "Error de logueo %s" % mensaje})