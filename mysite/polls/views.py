from urllib import response
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question
# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    """
    위에 shortcut 함수 내용을 길게 풀어쓰면 아래처럼 작성
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exits")
    """


def results(request, question_id):
    response = "You are looking at the results of question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)
