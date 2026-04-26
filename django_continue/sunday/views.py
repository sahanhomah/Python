from django.shortcuts import render
import datetime

# Create your views here.
def sunday(request):
    day = datetime.datetime.now().weekday()
    return render(request, "sunday.html", {"sunday": day == 6})


def hello_world(request):
    # Backward-compatible alias for older URL patterns.
    return sunday(request)

    #datetime.now().weekday()
