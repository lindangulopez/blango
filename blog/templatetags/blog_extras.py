from django import template
from django.contrib.auth.models import User
from django.utils.html import format_html

register = template.Library()


@register.filter
def author_details(author):
    if not isinstance(author, User):
        return ""

    if author.first_name and author.last_name:
        return f"{author.first_name} {author.last_name}"

    return author.username