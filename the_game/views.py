from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import GameSerializer
from .models import TheGame
from .game import get_game_result
from .utils import array_to_string


@api_view(['POST'])
def add_grid(request):
    serializer = GameSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def grid_get_update_oparate(request, id):
    grid = get_object_or_404(TheGame, pk=id)

    if request.method == 'PATCH':
        serializer = GameSerializer(grid, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET' and not request.GET.get('after', None):
        serializer = GameSerializer(grid)
        return Response(serializer.data)

    elif request.method == 'GET' and request.GET.get('after'):
        try:
            ages = list(map(lambda x: int(x), request.GET.get('after').split(',')))
            ages_str = request.GET.get('after').split(',')
        except ValueError:
            return Response({'message': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
        results = get_game_result(grid, ages)

        restponse_data = dict()
        restponse_data['id'] = grid.id
        restponse_data['x'] = grid.x
        restponse_data['y'] = grid.y
        restponse_data['data'] = []
        for age in ages_str:
            if age in results:
                data = dict()
                data['age'] = age
                grid = results[age]
                if not type(grid) == str:
                    grid = array_to_string(grid)
                data['grid'] = grid
                restponse_data['data'].append(data)
        return Response(restponse_data)
