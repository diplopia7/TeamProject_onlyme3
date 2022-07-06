from django.db.models import F
from django.shortcuts import render

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
        form = request.POST.dict()

        m = Member.objects.filter(userid=form['name'], jumin=form['rrn'], phone=form['phone'])

        if request.session.get('userid'):
            if m:
                m.update(cash=F('cash') + form['inlineRadioOptions'])

        context = {'m': m}

        return render(request, 'payok.html', context)


def payok(request):
    return render(request, 'payok.html')