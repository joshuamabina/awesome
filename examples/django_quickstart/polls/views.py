from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Question, Choice

def index(request):
  context = { 'polls': Question.objects.all() }
  return render(request, 'polls/index.html', context)

def show(request, question_id):
  question = Question.objects.filter(pk=question_id).get()
  choices = Choice.objects.filter(question=question)

  total_votes = 0
  for choice in choices:
    total_votes += choice.votes;

  context = { 'poll': question, 'choices': choices, 'total_votes': total_votes }
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

def vote(request, question_id):
  selected_choice_id = request.POST['choice_id']

  question = Question.objects.filter(pk=question_id).get()

  selected_choice = Choice.objects.filter(question=question, pk=selected_choice_id).get()

  selected_choice.votes += 1
  selected_choice.save()

  print(selected_choice.votes)

  return redirect('polls:show', question.id)

