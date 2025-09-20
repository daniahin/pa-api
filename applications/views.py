from rest_framework import viewsets, mixins
from .models import Application
from .serializers import ApplicationSerializer

class ApplicationViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
