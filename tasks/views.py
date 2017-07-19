from django.shortcuts import render, get_object_or_404
from .models import Task, User
from .forms import TaskForm
from django.shortcuts import redirect

def task_list(request):
	 # also need to add a gitignore and other files. Also integrate the forms demo project?
	tasks = Task.objects.all()
	print ("!!!!!!!!!!!!!!!!!!")
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
	if request.method == "POST":
		form = TaskForm(request.POST, instance=post)
		if form.is_valid():
			task = form.save(commit=False)
			task.save()
			return redirect('task_edit')
	else:
		form = TaskForm(instance=post)
	return render(request, 'edit.html', {'task': task})