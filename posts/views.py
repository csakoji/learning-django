from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class ViewAllPosts(ListView):
    model = Post
    template_name = 'home.html'


class ViewPostDetails(DetailView):
    model = Post
    template_name = 'posts/post_details.html'


class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ('title', 'description')
    template_name = 'posts/update_post.html'

    def test_func(self):
        current_user = self.get_object()
        return current_user == self.request.user


class DeletePost(DeleteView):
    model = Post
    template_name = 'posts/delete_post.html'
    success_url = reverse_lazy('home')


class CreatePost(CreateView):
    model = Post
    fields = ('title', 'description')
    template_name = 'posts/create_post.html'

    # Set user to current user
    def form_valid(self, form):
        # This approach is cant be used as it needs pk or slug in URL
        # and new post does not have pk util created.
        # current_user = self.get_object()
        # form.instance.author = current_user
        form.instance.author = self.request.user
        return super().form_valid(form)
