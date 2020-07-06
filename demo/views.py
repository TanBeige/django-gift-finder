from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .forms import GiftForm


def home(request):
    # Loads the HTML file base.html

    print(request.GET)

    form=GiftForm()

    return render(request, "base.html", {'form': form})




def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
