from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from finance.models import User,Moviment,Type,Wallet
from logs.models import Log
from django.db.models import QuerySet
from typing import Optional
from django.http import HttpResponse


def index(request):
    wallets:QuerySet[Wallet] = Wallet.objects.all()
    return render(request, "finance/wallet/index.html",locals())

def add_wallet(request):
    return
def edit_wallet(request,wallet_id):
    return
def delete_wallet(request, wallet_id):
    item:Optional[Wallet] = Wallet.objects.filter(pk=wallet_id).first()
    if item:
        item.delete()  
    return redirect('/finance/')  


def index_type(request):
    title:str = "Types"
    types:QuerySet[Type] = Type.objects.all()
    return render(request, "finance/type/index.html",locals())

def add_type(request):
    title:str = "Add type"
    message_form:str = ""
    if request.method == 'POST':
        name:str = request.POST.get("name","")
        operation:str = request.POST.get("operation","")
        user = User.objects.get_or_create(id=1)
        user = user[0]
        user.name= "Teste"
        user.save()
        if name and operation:
            type:Type = Type(name=name,operation=operation,user=user)
            type.save()
            Log.add(description =f"Add type of created with name:{name} - operation {operation}",app="finance",model="type",object_id=type.id,user=user.name)
            return redirect('/finance/type')  
        else:
            message_form = "ERROR! NAME OR OPERATION EMPTY!"
    return render(request, 'finance/type/add.html', locals())


def edit_type(request,type_id):
    title:str = "Edit type"
    message_form:str = ""
    type :Optional[Type] = Type.objects.filter(id=type_id).first()
    if not type:
        return redirect('/finance/type')  
    if request.method == 'POST':
        name:str = request.POST.get("name","")
        operation:str = request.POST.get("operation","")
        user = User.objects.get_or_create(id=1)
        user = user[0]
        user.name= "Teste"
        user.save()
        if name and operation:
            type.name = name
            type.operation = operation
            type.save()
            Log.add(description =f"Type of update to with name:{name} - operation {operation}",app="finance",model="type",object_id=type.id,user=user.name)
            return redirect('/finance/type')  
        else:
            message_form = "ERROR! NAME OR OPERATION EMPTY!"
    return render(request, 'finance/type/edit.html', locals())

def delete_type(request, type_id):
    item:Optional[Type] = Type.objects.filter(pk=type_id).first()
    if item:
        item.delete()  
    return redirect('/finance/type/')
  

def view_wallet(request,wallet_id):
    moviments:QuerySet[Moviment] = Moviment.objects.filter(wallet=wallet_id)
    return render(request, "finance/wallet/view_wallet.html",locals())

def add_moviment_walet(request,wallet_id):
    return

def delete_moviment_walet(request,moviment_id):
    moviment:Optional[Moviment] = Moviment.objects.filter(id=moviment_id).first()
    if moviment:
        moviment.delete()
    return HttpResponse('<script>window.history.go(-1);</script>')

def edit_moviment_walet(request, moviment_id):
    return


