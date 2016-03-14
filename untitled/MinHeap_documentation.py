#! /usr/bin/env python


from __future__ import print_function, division


class Node(object):

    """
    The object that has item and priority. It can be compared with other Node by it's priority.
    :type item: any
    :type priority: digit
    """

    def __init__(self, item, priority):
        self._item = item
        self._priority = priority

    @property
    def item(self):
        return self._item

    @property
    def priority(self):
        return self._priority

    def __str__(self):
        return str((self.item, self.priority))

    def __ne__(self, other):
        """
        Return true if Node is not equal other Node
        :type other: Node
        :return: bool
        """
        return not self == other

    def __eq__(self, other):
        """
        Return true if Node is equal other Node
        :type other: Node
        :return: bool
        """
        return self.priority == other.priority

    def __gt__(self, other):
        """
        Return true if Node is greater than other Node
        :type other: Node
        :return: bool
        """
        return self.priority > other.priority

    def __ge__(self, other):
        """
        Return true if Node is greater than or equal other Node
        :type other: Node
        :return: bool
        """
        return self.priority >= other.priority

    def __lt__(self, other):
        """
        Return true if Node is less than other Node
        :type other: Node
        :return: bool
        """
        return self.priority < other.priority

    def __le__(self, other):
        """
        Return true if Node is less than or equal other Node
        :type other: Node
        :return: bool
        """
        return self.priority <= other.priority


class MinHeap(object):
    """
    It is instance of binary tree data structure. At he head of tree Node with minimal value.
    Each parent Node have no more than two children-Nodes. Each parent Node value must be smaller than
    its child Node value. The first Node of MinHeap is always 0 and inputting of Nodes always starts with 1st index.
    The lenght of MinHeap is len(self) -1
    :type _heap: list
    """
    def __init__(self):
        self._heap = [0]

    def __len__(self):
        return len(self._heap) - 1

    def __nonzero__(self):
        return bool(len(self))

    def _exchange(self, i, j):
        """
        Exchange positions of two Nodes with [i] and [j] indices
        :type i: int
        :param i:
        :type j: int
        :param j:
        :return:
        """
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def _percolate_up(self, i):
        """
        Percolate up Node with [i] index by exchanging positions of Node[i] and its parent
        if Node[i] meets the conditions.
        :type i: int
        :param i:
        :return:
        """
        cur_pos = i
        while cur_pos // 2 > 0:
            parent_idx = self._parent_idx(i)
            if self._heap[cur_pos] >= self._heap[parent_idx]:
                break
            self._exchange(cur_pos, parent_idx)
            i //= 2
            cur_pos //= 2

    def _percolate_down(self, i):
        """
         Percolate down Node with [i] index by exchanging positions of Node[i] and its minimal child
        if Node[i] meets the conditions.
        :type i: int
        :param i:
        :return:
        """
        while (i * 2) <= len(self):
            min_child_index = self._min_child_idx(i)
            if self._heap[i] > self._heap[min_child_index]:
                self._exchange(i, min_child_index)
            i = min_child_index

    def _min_child_idx(self, i):
        """
        Return child with minimal value from children indices for Node with [i] index
        :type i: int
        :param i:
        :return:
        """
        children_indices = self._children_indices(i)
        if not children_indices:
            return None
        children = [self._heap[idx] for idx in children_indices]
        return sorted(zip(children, children_indices))[0][1]

    @staticmethod
    def _parent_idx(i):
        """
        Return value of parent index for Node with [i] index
        :type i: int
        :param i:
        :return:
        """
        return i // 2

    def _children_indices(self, i):
        """
        Return tuple with indices of children from possible children for Node with [i] index
        :type i: int
        :param i:
        :return:
        """
        possible_children = [i * 2, (i * 2) + 1]
        return tuple(idx for idx in possible_children if idx <= len(self))

    def get_min(self):
        """
        Return value of Node with index [1]
        :return:
        """
        if not self:
            raise ValueError("The heap is empty")
        return self._heap[1]

    def pop_min(self):
        """
        Return Node with minimal value. This function exchange positions of Node[1] and Node with last index
        in the MinHeap with further execution of pop and percolating down of Node [1]
        :return:
        """
        min_val = self.get_min()
        self._exchange(1, len(self))
        self._heap.pop()
        self._percolate_down(1)
        return min_val

    def push(self, item):
        """
        This function append Node to MinHeap and percolate it up
        :type item: Node
        """
        if not isinstance(item, Node):
            raise ValueError("`item` should be a `Node` instance")
        self._heap.append(item)
        self._percolate_up(len(self))


class Memoize(object):
    def __init__(self, func):
        self._func = func
        self._cache = {}

    def __call__(self, *args):
        return args not in self.cache and self.cache.update(
            {args: self.func(*args)}) or self.cache.get(args)

    @property
    def cache(self):
        return self._cache

    @property
    def func(self):
        return self._func

    def is_cached(self, *args):
        return frozenset(args) in self.cache


@Memoize               # sqrt = Memoize(sqrt)
def sqrt(num):
    return num ** 0.5


def test_heap():
    heap = MinHeap()
    nodes = [Node(val, val) for val in xrange(9, -1, -1)]
    for node in nodes:
        heap.push(node)
    while heap:
        print(heap.pop_min())


def main():
    test_heap()

if __name__ == "__main__":
    main()
