from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Carta
from .serializers import CartaSerializer

@api_view(['GET', 'POST'])
def api_cartas_list(request):
    # GET: Obtener todas las cartas (200 OK)
    if request.method == 'GET':
        cartas = Carta.objects.all()
        serializer = CartaSerializer(cartas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST: Crear una nueva carta (201 Created)
    elif request.method == 'POST':
        serializer = CartaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "mensaje": "Carta creada correctamente",
                "carta": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def api_carta_detail(request, pk):
    try:
        carta = Carta.objects.get(pk=pk)
    except Carta.DoesNotExist:
        return Response({"error": "Carta no encontrada"}, status=status.HTTP_404_NOT_FOUND)

    # GET: Obtener una carta específica
    if request.method == 'GET':
        serializer = CartaSerializer(carta)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # PUT: Actualizar completamente la carta
    elif request.method == 'PUT':
        serializer = CartaSerializer(carta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "mensaje": "Carta actualizada correctamente",
                "carta": serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE: Eliminar la carta
    elif request.method == 'DELETE':
        carta.delete()
        return Response({"mensaje": "Carta eliminada correctamente"}, status=status.HTTP_204_NO_CONTENT)