from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from House.models import Post
from django.shortcuts import render, get_object_or_404, redirect
from House.forms import PostForm
from accounts.models import User

 

# def houseList(request):
#     context = { 'posts': House.objects.all()}
#     # else:
#     #     houses = House.objects.filter(user=request.user)
#     return render(request, 'House/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'House/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 6

class UserPostListView(ListView):
    model = Post
    template_name = 'House/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2

    # def get_query_set(self):
    #     user = get_object_or_404(User, username =self.kwargs.get('username'))
    #     return Post.objects.filter(user= user).order_by('-date_posted')

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(user=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'description','area','location','price','image' ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'description','area','location','price', 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/house'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


def about(request):
    return render(request, 'about.html', {'title': 'About'})
