import logging

from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

from blog.models import Post
from blog.forms import CommentForm


logger = logging.getLogger(__name__)


# Create your views here.

@cache_page(300)
@vary_on_cookie
def index(request):
    try:
        posts = Post.objects.filter(
            published_at__lte=timezone.now()
        ).select_related("author")

        logger.debug("Got %d posts", len(posts))

        return render(
            request,
            "blog/index.html",
            {"posts": posts},
        )

    except Exception as e:
        logger.exception("Error loading index page: %s", e)

        return render(
            request,
            "blog/index.html",
            {"posts": []},
        )


def grid(request):
    try:
        return render(
            request,
            "blog/grid.html"
        )

    except Exception as e:
        logger.exception(
            "Error loading grid page: %s",
            e,
        )

        return render(
            request,
            "blog/grid.html",
            {},
        )


def post_detail(request, slug):
    try:
        post = get_object_or_404(
            Post,
            slug=slug
        )

        if request.user.is_active:

            if request.method == "POST":
                comment_form = CommentForm(request.POST)

                if comment_form.is_valid():
                    try:
                        comment = comment_form.save(
                            commit=False
                        )

                        comment.content_object = post
                        comment.creator = request.user
                        comment.save()

                        logger.info(
                            "Created comment on Post %d for user %s",
                            post.pk,
                            request.user,
                        )

                        return redirect(
                            request.path_info
                        )

                    except Exception as e:
                        logger.exception(
                            "Error saving comment for post %d: %s",
                            post.pk,
                            e,
                        )

            else:
                comment_form = CommentForm()

        else:
            comment_form = None

        return render(
            request,
            "blog/post-detail.html",
            {
                "post": post,
                "comment_form": comment_form,
            },
        )

    except Exception as e:
        logger.exception(
            "Error loading post detail for slug %s: %s",
            slug,
            e,
        )

        return render(
            request,
            "blog/post-detail.html",
            {
                "post": None,
                "comment_form": None,
            },
        )


def get_ip(request):
    """
    Returns the client's IP address.
    Used to determine the value for INTERNAL_IPS
    when configuring Django Debug Toolbar.
    """
    return HttpResponse(
        request.META["REMOTE_ADDR"]
    )