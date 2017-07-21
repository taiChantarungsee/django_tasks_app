from .models import Task, User
from .forms import TaskForm, DeleteTaskForm
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy

def task_list(request):
	 # also need to add a gitignore and other files. Also integrate the forms demo project?
	tasks = Task.objects.all()
	#if request.user is_authenticated():
#		user_posts = Posts.objects.get('user'=request.user.username)
#		posts = { 'posts': user_posts}
	#if so there will be a database entry with all his tasks...

#	if request.method == "POST":
#		form = PostForm(request.post, )
#			if form.isvalid():
#				post = form.save(commit=False)
#				return render(request, {'form':form})

	return render(request, 'tasks/main.html', {'tasks': tasks})
	#{ 'posts': user_posts}
	# First stage. Needs refactoring. 

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

def task_delete(request, pk): 
	#This way of implementing delete is modular and keeps us safe from CSRF attacks.
	task = get_object_or_404(Task, pk=pk)
	print ("1")
	if request.method == 'POST':
		print ("2")
		form = DeleteTaskForm(request.POST, instance=new_to_delete)
		if form.is_valid():
			task.delete()
	else:
		print ("3")
		form = DeleteTaskForm(instance=task)
	print ("4")
	tasks = Task.objects.all()
	template_vars = {'tasks':tasks}
	return render(request, 'tasks/main.html', template_vars)

class TaskDelete(DeleteView):
    model = Task
    template_name = 'delete_task.html'
    success_url = reverse_lazy('main')

    def get_sucess_url(self):
    	return success_url
