from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Super
from .serializers import SuperSerializer

@api_view(['GET', 'POST'])
def supers_list(request):

    if request.method == 'GET':
        super_type = request.query_params.get("supertype")
        supers = Super.objects.all()
        if super_type:
            queryset = queryset.filter(super_type=super_type)
        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SuperSerializer(data = request.data)      
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)