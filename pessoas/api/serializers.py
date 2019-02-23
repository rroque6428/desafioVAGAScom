from rest_framework.serializers import ModelSerializer

from pessoas.models import Pessoa

class PessoaSerializer(ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ('id', 'nome', 'profissao', 'localizacao', 'nivel')
