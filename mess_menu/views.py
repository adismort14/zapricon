from django.shortcuts import render

# Create your views here.


def showMenu(request):
    return render(request=request, template_name="mess/mess.html", context={})
