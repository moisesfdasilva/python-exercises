from rest_framework import viewsets
from .models import Client
from .serializers import ClientSerializer
from .permissions import IsOwner


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsOwner]
