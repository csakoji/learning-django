from django.core.exceptions import PermissionDenied
from .models import Post


def user_must_be_creator(function):
    def wrapper(request, *args, **kwargs):
        current_user = Post.objects.get(pk=kwargs['post_id'])
        if not current_user.author == request.user:
            raise PermissionDenied("You dont have required permissions.")
    return wrapper
