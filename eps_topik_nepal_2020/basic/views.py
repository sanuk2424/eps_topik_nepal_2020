from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from basic.models import Basic


def index(request):
    if request.session.has_key('username'):
        basics = Basic.objects.all().order_by('id')
        counter = 1;



        return render(request, 'basic/index.html', {'title': 'Basic', 'basics': basics,'counter':counter})
    else:
        return redirect('/login')


def basic_detail(request, myid):
    if request.session.has_key('username'):
        basic = Basic.objects.filter(id=myid)
        string_nep = ''' ग्/ख्/क् न् द्
        र्/ल् म् व् स् अ/ङ ज् छ् ख् थ् फ् ह्'''

        double_vowel = ['ㅐ','ㅒ','ㅔ','ㅖ','ㅘ','ㅚ','ㅙ','ㅝ','ㅟ','ㅞ','ㅢ']
        single_vowel = ['ㅏ','ㅑ','ㅓ','ㅕ','ㅣ','ㅗ','ㅛ','ㅜ','ㅠ','ㅡ']
        consonant = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ','ㄲ','ㄸ','ㅃ','ㅆ','ㅉ']
        single_consonant_meaning = ','.join(string_nep)

        return render(request, 'basic/basic_detail.html', {'basic': basic[0],
                                                           'bid':basic[0].id,
                                                           'sc':consonant,
                                                           'sv':single_vowel,
                                                           'dv':double_vowel

                                                           })
        # content_lists = basic[0].content.split('\n')
        # n = len(content_lists)
        # di = int(n / 2)
        # first_slice = "0:%d" % di
        # second_slice = "%d:%d" % (di + 1, n)

        # return render(request, 'basic/basic_detail.html', {'basic': basic[0], 'content_lists': content_lists, 'first':first_slice,'second':second_slice})
    else:
        return redirect('/login')