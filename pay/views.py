from django.db.models import F
from django.shortcuts import render, redirect

# Create your views here.
from member.models import Member
from pay.models import Shop


def pay(request):
    if request.method == 'GET':
        bds = Shop.objects.all()

        context = {'bds': bds}
        return render(request, 'pay.html', context)

    elif request.method == 'POST':
        error = ''
        returnPage = ''
        form = request.POST.dict()

        m = Member.objects.filter(name=form['name'], jumin=form['rrn'], phone=form['phone'])

        if request.session.get('userid'):
            if m:
                m.update(cash=F('cash') + form['inlineRadioOptions'])

                returnPage = 'payok.html'

                return render(request, returnPage)

            else:
                error = '잘못된 정보를 입력하셨습니다'
                print(error)

        context = {'m': m}

        return render(request, 'pay.html', context)


def payok(request):
    return render(request, 'payok.html')