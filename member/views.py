from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
from member.models import Member

# 회원가입 처리 함수
def join(request):
    returnPage = 'join.html'

    if request.method == 'GET':
        return render(request, returnPage)

    elif request.method == 'POST':
        form = request.POST.dict()
        error1 = ''
        error2 = ''
        error3 = ''
        error4 = ''
        error5 = ''
        duplicate=''

        try:
            member = Member.objects.get(userid=form['userid'])
        except Member.DoesNotExist:
            member = None
        if member is not None:
            duplicate = '이미 사용하고 있는 아이디 입니다.'
        else:
            duplicate = '사용할 수 있는 아이디 입니다.'

            if not form['userid']:
                error1='아이디를 입력하세요'
            elif not form['passwd']:
                error2='비밀번호를 입력하세요'
            elif not form['name']:
                error3='이름을 입력하세요'
            elif not form['email']:
                error4 = '이메일 주소를 입력하세요'
            elif form['passwd'] != form['repasswd']:
                error5 = '비밀번호가 일치하지 않습니다!'
            else:
                member = Member(
                    userid=form['userid'],
                    passwd=make_password(form['passwd']),
                    name=form['name'],
                    email=form['email']
                )
                member.save()
                returnPage = 'joinok.html'


        context = {'form': form, 'error1': error1,'error2':error2,'error3':error3,'error4':error4,'error5':error5,
                   'duplicate':duplicate}

        return render(request, returnPage, context)

# 로그인 처리 함수
def login(request):
    returnPage = 'login.html'

    if request.method == 'GET':
        return render(request, returnPage)

    elif request.method == 'POST':
        form = request.POST.dict()

        # 유효성 검사 1/2
        error = ''
        if not (form['userid'] and form['passwd']):
            error = '아이디나 비밀번호가 입력되지 않았습니다.'
        else:
            # 입력한 아이디로 회원정보가 테이블에 있는지 여부 확인
            try:
                member = Member.objects.get(userid=form['userid'])
            except Member.DoesNotExist:
                member = None

            if member and check_password(form['passwd'], member.passwd):
                # 아이디와 비밀번호 인증을 정상적으로 마쳤다면,
                # 세션변수에 인증정보를 저장해 둠
                request.session['userid'] = form['userid']

                id = Member.objects.all().filter(userid=form['userid'])\
                    .values_list('id')[0][0]
                request.session['userid_id'] = id

                return redirect('/')    # index 페이지로 이동
            else:
                error = '아이디나 비밀번호가 틀립니다!'
        context = {'error': error}
        return render(request, returnPage, context)

# 로그인한 회원의 정보 출력 함수
def myinfo(request):
    member = {}

    # 로그인한 회원 아이디를 알아냄 - 먼저 세션변수 존재여부 확인
    if request.session.get('userid'):
        userid = request.session.get('userid')


        # 아이디를 이용해서 member테이블에서 회원정보를 알아냄
        member = Member.objects.get(userid=userid)

    context = {'member': member}
    return render(request, 'myinfo.html', context)

# 로그아웃 처리 함수
def logout(request):
    if request.session.get('userid'):
        del(request.session['userid'])

    return redirect('/')

