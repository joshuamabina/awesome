import uuid
from datetime import datetime
from django.db import models

class Question(models.Model):
  unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
  question_text = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now=True)

class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
