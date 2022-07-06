from django.shortcuts import render

# Create your views here.
from member.models import Member
from pay.models import Shop


def pay(request):
    if request.method == 'GET':
        bds = Shop.objects.all()
        # if request.session.get('userid'):
        #     if
        context = {'bds': bds}
        return render(request, 'pay.html', context)
    elif request.method == 'POST':
        error=''
        form = request.POST.dict()
        print(form)

        m = Member.objects.all()
        if m['name']==form['name']:
            print('ss')

        return render(request, 'payok.html')

def payok(request):
    return render(request, 'payok.html')