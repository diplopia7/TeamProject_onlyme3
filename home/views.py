from django.shortcuts import render,HttpResponse

# Create your views here.
def project(request):
    return render(request, 'project.html')