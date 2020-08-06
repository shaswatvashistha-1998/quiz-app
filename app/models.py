from __future__ import unicode_literals
from django.db import models
from django.urls import reverse

class Genre(models.Model):
    genre=models.CharField(max_length=200)

    def __str__(self):
        return self.genre

class Question(models.Model):
    """ model class question with fields for question number,question,choices and answer"""
    question_num = models.CharField(max_length = 2)
    question = models.CharField(max_length = 200)
    choice1 = models.CharField(max_length = 200)
    choice2 = models.CharField(max_length = 200)
    choice3 = models.CharField(max_length = 200)
    choice4 = models.CharField(max_length = 200)
    choice5 = models.CharField(max_length = 200)
    answer = models.CharField(max_length = 200)
    genre1=models.CharField(max_length=200)

    def __str__(self):
        return self.question
    def get_absolute_url(self): # new
        return reverse('Start')
