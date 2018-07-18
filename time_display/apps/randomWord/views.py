from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    unique_id = get_random_string(length=32)
    context = {
        "randomword": unique_id,
    }
    if "count" in request.session:
        request.session["count"] = request.session["count"] + 1
    else:
        request.session["count"] = 1
    return render(request, "randomWord/index.html", context)


