#! /usr/bin/env python

from __future__ import division, print_function

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
        if node not in set(list_of_groups):
            to_visit.append(node)
            to_visit.append(neighbours)
            while len(to_visit):
                group = (((visited.append(node) or visited.append(neighbours[-1]) for node, neighbours in to_visit
                       if node and neighbours[-1] not in visited)))
                for reviewed_node in to_visit:
                    if reviewed_node in visited:
                        to_visit.remove(reviewed_node)
                    if not len(neighbours):
                        to_visit.remove(neighbours)
                else:
                    list_of_groups.append(group)
    return list_of_groups


