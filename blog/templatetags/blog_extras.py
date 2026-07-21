import logging

from django import template
from django.contrib.auth.models import User

from blog.models import Post


register = template.Library()

logger = logging.getLogger(__name__)


@register.filter
def author_details(author):
    if not isinstance(author, User):
        return ""

    if author.first_name and author.last_name:
        return f"{author.first_name} {author.last_name}"

    return author.username


@register.inclusion_tag("blog/recent_posts.html")
def recent_posts(post=None):
    """
    Displays recent posts excluding the current post.
    Handles cases where no post object is available.
    """

    if post is None:
        logger.warning(
            "recent_posts called without a post object"
        )

        posts = Post.objects.order_by("-published_at")[:5]

        return {
            "posts": posts
        }

    posts = (
        Post.objects
        .exclude(pk=post.pk)
        .order_by("-published_at")[:5]
    )

    logger.debug(
        "Loaded %d recent posts for post %d",
        len(posts),
        post.pk,
    )

    return {
        "posts": posts
    }