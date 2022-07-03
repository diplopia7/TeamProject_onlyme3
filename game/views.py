from django.shortcuts import render


# Create your views here.
def game_info(request):
    return render(request, 'game_info.html')


def main_menu(request):
    return render(request, 'main_menu.html')


def character(request):
    global context
    returnPage = 'character.html'

    if request.method == 'GET':
        command=0
        power=0
        inteli=0
        politics=0
        innertrait='없음'
        fighttrait='없음'
        skill='없음'

    elif request.method == 'POST':
        form = request.POST.dict()
        request.session['command']=form['통솔']
        request.session['power']=form['무력']
        request.session['inteli']=form['지력']
        request.session['politics']=form['정치']

    context={'command':command,'power':power,'inteli':inteli,'politics':politics,'innertrait':innertrait,'fighttrait':fighttrait,'skill':skill}

    return render(request, returnPage,context)


def story1(request):
    return render(request, 'story1.html')


def story2(request):
    return render(request, 'story2.html')


def story3(request):
    return render(request, 'story3.html')


def 내정(request):
    return render(request, '내정.html')


def 전투(request):
    return render(request, '전투.html')


def how_to_fight(request):
    return render(request,'how_to_fight.html')