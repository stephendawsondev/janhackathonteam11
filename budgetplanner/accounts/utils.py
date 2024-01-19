from django.urls import reverse
# import random
from django.http import HttpResponseRedirect

# Allow Unauthenticated users


def anonymous_required(redirect_url):
    """
    Decorator for views that allows only unauthenticated users to access the view.
    Redirects authenticated users to the specified URL.
    """
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                return HttpResponseRedirect(reverse(redirect_url))
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
