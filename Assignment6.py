#! /usr/bin/env python

from __future__ import division, print_function

#task 1

def groups_for_graph(graph):
    """
    :type graph: dict{key: list}
    :param graph:
    :return:
    """
    graph_= {node: [neighbours]}
    to_visit_ = []
    visited = []
    for node, neighbours in graph:
        to_visit_.append(node)
        to_visit_.append(neighbours)
        while node or neighbours in to_visit_:
            group = ((visited.append(node) or visited.append(neighbours[-1])
                      if not node or neighbours[-1] in visited else neighbours.remove[-1]))
        else:
            for reviewed_node in to_visit_, visited:
                if reviewed_node in visited:
                    to_visit_.remove(reviewed_node)
        return group

