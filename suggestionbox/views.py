from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import TemplateView, CreateView
from suggestionbox.forms import PostForm
from suggestionbox.models import Post

# Create your views here.
class DoneView(TemplateView):
    template_name = 'suggestionbox/thankyou.html'

class CreatePostView(CreateView):
    form_class = PostForm
    redirect_field_name = 'post_form.html'
    model = Post    

def post_publish(request):
    post = get_object_or_404(Post)
    print(post)
    if len(post['name']) == 0 :
        post['name'] = 'anonymous'
    post.submit()
    return redirect('thankyou') 

