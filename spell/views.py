from django.shortcuts import render
from django.http.response import HttpResponse
import random


def index(request):
    return HttpResponse(f'hello - {request}')


def randon_cube(request, qube, total):
    i = 0
    h = []
    for l in range(total):
        r = random.randint(1, qube)
        i+=r
        h.append(r)

    return HttpResponse(f'<h1>{i}</h1><tr><h1>{h}</h1>')


def test(request):
    return HttpResponse('<h1> TESTTT </h1>')


def detail(request, question_id):
    return HttpResponse(f"You're looking at question.{question_id}")


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
