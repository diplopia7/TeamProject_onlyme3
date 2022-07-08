from math import ceil

from django.db.models import F
from django.shortcuts import render

# Create your views here.
from member.models import Member
from pay.models import Shop


def pay(request, perPage=6):
    if request.method == 'GET':
        form = request.GET.dict()
        bds = Shop.objects.all()

        pages = ceil(bds.count() / perPage)

        cpage = 1
        if request.GET.get('cpage') is not None: cpage = form['cpage']

        start = (int(cpage) - 1) * perPage
        end = start + perPage

        bds = bds[start:end]

        stpgn = int((int(cpage) - 1) / 10) * 10 + 1

        context = {'bds': bds, 'pages': pages, 'range': range(stpgn, stpgn + 5)}
        return render(request, 'pay.html', context)

    elif request.method == 'POST':
        returnPage = ''
        form = request.POST.dict()
        print(form)

        m = Member.objects.filter(name=form['name'], jumin=form['rrn'], phone=form['phone'])

        if request.session.get('userid'):
            if m:
                m.update(cash=F('cash') + form['inlineRadioOptions'])

                returnPage = 'payok.html'

                return render(request, returnPage)
            else:
                returnPage = 'payfail.html'

                return render(request, returnPage)

        context = {'m': m}

        return render(request, returnPage, context)


def buy(request):
    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        form = request.POST.dict()

        p = Shop.objects.filter(cname=form['chrname'])
        return render(request, 'pay.html')


def payok(request):
    return render(request, 'payok.html')


