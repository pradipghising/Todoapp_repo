from django.shortcuts import render,redirect,HttpResponse
from todoapp import models
# Create your views here.
def fortask(request):
    if request.method=="POST":
        intask=request.POST['task']

        obj=models.todomodel.objects.create(
            task=intask,
        )
        obj.save()
        return redirect('index')
    return render(request,'index.html')

def forlist(request):
    alltask=models.todomodel.objects.all()
    return render(request,'list.html',{'alltask':alltask})


def fordelete(request,key):
    obj=models.todomodel.objects.get(id=key)
    
    obj.delete()
    return redirect('list')
