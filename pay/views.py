from math import ceil

from django.db.models import F
from django.shortcuts import render, redirect

# Create your views here.
from member.models import Member
from pay.models import Shop, Possession


def pay(request, perPage=6):
    if request.method == 'GET':
        form = request.GET.dict()
        bds = Shop.objects.all()
        qry = ''
        # p = Possession.objects.all().values('userid_id')
        # p = Possession.objects.select_related().filter(userid_id=request.session['userid_id']).values('cname_id')
        # p1 = Possession.objects.filter(userid_id=request.session['userid_id']).values('cname_id')
        pa = Possession.objects.select_related().filter(userid_id=request.session['userid_id'])

        pages = ceil(bds.count() / perPage)

        cpage = 1
        if request.GET.get('cpage') is not None:
            cpage = form['cpage']

        start = (int(cpage) - 1) * perPage
        end = start + perPage

        bds = bds[start:end]

        stpgn = int((int(cpage) - 1) / 10) * 10 + 1

        context = {'bds': bds, 'pages': pages, 'range': range(stpgn, stpgn + 5), 'qry': qry, 'pa':pa,}
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
        # p = Possession.objects.all()
        # context={'p':p}
        # return (request, 'pay.html', context)
        pass
    elif request.method == 'POST':
        form = request.POST.dict()

        possession = Possession(
            cname_id=form['chrname'],
            userid_id=form['idnum'],
        )
        possession.save()

        qry = '/pay/?cpage=' + form['cpage']
        #
        # context={'qry':qry}

        return redirect(qry)


def payok(request):
    return render(request, 'payok.html')


def userpos(request, perPage=6):
    form = request.GET.dict()
    bds = Possession.objects.filter(userid_id=request.session['userid_id'])
    qry = ''

    pages = ceil(bds.count() / perPage)

    cpage = 1
    if request.GET.get('cpage') is not None: cpage = form['cpage']

    start = (int(cpage) - 1) * perPage
    end = start + perPage

    bds = bds[start:end]

    stpgn = int((int(cpage) - 1) / 10) * 10 + 1
    context = {'bds': bds, 'pages': pages, 'range': range(stpgn, stpgn + 5), 'qry': qry}
    return render(request, 'pay.html', context)
