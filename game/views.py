import requests
from django.shortcuts import render


# Create your views here.

def game_info(request):
    return render(request, 'game_info.html')


def main_menu(request):
    return render(request, 'main_menu.html')


def character(request):
    returnPage = 'character.html'

    command = 0
    power = 0
    inteli = 0
    politics = 0
    innertrait = '없음'
    fighttrait = '없음'
    skill = '없음'

    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        form = request.POST.dict()
        request.session['command'] = form['command']
        request.session['power'] = form['power']
        request.session['inteli']=form['inteli']
        request.session['politics']=form['politics']
        request.session['innertrait']=form['innertrait']
        request.session['fighttrait']=form['fighttrait']
        request.session['skill']=form['skill']
        request.session['status'] = '부장'
        request.session['hp'] = 100
        print(form)
        returnPage = 'story2.html'
        return render(request, returnPage)

    context = {'command': command, 'power': power, 'inteli': inteli, 'politics': politics, 'innertrait': innertrait, 'fighttrait': fighttrait, 'skill': skill}

    return render(request, returnPage,context)


def story1(request):
    return render(request, 'story1.html')


def story2(request):
    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        form = request.POST.dict()
        if form['success'] == '대실패':
            request.session['innertrait'] = ''
            request.session['fighttrait']=''
            request.session['skill']=''
            innertrait=''
        elif form['success'] == '대성공':
            request.session['command']=int(request.session['command'])+5
            request.session['power']=int(request.session['power'])+5
            request.session['inteli']=int(request.session['inteli'])+5
            request.session['politics']=int(request.session['politics'])+5
            request.session['status']='도독'
        print(form)
    return render(request, 'story2.html')


def story3(request):
    return render(request, 'story3.html')


def 내정(request):
    return render(request, '내정.html')


def 전투(request):
    return render(request, '전투.html')


def how_to_fight(request):
    return render(request,'how_to_fight.html')