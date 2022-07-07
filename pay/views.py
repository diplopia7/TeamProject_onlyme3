from django.db.models import F, Q
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
        print(form)
        m = Member.objects.filter(name=form['name'], jumin=form['rrn'], phone=form['phone'])

        # muserid = Member.objects.filter().values('userid')
        # mname = Member.objects.filter().values('name')
        # mjumin = Member.objects.filter().values('jumin')
        # mphone = Member.objects.filter().values('phone')

        if request.session.get('userid'):
            if m:
                m.update(cash=F('cash') + form['inlineRadioOptions'])

                returnPage = 'payok.html'

                return render(request, returnPage)
            else:
                returnPage = 'payfail.html'
                return render(request, returnPage)

        context = {'m': m}

        return render(request, 'pay.html', context)


def payok(request):
    return render(request, 'payok.html')