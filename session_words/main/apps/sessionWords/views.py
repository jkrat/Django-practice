from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "sessionWords/index.html")

def process(request):
    showbig = 3 if 'showBig' in request.POST else 6
    word_info = {
        'word': request.POST['word'],
        'color': request.POST['color'],
        'showBig': showbig
    }
    if len(request.session.keys()) == 0:
        temp_list = []
        temp_list.append(word_info)
        request.session['words'] = temp_list
        print(request.session['words'])
    else:
        temp_list = []
        display_list = []
        sesh_data = request.session['words']
        for sesh in sesh_data:
            temp_list.append(sesh)
        temp_list.append(word_info)
        for item in temp_list:
            display_list.append(item)
        request.session['words'] = display_list
    return redirect("/")

def clear(request):
    request.session.clear()
    print(request.session)
    return redirect("/")


