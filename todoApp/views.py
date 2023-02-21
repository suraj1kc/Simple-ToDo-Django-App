from django.shortcuts import redirect, render
from django.views import View

from todoApp.models import Task

# Create your views here.
class home(View):
    def get(self, request):
        tasks = Task.objects.all().order_by('-created_at')
        context = {
            'tasks': tasks
        }
        return render(request, 'todoApp/home.html', context)
    
    def post(self, request):
        return render(request, 'todoApp/home.html', {})
    
    def post(self, request):
        return render(request, 'todoApp/home.html', {})
    
class addTodo(View):
    def get(self, request):
        return render(request, 'todoApp/add_todo.html')
    
    def post(self, request):
        title = request.POST.get('title')
        task = Task(title=title)
        task.save()
        
        context = {
            'task': task
        }
        return redirect('home')
    
class editTodo(View):
    def get(self, request, id):
        task = Task.objects.get(id=id)
        context = {
            'task': task
        }
        return render(request, 'todoApp/edit_todo.html', context)

    def post(self, request, id):
        task = Task.objects.get(id=id)
        task.title = request.POST.get('title')
        task.save()
        return redirect('home')

    
class deleteTodo(View):
    def get(self, request, id):
        task = Task.objects.get(id=id)
        task.delete()
        return redirect('home')

    
        