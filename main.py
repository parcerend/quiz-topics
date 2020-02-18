from graph import Graph, Node, Arc

nodeAlbacete = Node('Albacete')
nodeBadajoz = Node('Badajoz')
nodeBarcelona = Node('Barcelona')
nodeBilbao = Node('Bilbao')
nodeCadiz = Node('Cadiz')
nodeCoruna = Node('Coruña')
nodeGerona = Node('Gerona')
nodeGranada = Node('Granada')
nodeJaen = Node('Jaen')
nodeMadrid = Node('Madrid')
nodeMurcia = Node('Murcia')
nodeOviedo = Node('Oviedo')
nodeSevilla = Node('Sevilla')
nodeValencia = Node('Valencia')
nodeValladolid = Node('Valladolid')
nodeVigo = Node('Vigo')
nodeZaragoza = Node('Zaragoza')

grafo_quiz = Graph([
    nodeAlbacete,
    nodeBadajoz,
    nodeBarcelona,
    nodeBilbao,
    nodeCadiz,
    nodeCoruna,
    nodeGerona,
    nodeGranada,
    nodeJaen,
    nodeMadrid,
    nodeMurcia,
    nodeOviedo,
    nodeSevilla,
    nodeValencia,
    nodeValladolid,
    nodeVigo,
    nodeZaragoza
], [
    Arc(251, nodeAlbacete, nodeMadrid),
    Arc(150, nodeAlbacete, nodeMurcia),
    Arc(191, nodeAlbacete, nodeValencia),
    Arc(403, nodeBadajoz, nodeMadrid),
    Arc(100, nodeBarcelona, nodeGerona),
    Arc(349, nodeBarcelona, nodeValencia),
    Arc(296, nodeBarcelona, nodeZaragoza),
    Arc(395, nodeBilbao, nodeMadrid),
    Arc(304, nodeBilbao, nodeOviedo),
    Arc(280, nodeBilbao, nodeValladolid),
    Arc(324, nodeBilbao, nodeZaragoza),
    Arc(125, nodeCadiz, nodeSevilla),
    Arc(455, nodeCoruna, nodeValladolid),
    Arc(171, nodeCoruna, nodeVigo),
    Arc(100, nodeGerona, nodeBarcelona),
    Arc(99, nodeGranada, nodeJaen),
    Arc(278, nodeGranada, nodeMurcia),
    Arc(256, nodeGranada, nodeSevilla),
    Arc(99, nodeJaen, nodeGranada),
    Arc(335, nodeJaen, nodeMadrid),
    Arc(242, nodeJaen, nodeSevilla),
    Arc(251, nodeMadrid, nodeAlbacete),
    Arc(403, nodeMadrid, nodeBadajoz),
    Arc(395, nodeMadrid, nodeBilbao), 
    Arc(335, nodeMadrid, nodeJaen), 
    Arc(193, nodeMadrid, nodeValladolid),
    Arc(325, nodeMadrid, nodeZaragoza),
    Arc(150, nodeMurcia, nodeAlbacete),
    Arc(278, nodeMurcia, nodeGranada),
    Arc(241, nodeMurcia, nodeValencia),
    Arc(304, nodeOviedo, nodeBilbao),
    Arc(125, nodeSevilla, nodeCadiz),
    Arc(256, nodeSevilla, nodeGranada),
    Arc(242, nodeSevilla, nodeJaen),
    Arc(191, nodeValencia, nodeAlbacete),
    Arc(349, nodeValencia, nodeBarcelona),
    Arc(241, nodeValencia, nodeMurcia),
    Arc(280, nodeValladolid, nodeBilbao),
    Arc(455, nodeValladolid, nodeCoruna),
    Arc(193, nodeValladolid, nodeMadrid),
    Arc(356, nodeValladolid, nodeVigo),
    Arc(171, nodeVigo, nodeCoruna),
    Arc(356, nodeVigo, nodeValladolid),
    Arc(296, nodeZaragoza, nodeBarcelona),
    Arc(324, nodeZaragoza, nodeBilbao),
    Arc(325, nodeZaragoza, nodeMadrid)
])

deepPath = grafo_quiz.find_depth_path(nodeCoruna, nodeCadiz)
path = grafo_quiz.find_path(nodeCoruna, nodeCadiz)


for place in path.get('path'):
    print(place[0].value)

print(path.get('distance'))

print('')

for place in deepPath.get('path'):
    print(place[0].value)
print(deepPath.get('distance'))
