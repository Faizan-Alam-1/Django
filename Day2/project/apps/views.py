from django.shortcuts import render , redirect
from . models import Project
from .form import Project_Form


def home(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render( request ,'home.html' , context)


def index(request , pk):
    obj  = Project.objects.get(id=pk)
    projects = obj.tags.all()
    return render(request , 'apps/index.html' , {'project': obj  , 'tags' : projects})
     

  
def project_form(request):
    if request.method == 'POST':
        form = Project_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    project = Project_Form() 
    context = {'form' : project}  
    return render(request , 'apps/form.html' ,context)


def update_form(request , pk):
    project = Project.objects.get(id=pk)
    form  = Project_Form(instance=project)

    if request.method == 'POST':
        form = Project_Form(request.POST, instance= project)
        if form.is_valid():
            form.save()
            return redirect('home') 
    context = {'form' : form}  
    return render(request , 'apps/form.html' ,context)

def delete_form(request , pk):
      project = Project.objects.get(id=pk)

      if request.method == 'POST':
        project .delete()
        return redirect('home')
      context = {'Obj' : project}
      return render(request, 'apps/delete.html' , context)
    
