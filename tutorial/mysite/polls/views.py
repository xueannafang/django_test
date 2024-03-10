from django.db.models.query import QuerySet
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import F
from django.urls import reverse
from django.views import generic

# Create your views here.
from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        return the last five published questions
        """
        return Question.objects.order_by("-pub_date")[:5]
    

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"




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
    question = get_object_or_404(Question, pk=question_id)
    # response = "You're looking at the results of question %s." 
    return render(request, "polls/results.html", {"question":question}) 

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question":question,
            "error_message":"You didn't select a choice.",
        },)
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        #return an HttpResponseRedirect after successful dealing with post data
        #to prevent data submitted twice by clicking the back button.
        return HttpResponseRedirect(reverse("polls:results", args = (question.id,)))

    return HttpResponse("You're voting on question %s." % question_id)