from rest_framework.serializers import ModelSerializer

from candidaturas.models import Candidatura

class CandidaturaSerializer(ModelSerializer):
    class Meta:
        model = Candidatura
        fields = ('id', 'id_vaga', 'id_pessoa')