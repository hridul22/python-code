from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import TodoForm
from .models import Task
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView,DeleteView


class Tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'name'

class Taskdetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task1'

class Taskupdateview(UpdateView):
    model = Task
    template_name = 'edit.html'
    context_object_name = 'task2'
    fields = ['task','priority','date']

    def get_success_url(self):

        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})


class Taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')



# Create your views here.
def index(request):
    name=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date= request.POST.get('date','')
        task=Task(task=name,priority=priority,date=date)
        task.save()
        return redirect('/')

    return render(request, 'home.html',{'name':name})


def delete(request,taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')


def update(request,id):
    task = Task.objects.get(id=id)
    f = TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        task.save()
        return redirect('/')

    return render(request,'update.html',{'f':f,'task':task})