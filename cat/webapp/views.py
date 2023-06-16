# from django.shortcuts import render
#
#
# # Create your views here.
#
# def home(request):
#     return render(request, 'home_page.html')
#
#
# def cat_actions(request):
#     return render(request, 'cat_actions.html')
from django.shortcuts import render, redirect
from .models import Cat
from django.http import HttpResponseRedirect


def home(request):
    if request.method == 'POST':
        cat_name = request.POST.get('name')
        request.session['cat'] = Cat()
        request.session['cat'].name = cat_name
        return redirect('cat_info')
    return render(request, 'home_page.html')


def cat_stats(request):
    cat = request.session.get('cat')
    if not cat:
        return HttpResponseRedirect("/")
    return render(request, 'cat_actions.html', {'cat': cat})


def interact(request):
    cat = request.session.get('cat')
    if not cat:
        return HttpResponseRedirect("/")

    action = request.POST.get('action')
    if action == 'feed':
        cat.to_feed()
    elif action == 'play':
        cat.to_play()
    elif action == 'sleep':
        cat.to_sleep()

    return redirect('cat_info')
