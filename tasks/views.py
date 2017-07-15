from django.shortcuts import render
from .models import Task, User

def task_list(request):
	tasks = Task.objects.all()
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

	return render(request, 'tasks/main.html', {'tasks': tasks}) 
	#{ 'posts': user_posts}
	# First stage. Needs refactoring. 
