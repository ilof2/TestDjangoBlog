from django.urls import path
from .views import *


urlpatterns = [
    path("", posts_list, name="posts_list_url"),
    path("post/<str:slug>/", PostDetail.as_view(), name="post_detail_url"),
    path("post/<str:slug>/update", UpdatePost.as_view(), name="update_post_url"),
    path("tags/", tags_list, name="tags_list_url"),
    path("create/tag/", CreateTag.as_view(), name="create_tag_url"),
    path("create/post/", CreatePost.as_view(), name="create_post_url"),
    path("tag/<str:slug>/", TagDetail.as_view(), name="tag_detail_url"),
    path("tag/<str:slug>/update/", UpdateTag.as_view(), name="update_tag_url"),
    path("post/<str:slug>/delete", DeletePost.as_view(), name="delete_post_url"),
    path("tag/<str:slug>/delete", DeleteTag.as_view(), name="delete_tag_url"),
]