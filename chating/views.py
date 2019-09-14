from django.shortcuts import render, redirect
from chating.forms import RegistrationForm


def index(request):
    return render(request, 'chating/index.html', {'val': 'hello index page'})


def account(request):
    return render(request, 'chating/account.html', {'account': 'Account page'})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chating:account')
    else:
        form = RegistrationForm()
        return render(request, 'chating/reg_form.html', {'form': form})


