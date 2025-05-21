from django.http import HttpResponseForbidden
from functools import wraps
from .models import RoleUser

def roles_required(*role_names):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                if RoleUser.objects.filter(user=request.user, role__name__in=role_names).exists():
                    return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("⛔ Vous n'avez pas les permissions nécessaires.")
        return _wrapped_view
    return decorator
