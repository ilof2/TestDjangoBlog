from django.shortcuts import redirect


def index(request):
    return redirect("posts_list_url", permanent=True)