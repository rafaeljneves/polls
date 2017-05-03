# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from django.views.decorators.csrf import ensure_csrf_cookie
from django.template.response import TemplateResponse

from polls.models import Poll, Choice
from time import gmtime, strftime



def index(request):
    poll_list = Poll.objects.order_by('data_publicacao')

    return render_to_response('index.html', {'poll_list': poll_list})

@ensure_csrf_cookie
def details(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    c={}
    c.update(csrf(request))

    return TemplateResponse(request, 'details.html', {'poll_id': poll,
                                                   'c':c})

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    # return render_to_response('results.html', {'poll_id':poll})
    return render(request, 'results.html', {'poll_id':poll})


def vote(request, poll_id):
    p =get_object_or_404(Poll, pk=poll_id)
    c={}
    c.update(csrf(request))
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #exibe novamente o formulario  details
        return render(request, 'details', {'poll_id':p,
                                                'error_message': "favor selecione uma opcao.",
                                               })
    else:
        selected_choice.votos +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(p.id,)))
        # return render(request, 'results.html', {'c':c})


def hora_certa(request):
    data_hora = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    html = "<html><body>Hora Certa: %s</body></html>" % data_hora
    return HttpResponse(html)
