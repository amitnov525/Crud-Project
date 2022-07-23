from django.shortcuts import render,HttpResponseRedirect
from main.forms import Student
from main.forms import Student1

# Create your views here.
def base(request):
    return render(request,'main/base.html')
def add(request):
    if request.method=='POST':
        fm=Student(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=Student1(name=nm,email=em,password=pw)
            reg.save()
            fm=Student()
    else:
        fm=Student()
    stud=Student1.objects.all()
    context={'form':fm,'stud':stud}
    return render(request,'main/addshow.html',context)
def delete(request,id):
    if request.method=="POST":
        pi=Student1.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/add')
def update(request,id):
    if request.method=="POST":
        pi=Student1.objects.get(pk=id)
        fm=Student(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=Student1.objects.get(pk=id)
        fm=Student(instance=pi)
    context={"fm":fm}
    return render(request,'main/update.html',context)

        
