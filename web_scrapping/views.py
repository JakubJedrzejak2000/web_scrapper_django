from rest_framework.response import Response
from rest_framework.views import APIView

from web_scrapping.models import Web
from web_scrapping.serializers import WebSerializer


class ArticleRename(APIView):

    def get(self, request):
        webs = Web.objects.all()
        domain = request.query_params.get("source")
        if domain:
            webs = webs.filter(url__icontains=domain)
        serialized = WebSerializer(webs, many=True).data
        return Response(serialized)


class ArticleDetail(APIView):
    def get(self, request, id):
        try:
            web = Web.objects.get(id=id)
            web = WebSerializer(web)
            return Response(web.data)
        except Web.DoesNotExist:
            return Response({"Error!"})
