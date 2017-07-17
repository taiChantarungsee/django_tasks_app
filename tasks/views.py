from django.shortcuts import render, get_object_or_404
from .models import Task, User
from .forms import TaskForm
from django.shortcuts import redirect

def task_list(request):
	tasks = Task.objects.all() # also need to add a gitignore and other files. Also integrate the forms demo project?
	if request.method == "POST": # now add form validation
		task = get_object_or_404(Task, pk=pk)
		form = TaskForm(request.POST, instance=task)
		print ("Success!!!")
		if form.is_valid():
			post = form.save(commit=False)
			#post.author = request.user
			#post.published_date = timezone.now()
			post.save()
			#return redirect('post_detail', pk=post.pk)
	else:
		form = TaskForm()
	# First check is user is authenticated or not
	#if request.user is_authenticated():
#		user_posts = Posts.objects.get('user'=request.user.username)
#		posts = { 'posts': user_posts}
	#if so there will be a database entry with all his tasks...

#	if request.method == "POST":
#		form = PostForm(request.post, )
#			if form.isvalid():
#				post = form.save(commit=False)
#				return render(request, {'form':form})

	return render(request, 'tasks/main.html', {'tasks': tasks, 'form': form}) #fix this!
	#{ 'posts': user_posts}
	# First stage. Needs refactoring. 