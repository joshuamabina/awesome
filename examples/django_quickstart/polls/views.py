from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Question, Choice

def index(request):
  context = { 'polls': Question.objects.all() }
  return render(request, 'polls/index.html', context)

def show(request, question_id):
  context = { 'poll': {}}
  return render(request, 'polls/show.html', context)

def store(request):
  question = request.POST['question_text']
  choices = request.POST['choices']

  # Save new question
  question = Question(question_text=question)
  question.save()

  # Save all choices for question above
  for choice in choices:
    choice = Choice(question=question, choice_text=choice)
    choice.save()

  return redirect('polls:index')

