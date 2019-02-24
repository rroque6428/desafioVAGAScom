import math

from .dijkstra import *

from candidaturas.models import Candidatura

def calcDistancia(candidatura):
    locVaga = candidatura.id_vaga.localizacao
    locPessoa = candidatura.id_pessoa.localizacao
    return calcCityDistance(locVaga, locPessoa)

def calcScore(id_candidatura):
    candidatura = Candidatura.objects.get(pk=id_candidatura)
    n = 100-25*abs(candidatura.id_vaga.nivel - candidatura.id_pessoa.nivel)
    dist = calcDistancia(candidatura)
    if   dist <= 5:  d = 100
    elif dist <= 10: d = 75
    elif dist <= 15: d = 50
    elif dist <= 20: d = 25
    else: d = 0
    candidatura.score = round((n+d)/2)
    candidatura.save()
    return

# Some internal tests:
# [(calcCityDistance(c1,c2), c1, c2) for c1 in 'ABCDEF' for c2 in 'ABCDEF']
# [calcCityDistance(c1,c2) for c1 in 'ABCDEF' for c2 in 'ABCDEF']
def calcCityDistance(e1, e2):
    edges = [
            ("A", "B", 5),
            ("B", "C", 7),
            ("B", "D", 3),
            ("C", "E", 4),
            ("D", "E", 10),
            ("D", "F", 8),
            ("E", "F", 18), # Added node
            ("C", "D", 10), # Added node
        ]
    l_ = sorted([e1.upper(), e2.upper()]) # secure direction of search
    e1 = l_[0]
    e2 = l_[1]
    return dijkstra(edges, e1, e2)[0]
    
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
