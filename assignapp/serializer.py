from rest_framework import serializers
from assignapp.models import Industry

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model=Industry
        fields=('date','open','high','low','close','adjclose','volume')