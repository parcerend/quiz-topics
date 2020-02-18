# @packages
from functools import reduce
from queue import Queue
import graphutils

class Arc:
    def __init__(self, weigth, initial_node, final_node):
        assert weigth > 0, 'Weigth must be greather than 0'
        self.weigth = weigth
        self.initial_node = initial_node
        self.final_node = final_node

class Node:
    def __init__(self, value):
        self.value = value

class Graph:
    def __init__(self, nodes, arcs):
        self.nodes = graphutils.init_edged_list(nodes, arcs)
        self.nodes_length = len(nodes)

    def deep_first_search(self, initial_node):
        visited_nodes = graphutils.init_visited_nodes(self.nodes.keys())
        previous = graphutils.init_visited_nodes(self.nodes.keys())
        distance = {}
        
        for key in self.nodes.keys():
            distance[key] = 1e1000 # Infinite

        distance[initial_node.value] = 0

        def dfs(initial_node):
            if visited_nodes[initial_node[0].value]:
                return

            visited_nodes[initial_node[0].value] = True
            neighboors = self.nodes[initial_node[0].value]

            for neighboor in neighboors:
                new_distance = distance[initial_node[0].value] + neighboor[1]
                
                if new_distance < distance[neighboor[0].value]:
                    previous[neighboor[0].value] = initial_node
                    distance[neighboor[0].value] = new_distance
                    dfs(neighboor)

        dfs((initial_node, 0))
        
        return { 'distance': distance, 'previous': previous }


    def breadth_first_search(self, initial_node, goal_node):
        visited_nodes = graphutils.init_visited_nodes(self.nodes.keys())
        queue = Queue(self.nodes_length)
        queue.put(initial_node)
        visited_nodes[initial_node.value] = True
        graph_nodes = []

        while not queue.empty():
            front = queue.get()
            neighboors = self.nodes[front.value]

            for neighboor in neighboors:
                if not visited_nodes[neighboor[0].value]:
                    graph_nodes.append(neighboor[0])
                    visited_nodes[neighboor[0].value] = True
                    queue.put(neighboor[0])

                    if goal_node and neighboor[0].value == goal_node.value:
                        return graph_nodes

        return graph_nodes

    def dijkstra(self, initial_node):
        visited_nodes = graphutils.init_visited_nodes(self.nodes.keys())
        previous = graphutils.init_visited_nodes(self.nodes.keys())
        distance = {}

        for node in self.nodes.keys():
            distance[node] = 1e1000

        distance[initial_node.value] = 0
        queue = Queue()
        queue.put((initial_node, 0))

        while not queue.empty():
            current_node = queue.get()
            visited_nodes[current_node[0].value] = True
            for neighboor in self.neighboors(current_node[0]):
                if visited_nodes[neighboor[0].value]:
                    continue

                new_distance = distance[current_node[0].value] + neighboor[1]

                if new_distance < distance[neighboor[0].value]:
                    previous[neighboor[0].value] = current_node
                    distance[neighboor[0].value] = new_distance
                    queue.put((neighboor[0], new_distance))

        return {'distance': distance, 'previous': previous}

    def find_depth_path(self, initial_node, final_node):
        dijkstra = self.dijkstra(initial_node)
        path = []

        if (not dijkstra.get('previous')[final_node.value]):
            return { 'path': path, 'distance': 10e2000 }

        queue = Queue()
        queue.put(dijkstra.get('previous')[final_node.value])

        while not queue.empty():
            current = queue.get()

            if current:
                path.append(current)
                queue.put(dijkstra.get('previous')[current[0].value])

        current_distance = reduce(
            lambda acumulated, 
            current, 
            : acumulated + current[1], 
            path, 
            0)

        path.insert(
            0, 
            (final_node, abs(dijkstra.get('distance')[final_node.value] - current_distance)))

        return {
            'path': list(reversed(path)),
            'distance': dijkstra.get('distance')[final_node.value]
        }

    def find_path(self, initial_node, final_node):
        dijkstra = self.deep_first_search(initial_node)
        path = []

        if (not dijkstra.get('previous')[final_node.value]):
            return { 'path': path, 'distance': 10e2000 }

        queue = Queue()
        queue.put(dijkstra.get('previous')[final_node.value])

        while not queue.empty():
            current = queue.get()
            if current:
                path.append(current)
                queue.put(dijkstra.get('previous')[current[0].value])

        current_distance = reduce(
            lambda acumulated, 
            current, 
            : acumulated + current[1], 
            path, 
            0)

        path.insert(
            0, 
            (final_node, abs(dijkstra.get('distance')[final_node.value] - current_distance)))

        return {
            'path': list(reversed(path)),
            'distance': dijkstra.get('distance')[final_node.value]
        }

    def neighboors(self, node):
        return self.nodes[node.value]
