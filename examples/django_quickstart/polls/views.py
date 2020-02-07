from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Question

def index(request):
  context = { 'polls': [] }
  return render(request, 'polls/index.html', context)

def show(request, question_id):
  context = { 'poll': {}}
  return render(request, 'polls/show.html', context)

def store(request):
  Question.create(request.POST)

  return redirect('polls:index')

