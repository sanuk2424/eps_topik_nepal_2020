from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from verb.models import Verb


def index(request):
    if request.session.has_key('username'):
        verbs = Verb.objects.all().order_by('id')
        return render(request, 'verb/index.html', {'title': 'Verb', 'verbs': verbs})
    else:
        return redirect('/login')


def verb_detail(request, myid):
    if request.session.has_key('username'):
        verb = Verb.objects.filter(id=myid)
        content_lists = verb[0].content.split('\n')
        n = len(content_lists)
        if n % 2 == 0:
            di = int(n / 2)
        else:
            di = (int(n // 2) + 1)

        first_slice = "0:%d" % (di)
        second_slice = "%d:%d" % (di, n+1)
        second_index = di+1

        return render(request, 'verb/verb_detail.html',
                      {'verb': verb[0], 'content_lists': content_lists, 'first': first_slice, 'second': second_slice,'index':second_index})
    else:
        return redirect('/login')
