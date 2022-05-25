from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
import random
from .models import Math

# Create your views here.


def math(request):

    # initialize variables
    x = random.randint(0, 10)
    y = random.randint(0, 10)

    if not request.session.session_key:
        request.session.create()

    if Math.objects.filter(session_key=request.session.session_key).exists():
        mathe = Math.objects.get(session_key=request.session.session_key)
        mathe.x = x
        mathe.y = y
        mathe.rounds += 1
        mathe.save()
    else:
        mathe = Math.objects.create(x=x, y=y, points=0, rounds=0, session_key=request.session.session_key)

    context = {
        'math': mathe,
    }
    return render(request, 'math.html', context)


def operation(request):
    math = Math.objects.latest('id')
    user_answer = request.POST.get('answer', False)

    if int(user_answer) != int(math.x) * int(math.y):
        math.points -= 1
        math.save()
    else:
        math.points += 1
        math.save()

    return redirect('math')



