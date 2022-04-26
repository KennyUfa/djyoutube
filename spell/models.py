import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class SpellBook(models.Model):
    name_spell = models.CharField(max_length=30)
    lvl = models.IntegerField(default=0, max_length=2)
    school = models.CharField(max_length=20)
    cast_time = models.CharField(max_length=20)
    time_spell = models.CharField(max_length=40)
    components = models.CharField(max_length=50)
    class_user = models.CharField(max_length=30)
    text = models.TextField()

    def __str__(self):
        return self.name_spell


class PersonList(models.Model):
    name_person = models.CharField(max_length=30)

    def __str__(self):
        return self.name_person
