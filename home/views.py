from django.shortcuts import render
from django.utils import timezone


def index(request):
    """Renders a Hello World page with the current date and time."""
    return render(request, 'index.html', {'now': timezone.now().strftime('%Y-%m-%d %H:%M:%S %Z')})
