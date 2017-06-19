from rest_framework import serializers

from word import models


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Word
        fields = "__all__"


class SpeechPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SpeechPart
        fields = "__all__"


class MeaningSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Meaning
        fields = "__all__"
