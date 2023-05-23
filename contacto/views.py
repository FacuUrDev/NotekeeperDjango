from django.shortcuts import render,redirect
from .models import Contacto
from .forms import ContactoForm
from django.http import HttpResponse
from django.contrib import messages

def index(request):
    contactos = Contacto.objects.filter(name__contains=request.GET.get('search',''))
    context = {'contactos':contactos}
    return render(request, 'contacto/index.html',context)


def view (request ,id):
    contacto = Contacto.objects.get (id=id)
    context = {'contacto':contacto}
    return render (request,'contacto/detail.html',context)

def edit (request, id):
     contacto = Contacto.objects.get(id=id)
    
     if (request.method == 'GET'):
        form = ContactoForm(instance=contacto)
        context = {'form':form,'id':id}
                                
        
        return render (request,'contacto/edit.html',context)
    
     if (request.method == 'POST'):
        form = ContactoForm(request.POST,instance=contacto )
        if form .is_valid():
            form.save()
    
        context = {'form':form,'id':id}

        messages.success(request, 'Contacto actualizado correctamente')
        return render (request,'contacto/edit.html',context)

def create (request):
    if (request.method == 'GET'):
        form = ContactoForm()
        context = {'form':form}
        return render (request,'contacto/create.html',context)
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect ('contacto')
    
def delete (request,id):
    contacto = Contacto.objects.get(id=id)
    contacto.delete()
    return redirect ('contacto')