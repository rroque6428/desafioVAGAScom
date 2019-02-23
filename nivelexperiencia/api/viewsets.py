from rest_framework.viewsets import ModelViewSet

from .serializers import NivelExperienciaSerializer
from nivelexperiencia.models import NivelExperiencia

class NivelExperienciaViewSet(ModelViewSet):
    queryset = NivelExperiencia.objects.all()
    serializer_class = NivelExperienciaSerializer