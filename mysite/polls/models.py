import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    """
    The first spreadsheet
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    """
    The second spreadsheet
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #question is a foreignkey that connected to the Question spreadsheet
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text