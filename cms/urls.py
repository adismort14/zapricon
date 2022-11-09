from django.urls import path
from cms.views import *

app_name = "cms"

urlpatterns = [
    path("", cmsFun, name="cmsFun"),
    path("read/<int:complaint_id>", read, name="read"),
    path("create/", create, name="create"),
    path("update/<int:complaint_id>", update, name="update"),
    path("delete/<int:complaint_id>", delete, name="delete"),
]
