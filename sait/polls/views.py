from django.shortcuts import render, get_object_or_404
from django.http import  HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from menu.models import Menu


def index(request):
    menus = Menu.objects.all()
    latest_question_list = Question.objects.order_by('-date_pub')[:5]
    contex = {'question_list': latest_question_list, 'menus': menus}
    return render(request, 'polls/index.html', contex)


def detail(request, question_id):
    menus = Menu.objects.all()
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question, 'menus': menus})


def vote(request, question_id):
    menus = Menu.objects.all()
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',
                      {'question': question, 'error_message': "You didn't select a choice.", 'menus': menus})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def results(request, question_id):
    menus = Menu.objects.all()
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question, 'menus': menus})
