from rest_framework import serializers
from web_scrapping.models import Web

class WebSerializer(serializers.ModelSerializer):
    class Meta:
        model = Web
        fields = "__all__"
