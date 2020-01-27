from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator
from django.db.models import Q

from .forms import TagForm, PostForm
from .models import *
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = "blog/post_detail.html"
    redirect_url = "posts_list_url"


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = "blog/tag_detail.html"
    redirect_url = "tags_list_url"


class CreateTag(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = TagForm
    template = "blog/tag_create.html"
    raise_exception = True


class CreatePost(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = PostForm
    template = "blog/post_create.html"
    raise_exception = True


class UpdateTag(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    template = "blog/update_tag.html"
    form_model = TagForm
    raise_exception = True


class UpdatePost(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    template = "blog/update_post.html"
    form_model = PostForm
    raise_exception = True


class DeletePost(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    redirect_url = "posts_list_url"
    raise_exception = True


class DeleteTag(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    redirect_url = "tags_list_url"
    raise_exception = True


def posts_list(request):
    search_query = request.GET.get("search", "")
    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        posts = Post.objects.all()

    paginator = Paginator(posts, 3)
    page_number = request.GET.get("page", 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = f"?page={page.previous_page_number()}"
    else:
        prev_url = ""

    if page.has_next():
        next_url = f"?page={page.next_page_number()}"
    else:
        next_url = ""

    context = {
        "page": page,
        "next_url": next_url,
        "prev_url": prev_url,
        "is_paginated": is_paginated,
    }
    return render(request, "blog/index.html", context=context)


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, "blog/tags_list.html", context={"tags": tags})

