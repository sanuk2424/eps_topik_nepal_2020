from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import FileResponse, Http404
# https://www.eps.go.kr/exam/sub_01.zip download eps topik book
# Create your views here.
from book.models import Book, AudioMp3File


def index(request):
    if request.session.has_key('username'):
        books = Book.objects.all().order_by('id')

        return render(request, 'book/index.html', {'title': 'Book', 'books': books})
    else:
        return redirect('/login')


def book_detail(request, myid):
    if request.session.has_key('username'):
        book = Book.objects.filter(id=myid)
        audio = AudioMp3File.objects.filter(book_chapter_id=myid)
        content_lists = book[0].content.split('\n')
        n = len(content_lists)
        if n % 2 == 0:
            di = int(n / 2)
        else:
            di = int((n / 2) + 1)

        first_slice = "0:%d" % (di)
        second_slice = "%d:%d" % (di, n + 1)
        second_index = di + 1
        if book[0].pdf_file != "":
            file_name = str(book[0].pdf_file).split('/')[2][:-4]
        else:
            file_name = "default"

        return render(request, 'book/book_detail.html',
                      {'book': book[0],
                       'file_name': file_name,
                       'content_lists': content_lists,
                       'first': first_slice,
                       'audio': audio,
                       'second': second_slice,
                       'index': second_index
                       })
    else:
        return redirect('/login')


def pdf_view(request, file):
    with open('media/book/pdf/' + file + '.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'filename=reading1.pdf'
        return response


