# Django
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

# Allow Unauthenticated users only


def anonymous_required(redirect_url):
    """
    Decorator for views that allows only unauthenticated users to access the view.
    Redirects authenticated users to the specified URL
    and provide a messagea accordingly
    """
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                messages.warning(
                    request, 'You must logout to view the Demo version!')
                return HttpResponseRedirect(reverse(redirect_url))
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
