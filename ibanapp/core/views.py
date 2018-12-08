from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from core.models import Account

@login_required
def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'base.html')

@login_required
def account_list(request):
    accounts = Account.objects.all()
    return render(request, 'account_list.html', {'accounts': accounts})
