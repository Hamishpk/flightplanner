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
        input = sys.stdin.read()
        self.data = list(map(int, input.split()))
        self.n, self.m = self.data[0:2]
        self.data = self.data[2:]
        self.edges = list(zip(zip(self.data[0:(4 * self.m):4],
            self.data[1:(4 * self.m):4]), self.data[2:(4 * self.m):4], self.data[3:(4 * self.m):4]))
        self.data = self.data[3 * self.m:]
        self.graph = [[] for _ in range(self.n)]
        self.cost = [[] for _ in range(self.n)]
        self.distance = [[] for _ in range(self.n)]
        for ((a, b), c, d) in self.edges:
            self.graph[a - 1].append(b - 1)
            #self.graph[b - 1].append(a - 1)
            self.cost[a - 1].append(c)
            self.distance[a - 1].append(d)
        self.s, self.t = self.data[0] - 1, self.data[1] - 1





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

    def __init__(self, graph, cost, a, b):
        self.graph = graph
        self.cost = cost
        self.size = len(graph)
        self.a = a
        self.b = b


    def least_stops(self):
        """
        SUMMARY
        Caluclates the path between the two cities with the least amount of stops.

        Algorithm - BFS
        Runtime - O(n + m)
        ----
        INPUT
        Takes the graph of airports, Graph.
        The integer value of the airport representing starting airport, a.
        The integer value of the airport representing the target airport, b.
        ----
        OUTPUT
        Integer value representing the number of stops.
        """
        self.visited = [False] * self.size
        self.no_stops = [-1] * self.size
        self.queue = []
        self.queue.append(self.a)
        self.visited[self.a] = True
        self.no_stops[self.a] = 0

        while self.queue:
            self.node = self.queue.pop(0)

            for i in self.graph[self.node]:
                if self.visited[i] == False:
                    self.queue.append(i)
                    self.no_stops[i] = self.no_stops[self.node] + 1
                    self.visited[i] = True

        if self.no_stops[self.b] == -1:
            return "Sorry, no possible route"

        else:
            return self.no_stops[self.b]


    def cheapest_route(self):
        return self.dijkstras(self.cost)


    def shortest_distance(self):
        return self.dijkstras(self.distance)



    def dijkstras(self, weighting):
        """
        SUMMARY
        Calculates the optimal path for a weight graph. Currently only optimizes
        on cost but will soon include distance.

        Algorithm - Dijkstras
        Runtime - O(n^2)
        """
        self.weighting = weighting
        self.weight_vals = [sys.maxsize] * self.size
        self.visited = [False] * self.size
        self.weight_vals[self.a] = 0

        for i in range(self.size + 1):
            self.index = self.getmin(self.weight_vals, self.visited)
            self.visited[self.index] = True

            for j in range(len(self.graph[self.index])):
                if self.weight_vals[self.graph[self.index][j]] > self.weight_vals[self.index] + self.weighting[self.index][j]:
                    self.weight_vals[self.graph[self.index][j]] = self.weight_vals[self.index] + self.weighting[self.index][j]


        if self.weight_vals[self.b] == sys.maxsize:
            return "Sorry, no possible route"

        return self.weight_vals[self.b]



    def getmin(self, weights, visitied):
        """
        Temp method of finding minimum value for Dijkstra's algo.
        Worst case run time O(n^2)
        Will replace with heap
        """
        self.min_val = sys.maxsize
        self.min_index = 0

        for i in range(self.size):
            if self.weight_vals[i] < self.min_val and self.visited[i] == False:
                self.min_val = self.weight_vals[i]
                self.min_index = i
        return self.min_index


if __name__ == "__main__":
    graph = Graph()
    planner = FlightCalculators(graph.graph, graph.cost, graph.s, graph.t)
    print(planner.least_stops())
    print(planner.cheapest_route())
