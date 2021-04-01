from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, 
        DetailView, 
        CreateView,
        UpdateView,
        DeleteView)

from .models import Post


# Create your views here.



def Home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'my_firstapp/Home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'my_firstapp/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = [ 'title', 'content' ]

    def form_valid(self, form):
        form.instance.aurthor = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.aurthor:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.aurthor:
            return True
        return False

    
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [ 'title', 'content' ]

    def form_valid(self, form):
        form.instance.aurthor = self.request.user
        return super().form_valid(form)


def About(request):
    return render( request, 'my_firstapp/About.html', {'title' : 'About'} )


