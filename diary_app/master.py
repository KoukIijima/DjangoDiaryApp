from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist


class MasterApi(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        return Response(None, status=status.HTTP_200_OK)