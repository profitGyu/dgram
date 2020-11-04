from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'posts/index.html')


def post_create(request):
    if request.method == 'GET':
        return render(request, 'posts/post_create.html')
    elif request.method == 'POST':
        pass