from django.urls import path

from web_scrapping.views import ArticleRename, ArticleDetail

urlpatterns = [
    path("", ArticleRename.as_view(), name="selenium"),
    path("<id>", ArticleDetail.as_view())
]