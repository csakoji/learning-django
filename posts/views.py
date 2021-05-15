from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy


class ViewAllPosts(ListView):
    model = Post
    template_name = 'home.html'


class ViewPostDetails(DetailView):
    model = Post
    template_name = 'posts/post_details.html'


class UpdatePost(UpdateView):
    model = Post
    fields = "__all__"
    template_name = 'posts/update_post.html'


class DeletePost(DeleteView):
    model = Post
    template_name = 'posts/delete_post.html'
    success_url = reverse_lazy('home')


