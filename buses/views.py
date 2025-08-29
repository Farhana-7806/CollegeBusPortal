from rest_framework import viewsets
from .models import Bus
from .serializers import BusSerializer
from rest_framework.permissions import IsAuthenticated

class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
    permission_classes = [IsAuthenticated]
