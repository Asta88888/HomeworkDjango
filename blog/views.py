from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from blog.models import Post


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(publication_flag=True)


class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'preview', 'publication_flag']
    success_url = reverse_lazy('blog:post_list')


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'preview', 'publication_flag']
    success_url = reverse_lazy('blog:post_list')

    def get_success_url(self):
        return reverse('blog:post_detail', args=[self.kwargs.get('pk')])


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')