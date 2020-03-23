from rest_framework import permissions
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework import serializers

from .models import Diary


class DiaryAPI(views.APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        Diary_list = Diary.objects.all()
        serializer = DiarySerializer(instance=Diary_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = DiarySerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data, status=status.HTTP_200_OK)


class DiarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Diary
        fields = '__all__'
