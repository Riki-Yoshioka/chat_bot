from django.shortcuts import render, redirect, HttpResponse
from .forms import TalkForm
from .models import Dialogue, Q_A
from datetime import datetime

import csv

# def mz():


def index(request):
    
    messages = Dialogue.objects.order_by("send_date")
    
    if request.method == "GET":
        form = TalkForm()

    elif request.method == "POST":
        form = TalkForm(request.POST)

        if form.is_valid():
            input = form.save(commit=False)
            input.send_bot = False
            input.send_date = datetime.now()
            input.save()
        
        perfect_answer = 0


        answer = Q_A.objects.filter(
            user_input = input.message
        )

        if answer:
            perfect_answer = 1
        print(perfect_answer)

        bot_answer = []
    
        for i in range(len(answer)):
            bot_answer.append("【質問】" + answer[i].user_input + "\r\n【回答】" + answer[i].bot_reply)
            Dialogue.objects.create(
                message = bot_answer[i],
                send_bot = True,
                send_date = datetime.now(),
            )

        if perfect_answer == 0:
            answer = Q_A.objects.filter(
                user_input__icontains = input.message
            )


            bot_answer = []
        
            for i in range(len(answer)):
                bot_answer.append("【質問】" + answer[i].user_input + "\r\n【回答】" + answer[i].bot_reply)
                Dialogue.objects.create(
                    message = bot_answer[i],
                    send_bot = True,
                    send_date = datetime.now(),
                )
            if answer:
                perfect_answer = 1
            else:
                Dialogue.objects.create(
                    message = "分かりません。",
                    send_bot = True,
                    send_date = datetime.now(),
                )

    context = {
        "form": form,
        "messages": messages,

    }
    return render(request, "main/index.html", context)

    # if request.method == "GET":
    #     form = TalkForm()

    # elif request.method == "POST":
    #     form = TalkForm(request.POST)
    
    
    # answer = answer_text[0].bot_reply
    # answer_text = Q_A.objects.all()  
    # dialogues = Dialogue.object.all()

    # answer_text = Dialogue.objects.filter(
    #     send_bot = True
    # )

    # messages = Dialogue.objects.filter(
    #     send_bot = False
    # )


def load(request):

    filename = 'lets_code.csv'
    with open(filename, encoding='utf8', newline='') as f:
        csvreader = csv.reader(f)

        for line in csvreader:
             Q_A.objects.create(
                user_input = line[0], 
                bot_reply = line[1],
            )
             
    return HttpResponse(request)

        # for row in csvreader:
        #     Q_A.objects.create(
        #         user_input = 
        #         bot_reply = 
        #     )

    #     content = [row for row in csvreader]
    # print(content)


    

    # with open('lets_code.csv', newline="") as f:
    #     reader = csv.reader(f)
    # for line in reader:
    #     print(line)


    # filename = 'lets_code.csv'
    # with open(filename, encoding='utf8', newline='') as f:
    #     csvreader = csv.reader(f)
    # for row in csvreader:
    #     print(row)