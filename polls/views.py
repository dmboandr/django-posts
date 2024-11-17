# для специальных быстрых дейсвтий
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect  # мы подключаем HttpResponse
from django.urls import reverse

# импортируем таблицу
from .models import Question, Choice

# импортировать обработчик шаблонов django
from django.template import loader

# Create your views here.


# 127. .../polls/
def index(request):
    my_var = "это какой-то текст"
    latest_question_list = Question.objects.order_by("-pub_date")[:4]
    #output = "----".join([q.question_text for q in latest_question_list])
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
        "my_var": my_var,
    }
    return HttpResponse(template.render(context, request))


# 127. .../polls/details
def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    template = loader.get_template("polls/detail.html")
    context = {
        "question": question,
    }
    return HttpResponse(template.render(context, request))


# 127. .../polls/results
def results(request, question_id):

    response = "Ваш голос сделан"
    return HttpResponse(response)


# 127. .../polls/vote
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html",
                      {"question": question, "error_message": "You didn't Select!!!"})
    else:
        selected_choice.votes += 1
        selected_choice.save()

    return HttpResponseRedirect(reverse("results", args=(question_id,)))

# for question in Question.objects:
#     print(question.question_text)

# http://127.0.0.1:8000/polls/
#templates