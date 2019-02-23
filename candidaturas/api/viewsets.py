from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from .serializers import CandidaturaSerializer

from candidaturas.score import *
from candidaturas.models import Candidatura

class CandidaturaViewSet(ModelViewSet):
    queryset = Candidatura.objects.all()
    serializer_class = CandidaturaSerializer

    @action(methods=['get'], detail=False)
    def _ranking(self, request):
        return Response({'ok':1})

    def create(self, request, *args, **kwargs):
        response = super(CandidaturaViewSet, self).create(request, *args, **kwargs)
        # import pdb; pdb.set_trace() # - - - DEBUG
        calcScore(response.data.get('id'))
        return response

    def retrieve(self, request, *args, **kwargs):
        return super(CandidaturaViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        response =  super(CandidaturaViewSet, self).update(request, *args, 
        **kwargs)
        calcScore(response.data.get('id'))
        return response
    
    def destroy(self, request, *args, **kwargs):
        return super(CandidaturaViewSet, self).destroy(request, *args, **kwargs)
        
    def partial_update(self, request, *args, **kwargs):
        response = super(CandidaturaViewSet, self).partial_update(request, *args, **kwargs)
        calcScore(response.data.get('id')) 
        return response
