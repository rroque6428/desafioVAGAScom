from rest_framework.serializers import ModelSerializer

from vagas.models import Vaga

class VagaSerializer(ModelSerializer):
    class Meta:
        model = Vaga
        fields = ('id', 'empresa', 'titulo', 'descricao', 'localizacao', 'nivel')