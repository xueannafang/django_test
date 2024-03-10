from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse

# Create your views here.
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    # output = ",".join([q.question_text for q in latest_question_list])
    # return HttpResponse(template.render(context, request))
    # render is a shortcut function that don't need loader or httpresonse
    return render(request, "polls/index.html", context)


def details(request, question_id):
    
    # can be shortcut using get_object_or_404
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question doesn't exist.")
    question = get_object_or_404(Question, pk=question_id)
    # return HttpResponse("You're looking at question %s." %question_id)
    return render(request, "polls/detail.html", {"question":question})

def results(request, question_id):
    response = "You're looking at the results of question %s." 
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)