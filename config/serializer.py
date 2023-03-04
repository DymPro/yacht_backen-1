
from rest_framework import serializers
from .models import *

class ExtraFieldsSerializer(serializers.ModelSerializer):
    class Meta():
        model = ExtraFields
        fields = "__all__"

class CardsFieldsSerializer(serializers.ModelSerializer):
    extra_fields = ExtraFieldsSerializer(many=True)
    class Meta():
        model = CardFields
        fields = "__all__"

class CardsSerializer(serializers.ModelSerializer):
    fields = CardsFieldsSerializer(many=True)
    class Meta():
        model = Card
        fields = "__all__"

class TabsSerializer(serializers.ModelSerializer):
    card = CardsSerializer(many=True)
    class Meta():
        model = Tabs
        fields = "__all__"


class FormSerializer(serializers.ModelSerializer):
    tabs = TabsSerializer(many=True)
    class Meta():
        model = Form
        fields = "__all__"