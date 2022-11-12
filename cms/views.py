from django.shortcuts import render
from django.http import HttpResponse
from .models import MessComplaint
from django.shortcuts import redirect

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


def update(request, complaint_id):
    if complaint_id:
        post = MessComplaint.objects.filter(pk=complaint_id)
    if request.POST:
        newMessName = request.POST["mess-name"]
        newComplaint = request.POST["complaint"]
        post.update(messName=newMessName, complaint=newComplaint)
        return redirect("/cms")
    return render(
        request=request,
        template_name="cms/update.html",
        context={"post": post.get()},
    )


def delete(request, complaint_id):
    MessComplaint.objects.filter(pk=complaint_id).delete()
    return redirect("/cms")


def create(request):
    if request.POST:
        messName = request.POST["mess-name"]
        complaint = request.POST["complaint"]
        MessComplaint.objects.create(messName=messName, complaint=complaint)
        return redirect("/cms")

    return render(request=request, template_name="cms/create.html", context={})
