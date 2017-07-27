from .models import Task, User
from .forms import TaskForm, DeleteTaskForm
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.edit import CreateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def task_list(request):
	 # also need to add a gitignore and other files. Also integrate the forms demo project?
	if request.user.id:
		user = request.user.id
		tasks = Task.objects.filter(user=user)
	else:
		tasks = Task.objects.all()
	#if request.user is_authenticated():
#		user_posts = Posts.objects.get('user'=request.user.username)
#		posts = { 'posts': user_posts}
	#if so there will be a database entry with all his tasks...)

	return render(request, 'tasks/main.html', {'tasks': tasks})
	#{ 'posts': user_posts}

def task_edit(request, pk):
	task = get_object_or_404(Task, pk=pk)
	print (request.POST.get('delete'))
	if request.method == "POST" and request.POST.get('delete'):
		task.delete()
		return redirect('main') # use a switch statement here? Google best way to deal with a situation like this using boolean logic.
	if request.method == "POST":
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			task = form.save(commit=False)
			task.save()
			return redirect('main')
	else:
		form = TaskForm(instance=task)
	return render(request, 'tasks/edit.html', {'task': task})

def task_complete (request, pk):
	completed_task = Task.objects.get(pk=pk)
	completed_task.completed = True 
	completed_task.save()
	tasks = Task.objects.all()
	return render(request, 'tasks/main.html', {'tasks': tasks})


#This way of implementing delete is modular, brief, and keeps us safe from CSRF attacks.
class DeleteTask(DeleteView):
    model = Task
    template_name = 'tasks/delete_task.html'
    success_url = reverse_lazy('main')

    def get_sucess_url(self):
    	return success_url


class AddTask(CreateView):
	form_class = TaskForm
	template_name = 'tasks/add_task.html'
	success_url = reverse_lazy('main')

	#def task_valid(self, form):
	#	task_ = Task.objects.create()
	#	form.save(for_task=task_)

class CreateUser(CreateView):
	form_class = UserCreationForm
	template_name = 'tasks/create_user.html'

	def get_success_url(self):
		return reverse('main')