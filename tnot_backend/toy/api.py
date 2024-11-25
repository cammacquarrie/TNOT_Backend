from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Toy
from .serializers import ToysListSerializer, ToysDetailSerializer


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def toys_list(request):
    toys = Toy.objects.all()
    serializer = ToysListSerializer(toys, many=True)

    return JsonResponse({
        'data': serializer.data
    })


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def toys_detail(request, pk):
    toy = Toy.objects.get(pk=pk)

    serializer = ToysDetailSerializer(toy, many=False)

    return JsonResponse(serializer.data)
