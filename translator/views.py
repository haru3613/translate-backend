from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TranslationSerializer
from google.cloud import translate_v2 as translate

class TranslateView(APIView):
    
    def translate(self, source_text, target_language):
        client = translate.Client()
        result = client.translate(source_text, target_language=target_language)
        
        return result['translatedText']        
        
    def post(self, request):
        serializer = TranslationSerializer(data=request.data)
        
        if serializer.is_valid():
            source_text = serializer.validated_data['source_text']
            target_language = serializer.validated_data['target_language']

            # 假设你的翻译函数叫做 'translate'
            translated_text = self.translate(source_text, target_language)

            # 添加翻译后的文本到返回的数据中
            return_data = {
                'source_text': source_text,
                'target_language': target_language,
                'translated_text': translated_text
            }

            return Response(return_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
