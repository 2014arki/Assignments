#! /usr/bin/env python

from __future__ import division, print_function

#task 1

def groups_for_graph(graph):
    """
    :type graph: dict{key: list}
    :param graph:
    :return:
    """
    graph_= {node: [neighbours]}                  # столкнулась с проблемой, что не понимаю как
    to_visit_ = []                                # обстрактно изобразить словарь в нужном виде
    visited = []
    for node, neighbours in graph:
        to_visit_.append(node)
        to_visit_.append(neighbours)
        while node or neighbours in to_visit_:
            group = ((visited.append(node) or visited.append(neighbours[-1])
                      if not node or neighbours[-1] in visited else neighbours.remove[-1]))    # вместо remove
        else:                                                                                  #я хотела использовать
            for reviewed_node in to_visit_, visited:                                           #pop, но это бы возвра-
                if reviewed_node in visited:                                     #щало мне эту вершину перед удалением,
                    to_visit_.remove(reviewed_node)                              #но я не понимаю, что я с ней должна
        return group                                                             #была тогда делать

# и да, я понимаю, что здесь нет создания новых групп связности, если они имеются, но я решила, что
# алгоритм все равно составлен неправильно и надеялась уже после его правки как-то разобраться с
# этим моментом
# а насчет реализации как стека: я скорее хотела узнать, правильно ли я поняла вообще его принцип,
# но тут и так, наверное, все непонимание уже вскрылось в самом коде, если что