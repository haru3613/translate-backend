# serializers.py
from rest_framework import serializers

class TranslationSerializer(serializers.Serializer):
    source_text = serializers.CharField()
    target_language = serializers.CharField()
    translated_text = serializers.CharField(read_only=True)
