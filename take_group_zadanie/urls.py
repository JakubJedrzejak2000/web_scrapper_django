from django.urls import include, path
from rest_framework import routers

from web_scrapping import views as sel_views

router = routers.SimpleRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("selenium/", include("web_scrapping.urls"))
]