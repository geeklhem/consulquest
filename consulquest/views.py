# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader
from consulquest.models import Association, Question, Vote
import logging



def index(request):
    association = None
    asso_questions = []
    asso_choix = []
    if 'a' in request.GET:
        association = Association.objects.get(id=request.GET['a'])
        asso_questions = Question.objects.filter(author=association)
    all_questions = Question.objects.order_by('text')
    
    if association:
        asso_vote = Vote.objects.filter(author=association) 
  
        asso_choix = []
        pos = []

        for vote in asso_vote:
            asso_choix.append(Question.objects.get(id=vote.question.id))
            pos.append(vote.value)

        if asso_choix != []:
            ordered = sorted(zip(pos,asso_choix))
            asso_choix = zip(*ordered)[1]
        

    template = loader.get_template('consulquest/index.html')    

    context = RequestContext(request, {
        'all_questions': all_questions,
        'asso_questions': asso_questions,
        'asso_choix': asso_choix,
        'association':association,
    })
    return HttpResponse(template.render(context))
