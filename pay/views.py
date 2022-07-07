from django.db.models import F, Q
from django.http import HttpResponse
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
        complete=''

        form = request.POST.dict()
        print(form)

        m = Member.objects.filter(name=form['name'], jumin=form['rrn'], phone=form['phone'])

        if request.session.get('userid'):
            if not (form['name'] and form['rrn'] and form['phone'] and form['inlineRadioOptions']):
                return HttpResponse(
                    f'''
                    <script>
                        alert('입력하신 정보가 올바르지 않습니다. 다시 확인해주세요')
                    </script>
                    '''
                )
            # if form not in Member.objects.values('name'):
            #     print(Member.objects.values('name'))
            #     print(form)
            #     return HttpResponse(
            #         f'''
            #         <script>
            #             alert('입력하신 정보가 일치하지 않습니다. 다시 확인해주세요')
            #         </script>
            #         '''
            #     )
            else :
                m.update(cash=F('cash') + form['inlineRadioOptions'])

            # m.save()

        context = {'error':error}

        return render(request, 'payok.html', context)


def payok(request):
    return render(request, 'payok.html')