from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Super
from .serializers import SuperSerializer

@api_view(['GET', 'POST'])
def supers_list(request):

    if request.method == 'GET':
        # supertype = request.query_params.get("type")
        queryset = Super.objects.all()
        # if type:
        #     queryset = queryset.filter(supertype=supertype)
        serializer = SuperSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SuperSerializer(data = request.data)      
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)