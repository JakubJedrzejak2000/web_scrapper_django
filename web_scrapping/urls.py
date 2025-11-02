from django.urls import path

from web_scrapping.views import SeleniumList, SeleniumDetail

urlpatterns = [
    path("", SeleniumList.as_view(), name="selenium"),
    path("<id>", SeleniumDetail.as_view())
]