from django.shortcuts import render, redirect
from .models import *

# DOS英语对话
def dialogueView(request):
    courseid = int(request.GET.get('courseid', '1'))
    partid = int(request.GET.get('partid', '1'))
    add = request.GET.get('add', ' ')

    if add == 'word':
        word = request.POST.get('word')
        addword = Word(
            courseid=courseid,
            partid=partid,
            word=word,
        )
        addword.save()

    elif add == 'dialogue':
        courseid = int(request.POST.get('courseid'))
        partid = int(request.POST.get('partid'))
        index = 1
        spokesperson_id = request.POST.get('spokesperson')
        lr = request.POST.get('lr')
        content = request.POST.get('content')
        translate = request.POST.get('translate')
        action = 'add'

        dialoguepart = Dialogue(
            courseid=courseid,
            partid=partid,
            index=index,
            spokesperson_id=spokesperson_id,
            lr=lr,
            content=content,
            translate=translate,
        )
        dialoguepart.save()

    dialogue = Dialogue.objects.filter(courseid=courseid, partid=partid)
    wordlist = Word.objects.filter(courseid=courseid, partid=partid)
    num = dialogue.count()
    wordnum = wordlist.count()

    if dialogue.count() % 2 != 0:
        lr = 0
        role = 2
    else:
        lr = 1
        role = 1

    figurelist = Figure.objects.all()

    return render(request, 'dos/dialogue.html', locals())