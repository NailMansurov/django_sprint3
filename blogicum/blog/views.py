from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.utils.timezone import now

from .models import Post, Category


def index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all()[:5]

    return render(request, 'blog/index.html', {'post_list': posts})


def post_detail(request: HttpRequest, post_id: int) -> HttpResponse:
    post = get_object_or_404(
        Post.objects.all(),
        id=post_id,
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request: HttpRequest, category_slug: str) -> HttpResponse:
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    posts = category.posts.filter(
        is_published=True,
        pub_date__lt=now()
    )
    return render(
        request,
        'blog/category.html',
        {
            'category': category,
            'post_list': posts
        }
    )
