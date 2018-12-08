from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from core.models import Account
from core.forms import AccountForm


@login_required
def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'base.html')


@login_required
def account_list(request):
    accounts = Account.objects.all()
    return render(request, 'account_list.html', {'accounts': accounts})


@login_required
def account_edit(request, account_id=None):
    if account_id:
        account = Account.objects.get(id=account_id)
        if account.created_by != request.user:
            return HttpResponse(status=403)
        if request.POST:
            form = AccountForm(request.POST or None, instance=account)
            if form.is_valid():
                form.save()
        else:
            form = AccountForm(instance=account)
    else:
        if request.POST:
            form = AccountForm(request.POST or None)
            if form.is_valid():
                account_obj = form.save(commit=False)
                account_obj.created_by = request.user
                account_obj.save()
                return redirect('account_edit', account_obj.id)
        else:
            form = AccountForm()
    return render(request, 'account_edit.html', {'form': form})


@login_required
def account_delete(request, account_id):
    account = Account.objects.get(id=account_id)
    if account.created_by != request.user:
        return HttpResponse(status=403)
    account.delete()
    return redirect('account_list')
