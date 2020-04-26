from django.http import HttpResponse
from django.shortcuts import render, redirect
from reportlab.pdfgen import canvas
from django.http import HttpResponse

# Create your views here.
from word.models import Word


def index(request):
    if request.session.has_key('username'):
        words = Word.objects.all().order_by('id')

        return render(request, 'word/index.html', {'title': 'Word', 'words': words})
    else:
        return redirect('/login')


def getpdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'
    p = canvas.Canvas(response)
    p.setFont("Times-Roman", 20)

    p.drawString(100, 700, "Hello World")
    p.showPage()
    p.save()
    return response


def word_detail(request, myid):
    if request.session.has_key('username'):
        word = Word.objects.filter(id=myid)
        content_lists = word[0].content.split('\n')
        n = len(content_lists)
        if n % 2 == 0:
            di = int(n / 2)
        else:
            di = (int(n // 2) + 1)
        first_slice = "0:%d" % (di)
        second_slice = "%d:%d" % (di, n + 1)
        second_index = di + 1

        return render(request, 'word/word_detail.html',
                      {'word': word[0], 'content_lists': content_lists, 'first': first_slice, 'second': second_slice,
                       'index': second_index})
    else:
        return redirect('/login')
