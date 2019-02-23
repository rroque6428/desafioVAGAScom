from django.http import JsonResponse

from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import VagaSerializer
from vagas.models import Vaga

from candidaturas.score import *
from candidaturas.models import Candidatura
from candidaturas.api.serializers import CandidaturaSerializer
from pessoas.models import Pessoa
from pessoas.api.serializers import PessoaSerializer

def updateCandidaturas(id_vaga):
    # Update all 'candidaturas' related to this 'vaga'
    for candidatura in Candidatura.objects.filter(id_vaga=id_vaga): 
        calcScore(candidatura.id)

# class VagaReportsViewSet(ModelViewSet):
#     queryset = Vaga.objects.all()
#     serializer_class = VagaSerializer

#     @action(methods=['get'], detail=True)
#     def ranking(self, request, pk=None):
#         queryset = Candidatura.objects.filter(id_vaga=pk).order_by('score')
#         l_ = []
#         for candidatura in queryset:
#             dct_ = PessoaSerializer(candidatura.id_pessoa).data
#             dct_.update({"score": candidatura.score})
#             dct_.pop('id')
#             l_.append(dct_)
#         return JsonResponse(l_, safe=False)

class VagaViewSet(ModelViewSet):
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('empresa', 'titulo')

    # def get_queryset(self):
    #     return Vaga.objects.all()

    @action(methods=['get'], detail=True)
    def candidaturas(self, request, pk=None):   
        queryset = Candidatura.objects.filter(id_vaga=pk).order_by('score')
        serializer = CandidaturaSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def ranking(self, request, pk=None):
        # import pdb; pdb.set_trace() # - - - DEBUG
        queryset = Candidatura.objects.filter(id_vaga=pk).order_by('score')
        l_ = []
        for candidatura in queryset:
            dct_ = PessoaSerializer(candidatura.id_pessoa).data
            dct_.update({"score": candidatura.score})
            dct_.pop('id')
            l_.append(dct_)
        return JsonResponse(l_, safe=False)

    def create(self, request, *args, **kwargs):
        return super(VagaViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(VagaViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        response = super(VagaViewSet, self).update(request, *args, **kwargs)
        updateCandidaturas(response.data.get('id'))
        return response
    
    def destroy(self, request, *args, **kwargs):
        return super(VagaViewSet, self).destroy(request, *args, **kwargs)
        
    def partial_update(self, request, *args, **kwargs):
        response = super(VagaViewSet, self).partial_update(request, *args, **kwargs)
        updateCandidaturas(response.data.get('id'))
        return response
