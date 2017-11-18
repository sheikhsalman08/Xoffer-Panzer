from django.shortcuts import render,render_to_response
from django.template import RequestContext
from models import Post

def index(request):
	if request.method == 'POST':
		title = request.POST['title']
		post = Post(title=title)
		post.save()
	posts = Post.objects
	context = {
		"posts":posts
	}
	return render(request,"index.html",context)