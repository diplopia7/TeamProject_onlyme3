from django.shortcuts import render

# Create your views here.


def pay(request):
    return render(request, 'pay.html')


def payok(request):
    return render(request, 'payok.html')