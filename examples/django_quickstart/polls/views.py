from django.shortcuts import redirect, render
from django.http import HttpResponse

def index(request):
    context = { 'polls': [] }
    return render(request, 'polls/index.html', context)

def show(request, question_id):
    context = { 'poll': {}}
    return render(request, 'polls/show.html', context)

def store(request):
    return redirect('polls:index')

