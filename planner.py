# Python 3

import sys

class Graph:
    """
    SUMMARY
    Takes a text input and creates a graph using a list of list.
    ----
    INPUT
    A .TXT file in the form:

    n m
    s e c d

    where

    n = Number of airports (Nodes)
    m = Number of connections (Edges)
    s = Start of an edge
    e = End of an edge
    c = Cost associated with that edge
    d = Distance associated with that edge
    ----
    OUTPUT
    3 graphs made from lists of lists

    1. Connecting edges
    2. Costs of edges
    3. Distance between edges
    ----
    """
    def __init__(self):
        pass

    def read_data(self):
        pass



class FlightCalculators:
    """
    Creates flight plans between two locations optermising on:
    1. The least changes
    2. The cheapest
    3. The shortest distance

    All functions take a graph constructed of a list of lists and two integer
    values connected with the city.
    ----
    """

    def __init__(self):
        pass


    def least_stops(self, graph, a, b):
        """
        SUMMARY
        Caluclates the path between the two cities with the least amount of stops.

        Algorithm - BFS
        ----
        INPUT
        Takes the graph of airports, Graph.
        The integer value of the airport representing starting airport, a.
        The integer value of the airport representing the target airport, b.
        ----
        OUTPUT
        Integer value representing the number of stops.
        """
        self.size = len(graph)
        self.visisted = [False] * size
        self.no_stops = [-1] * size
        self.queue = []
        self.queue.append(a)
        self.visited[a] = True
        self.no_stops[a] = 0

        while self.queue:
            self.node = self.queue.pop(0)

            for i in graph[self.node]:
                if self.visited[i] == False:
                    self.queue.append(i)
                    self.no_stops[i] = no_stops[node] + 1
                    self.visitied[i] = True

        if self.distance[t] = -1:
            return "Sorry, no possible route"

        else:
            return distance[b]


    def lowest_weight(self, graph, weight, a, b):

        pass

    def getmin(weights, visitied):
        """
        Temp method of finding minimum value for Dijkstra's algo.
        Worst case run time On^2
        Will replace with heap
        """
        self.min_val = sys.maxsize
        self.min_index = 0

        for i in range(len(slef.min_val)):
            if self.weights[i] < self.minval and self.visitied[i] == False:
                self.min_val = self.weights[i]
                self.min_index = i
        return min_index
