from rest_framework.viewsets import ModelViewSet

from .serializers import PessoaSerializer
from pessoas.models import Pessoa

from candidaturas.score import *
from candidaturas.models import Candidatura

def updateCandidaturas(id_pessoa):
    # Update all 'candidaturas' related to this 'pessoa'
    for candidatura in Candidatura.objects.filter(id_pessoa=id_pessoa): 
        calcScore(candidatura.id)

class PessoaViewSet(ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

    def create(self, request, *args, **kwargs):
        return super(PessoaViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PessoaViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        response = super(PessoaViewSet, self).update(request, *args, **kwargs)
        updateCandidaturas(response.data.get('id'))
        return response
    
    def destroy(self, request, *args, **kwargs):
        return super(PessoaViewSet, self).destroy(request, *args, **kwargs)
        
    def partial_update(self, request, *args, **kwargs):
        response = super(PessoaViewSet, self).partial_update(request, *args, **kwargs)
        updateCandidaturas(response.data.get('id'))
        return response
