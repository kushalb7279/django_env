from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

# posts = [
#    {
#       'author':'Kushal',
#       'title' : 'first post',
#       'date_posted' : '11-sept-2001',
#       'content' : 'my first post'
#    },
#    {
#        'author':'Chinmay',
#        'title' : 'second post',
#        'date_posted' : '03-oct-2001',
#        'content' : 'my second post'
#    }
# ]


# def home(request):
#     context = {
#        'posts' : Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context)    #this is dead code since using class based views

class PostListView(ListView):   #list view
    model = Post
    template_name = 'blog/home.html'  # looks for <app>/<model>_<viewtype>.html
    context_object_name = 'posts'   #context , else access by object.-- in template
    ordering = ['-date_posted']  #this is to order where recently posted is at first
    paginate_by = 3    #for pagination


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):  #modify query set to return only stuff that satisfies specific conditions
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post



class PostCreateView(LoginRequiredMixin, CreateView): #dont forget to pass proper parameters, login... used to inherit so that it asks to login before postin
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)    #after overridng, parent fun is called



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):   #UserPassesTestMixin for testing if the user updating is the user who created
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False    #forbidden page 403


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):   #UserPassesTestMixin for testing if the user updating is the user who created
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about(request):
    return render(request,'blog/about.html',{"title":"about"})
