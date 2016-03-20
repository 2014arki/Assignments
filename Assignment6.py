#! /usr/bin/env python

from __future__ import division, print_function
import itertools

# task 1

# I try to change some parts of code and to take into account formation of the "connected groups"

def groups_for_graph(graph):
    """
    :type graph: dict{key: list}
    :param graph:
    :return:
    """
    list_of_groups = []
    to_visit = []
    visited = []
    for (node, neighbours) in graph.iteritems():
        for group in list_of_groups:
            for group_node in group:
                if group_node != node:
                    to_visit.append(node)
                    to_visit.extend(itertools.islice(neighbours, 0, len(neighbours)))
                    for to_vis_node in to_visit:
                        if to_vis_node is to_visit[-1]:
                            set_visited = set(visited)
                            if to_vis_node in graph and to_vis_node not in set_visited:
                                next_neighbours = graph[to_vis_node]
                                visited.append(to_visit.pop())
                                to_visit.extend(itertools.islice(next_neighbours, 0, len(next_neighbours)))
                            else:
                                to_visit.pop()
                    if not to_visit:
                        list_of_groups.append(visited)
                        visited = []
    return list_of_groups


