from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

def index(request):
    return render(request, "survey/index.html")

def process(request):
    request.session['data'] = request.POST
    if len(request.POST['name']) < 1:
        messages.add_message(request, messages.ERROR, "A name must be provided")
    if len(request.POST['comment']) < 1:
        messages.add_message(request, messages.ERROR, "A comment must be provided")
    if len(request.POST['comment']) > 120:
        messages.add_message(request, messages.ERROR, "A comment cannot have more than 120 characters")
    print("\n\n-------------------")
    if len(messages.get_messages(request)) > 0:
        return redirect('/')
    return redirect('/success')

def success(request):

    return render(request, "survey/result.html")
