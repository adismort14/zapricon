from django.shortcuts import render
from django.http import HttpResponse
from .models import MessComplaint

# Create your views here.


def cmsFun(request):
    data = MessComplaint.objects.all()
    return render(
        request=request, template_name="cms/cms.html", context={"data": data}
    )  # context should be a dictionary rather than a list


def read(request, complaint_id):
    if complaint_id:
        complaint_post = MessComplaint.objects.filter(pk=complaint_id)
        return render(
            request=request,
            template_name="cms/read.html",
            context={"complaint_post": complaint_post.get()},
        )


def update(request):
    return HttpResponse("Hello update")


def delete(request):
    return HttpResponse("Hello delete")


def create(request):
    return HttpResponse("Hello create")
