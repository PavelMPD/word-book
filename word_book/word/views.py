from rest_framework import viewsets

from word import models
from word import serializers


class WordViewSet(viewsets.ModelViewSet):
    queryset = models.Word.objects.all()
    serializer_class = serializers.WordSerializer


class SpeechPartViewSet(viewsets.ModelViewSet):
    queryset = models.SpeechPart.objects.all()
    serializer_class = serializers.SpeechPartSerializer


class MeaningViewSet(viewsets.ModelViewSet):
    queryset = models.Meaning.objects.all()
    serializer_class = serializers.MeaningSerializer
