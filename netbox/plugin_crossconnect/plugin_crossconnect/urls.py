from django.http import HttpResponse
from django.urls import path   

def dummmy_view(request):
    html = "<html><body>Cross Connect plugin.</body></html>"
    return  HttpResponse(html)

urlpatterns = [
    path("", dummmy_view, name="crossconnect_list"),
]