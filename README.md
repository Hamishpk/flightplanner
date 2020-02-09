# Flight Planner

## Summary

This is a pet project to try and mimick sites such as SkyScanner and Goolgle flights. I plan to apply what I learnt in a Coursera course on graph algorithms. The program is able read data from a mock graph and use that to calculate the routes with the shortest distance, cheapest route and least stops.

The least stops is calculated using BFS and both shortest distance and cheapest route is calculated using Dijkstra's Algorithm.

Currently I'm looking to add three functions:

Available flights - Given a start location and a total budget, return a list of locations reachable from that location within budget.

Route planner - Given a list of locations calculate the cheapest route connecting those locations.

Travel planner - Given a budget and a start location, calculate a route that visits the maximum locations and returns to the start locations.

## Roadmap

Fist on the list is impliment a priority queue to impove the runtime of Dijkstras. Then complete the functions and once everything is working through my command line I'll build a back end using Flask and host it on Heroku.

Currently the program runs on dummy data I generate myself, once the above is complete I'll look into either collecting real life flight data or if an API exists even better :)


## Setup

Program is built in Python 3.6 and no additional libraries are needed.

## Testing

TBC
