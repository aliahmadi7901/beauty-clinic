from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from blog.forms import BlogCommentsForm
from blog.models import Blog, BlogCategory, BlogComment


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'
    paginate_by = 3

    def get_queryset(self):
        queryset = Blog.objects.all()
        search = self.request.GET.get('search', None)
        if search:
            queryset = queryset.filter(title__icontains=search, active=True)
            return queryset

        category_title = self.kwargs.get('title', None)
        if category_title:
            queryset = queryset.filter(category__title__iexact=category_title, active=True)
            return queryset

        queryset = queryset.filter(active=True)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories'] = BlogCategory.objects.all()
        context['blogs_current'] = Blog.objects.filter(active=True).order_by('-id')[:3]
        return context


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories'] = BlogCategory.objects.all()
        context['blogs_current'] = Blog.objects.filter(active=True).order_by('-id')[:3]
        context['blog_comment_form'] = BlogCommentsForm()
        context['blog_comments'] = BlogComment.objects.filter(
            blog=self.object, parent=None, is_active=True).prefetch_related('childes')
        return context

    def post(self, request, *args, **kwargs):
        comment_form = BlogCommentsForm(request.POST)
        if comment_form.is_valid():
            blog = Blog.objects.get(pk=self.kwargs['pk'])
            parent_id = request.POST.get('parent', None)
            comment = comment_form.save(commit=False)
            comment.user = self.request.user
            comment.blog = blog
            if parent_id is not None:
                parent = BlogComment.objects.get(pk=parent_id)
                comment.parent = parent
            comment.save()
            return redirect('blog_detail', pk=blog.id)
        else:
            return Http404()
