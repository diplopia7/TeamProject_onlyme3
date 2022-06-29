from django.shortcuts import render,HttpResponse

# Create your views here.
def base(content):
    return f'''
    <!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>레이아웃1</title>
    <link rel="stylesheet" href="/static/css/bs5/bootstrap.min.css">
    <link rel="stylesheet" href="/static/css/project.css">
</head>

<body>
    <div id="wrapper">
         <header>
         <h1><img src="/static/img/sword.jpg" alt="logo"></h1>
            <ul id="qmenu">
                <li><a href="/login">로그인</a></li>
                <li><a href="/">로그아웃</a></li>
                <li><a href="/join">회원가입</a></li>


            </ul>
        <nav>
        <ul id="mmenu">
            <li><a href="/">Home</a></li>
            <li><a href="/">게임소개</a></li>
            <li><a href="/pay">상점</a></li>
            <li><a href="/">회원정보</a></li>
            <li><a href="/main_menu">게임시작</a></li>
        </ul>
        </nav>
        </header>
    </div>
    <div id="main">
    {content}
    </div>
    <footer>
        <hr>
        <span>copyright &copy; 2022. Team2. All Rigjts Reserved</span>
    </footer>
</body>
</html>
    '''


def project(request):
    content='안녕하세요'
    return HttpResponse(base(content))