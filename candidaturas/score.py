import math

from candidaturas.models import Candidatura

def calcDistancia(candidatura):
    locVaga = candidatura.id_vaga.localizacao
    locPessoa = candidatura.id_pessoa.localizacao
    return 100

def calcScore(id_candidatura):
    candidatura = Candidatura.objects.get(pk=id_candidatura)
    n = 100-25*abs(candidatura.id_vaga.nivel - candidatura.id_pessoa.nivel)
    d = calcDistancia(candidatura)
    candidatura.score = (n+d)/2
    candidatura.save()
    return

# def getMatrixOfDistances():
#     cities_pairs = ['AB','BC','BD','CE','DE','DF']
#     cities_distances = [5,7,3,4,10,8]
#     m_dim = len(cities_pairs)
#     m = [[0 for i in range(m_dim)] for j in range(m_dim)]

# def generate_cities_coords():
#     # Project cities in a line
#     def get_relative_coord(distance):
#         angle = 0
#         x = round(math.cos(math.radians(angle))*distance, 2)
#         y = round(math.sin(math.radians(angle))*distance, 2)
#         return (x,y)
#     def get_absolute_coord(c1, c2):
#         return (c1[0]+c2[0], c1[1]+c2[1])
#     def calc_y(distance, x):
#         y = int(math.sqrt(abs(distance**2 - x**2)))
#         return (x,y)
#     city_coords = {}
#     cities_connected = ['AB','BC','BD','CE','DE','DF']
#     cities_distances = [5,7,3,4,10,8]
#     for (i, pair) in enumerate(cities_connected):
#         r_coord = get_relative_coord(cities_distances[i])
#         if not city_coords:
#             city_coords[pair[0]] = (0,0)
#             city_coords[pair[1]] = r_coord
#         else:    
#             if pair[0] in city_coords:
#                 city_coords[pair[1]] = get_absolute_coord(city_coords[pair[0]], r_coord)
#                 print(pair[0], pair[1], city_coords[pair[1]])
#             elif pair[1] in city_coords:
#                 city_coords[pair[0]] = get_absolute_coord(city_coords[pair[1]], r_coord)
#                 print(pair[0], pair[1], city_coords[pair[0]])
#             else:
#                 raise Exception('Disconnected cities detected.')
#     return city_coords
