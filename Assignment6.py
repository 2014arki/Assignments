#! /usr/bin/env python

from __future__ import division, print_function

#task 1

def groups_for_graph(graph):
    """
    :type graph: dict{key: list}
    :param graph:
    :return:
    """
    graph_= {node: [neighbours]}                  # I discovered, that i can't represent the dictionary
    to_visit_ = []                                # abstractedly at right way in this instance
    visited = []
    for node, neighbours in graph:
        to_visit_.append(node)
        to_visit_.append(neighbours)
        while node or neighbours in to_visit_:
            group = ((visited.append(node) or visited.append(neighbours[-1])
                      if not node or neighbours[-1] in visited else neighbours.remove[-1]))    # I wanted to use "pop"
        else:                                                                                  # rather than "remove".
            for reviewed_node in to_visit_, visited:                                           # But "pop" would have
                if reviewed_node in visited:                                     # returned the last value before
                    to_visit_.remove(reviewed_node)                              # deleting of it. So i don't understand
        return group                                                             # what i have to do with this value
                                                                                 # which returned.

# Also i understand that i don't create the new "groups of coherence" if it's more than one.
# I don't know how to provide this action on that code. So i decided that my algorithm is wrong any way
# and i would to correct this problem after correcting of whole algorithm.
# And about realization of "stack". I wanted to know how i have understood its principle: right or not.
# But i think that if it's not - you already find it in my code.