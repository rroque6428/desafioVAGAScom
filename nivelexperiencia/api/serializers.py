from rest_framework.serializers import ModelSerializer

from nivelexperiencia.models import NivelExperiencia

class NivelExperienciaSerializer(ModelSerializer):
    class Meta:
        model = NivelExperiencia
        fields = ('id', 'nivel', 'descricao')
