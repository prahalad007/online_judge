from .helper import run_code
from typing import Reversible
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Problems, Solution
from django.template import loader
from .helper import run_code
# Create your views here.


def allProblems(request):
    p_list = Problems.objects.all()
    return render(request, 'index.html', {'p_list': p_list})


def problem_details(request, problem_name):
    problem = get_object_or_404(Problems, name=problem_name)
    template = loader.get_template('details.html')
    context = {
        'problem': problem,
    }
    return HttpResponse(template.render(context, request))


def new_submission(request):
    if request.method == 'POST' and request.FILES['codefile']:
        submission_number = Solution.objects.last().id + 1
        run_code(request.FILES['codefile'])
        template = loader.get_template('onlinejudge/submitted.html')
        context = {
            'submission_number': submission_number,
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect(Reversible('problems_details'))
