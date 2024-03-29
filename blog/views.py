from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})


# myapp/views.py
from django.http import JsonResponse

def hello_api(request):
    return JsonResponse(
    [
        {'title': 'Hello API'},
        {'title': 'Jesus Christ!'},
        {'title': 'Bullshit!'},
        {'title': 'My name~'},
        {'title': '집에가요~'},
    ], json_dumps_params = {'ensure_ascii': True}, safe=False)