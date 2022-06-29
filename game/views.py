from django.shortcuts import render


# Create your views here.
def game_info(request):
    return render(request, 'game_info.html')


def main_menu(request):
    return render(request, 'main_menu.html')


def character(request):
    return render(request, 'character.html')


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
