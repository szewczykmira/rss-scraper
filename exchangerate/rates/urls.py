from django.urls import path

from .views import rate_detail, rates_list

urlpatterns = [path("", rates_list), path("<str:currency>", rate_detail)]
