import random

from sort import *
from graph import *
from heap import *

def main():
    test_sort(insertion_sort)
    stress_sort(insertion_sort, 1000, 30, 20)
    test_sort(selection_sort)
    stress_sort(selection_sort, 1000, 30, 20)
    test_sort(bubble_sort)
    stress_sort(bubble_sort, 1000, 30, 20)

    test_sort(quick_sort_recursive)
    stress_sort(quick_sort_recursive, 1000, 30, 20)
    test_sort(quick_sort_iterative)
    stress_sort(quick_sort_iterative, 1000, 30, 20)

    test_merge()
    test_sort(merge_sort_recursive)
    stress_sort(merge_sort_recursive, 1000, 30, 20)
    test_sort(merge_sort_iterative)
    stress_sort(merge_sort_iterative, 1000, 30, 20)

    test_heapify()
    test_heap_sift_down()

    test_sort(heap_sort)
    stress_sort(heap_sort, 1000, 30, 20)

    test_sort(counting_sort)

    test_graph()

    print("passed")

def print_if_ne(l, r):
    if l != r:
        print(l, "!=", r)
    return l == r

def test_sort_with(algo, t, a):
    algo(t)
    return print_if_ne(a, t)

def test_sort(algo):
    assert(test_sort_with(algo, [2, 1], [1, 2]))
    assert(test_sort_with(algo, [1, 2], [1, 2]))
    assert(test_sort_with(algo, [4, 2, 3, 1], [1, 2, 3, 4]))
    assert(test_sort_with(algo, [6, 5, 3, 1, 8, 7, 2, 4], [1, 2, 3, 4, 5, 6, 7, 8]))
    assert(test_sort_with(algo, [5, 5, 3, 8, 1, 2, 2, 7], [1, 2, 2, 3, 5, 5, 7, 8]))

def stress_sort(algo, trials, size, n):
    for i in range(trials):
        t = []
        for j in range(random.randint(0, size)):
            t.append(random.randint(-n, n))
        a = sorted(t)
        assert(test_sort_with(algo, t, a))

def test_merge_with(l, r, a):
    assert(print_if_ne(merge_sort_merge(l, r), a))

def test_merge():
    test_merge_with([1], [2], [1, 2])
    test_merge_with([2], [1], [1, 2])
    test_merge_with([1, 3, 5], [0, 4, 6], [0, 1, 3, 4, 5, 6])

def test_heapify_with(l, a):
    heapify(l)
    assert(print_if_ne(l, a))

def test_heapify():
    test_heapify_with([2, 1], [2, 1])
    test_heapify_with([1, 2], [2, 1])
    test_heapify_with([1, 3, 5], [5, 3, 1])

def test_heap_sift_down_with(l, i, len, a):
    heap_sort_sift_down(l, i, len)
    assert(print_if_ne(l, a))

def test_heap_sift_down():
    test_heap_sift_down_with([1, 2], 0, 2, [2, 1])

def test_graph():
    g = Graph()
    n0 = g.add_node(0)
    n1 = g.add_node(1)
    n2 = g.add_node(2)
    assert(print_if_ne(g.node(n0).data(), 0))
    assert(print_if_ne(g.node(n1).data(), 1))
    assert(print_if_ne(g.node(n2).data(), 2))
    assert(g.size() == 3)
    g.remove_node(n1)
    assert(g.size() == 2)
    n3 = g.add_node(3)
    assert(g.size() == 3)
    assert(n1 == n3)
    g.add_edge(n0, n2)
    g.add_edge(n2, n3)
    g.add_edge(n3, n0)
    assert(print_if_ne(g.node(n0).neighbors(), [n2, n3]))
    assert(print_if_ne(g.node(n2).neighbors(), [n0, n3]))
    assert(print_if_ne(g.node(n3).neighbors(), [n2, n0]))
    g.remove_edge(n0, n2)
    assert(print_if_ne(g.node(n0).neighbors(), [n3]))
    assert(print_if_ne(g.node(n2).neighbors(), [n3]))
    assert(print_if_ne(g.node(n3).neighbors(), [n2, n0]))
    n4 = g.add_node(4)
    assert(g.size() == 4)
    g.add_edge(n0, n4)
    g.add_edge(n3, n4)

    # n0 - n3 - n2
    # \    |
    #  --- n4
    assert(print_if_ne(g.dfs(n0), [n0, n4, n3, n2]))
    assert(print_if_ne(g.bfs(n0), [n0, n3, n4, n2]))
    assert(print_if_ne(len(g.shortest_path(n0, n3)), 1))
    assert(print_if_ne(len(g.shortest_path(n0, n4)), 1))
    assert(print_if_ne(len(g.shortest_path(n0, n2)), 2))

    # 0   6 - - - +
    # |   |       |
    # 1 - 3 - 4 - 8
    # |   |   |
    # 2 - 5   7
    g = Graph()
    for i in range(9):
        g.add_node(i)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 5)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(3, 6)
    g.add_edge(4, 7)
    g.add_edge(4, 8)
    g.add_edge(6, 8)
    assert(print_if_ne(g.dfs(0), [0, 1, 3, 6, 8, 4, 7, 5, 2]))
    assert(print_if_ne(g.bfs(0), [0, 1, 2, 3, 5, 4, 6, 7, 8]))
    assert(print_if_ne(len(g.shortest_path(0, 0)), 0))
    assert(print_if_ne(len(g.shortest_path(0, 1)), 1))
    assert(print_if_ne(len(g.shortest_path(0, 2)), 2))
    assert(print_if_ne(len(g.shortest_path(0, 3)), 2))
    assert(print_if_ne(len(g.shortest_path(0, 4)), 3))
    assert(print_if_ne(len(g.shortest_path(0, 5)), 3))
    assert(print_if_ne(len(g.shortest_path(0, 6)), 3))
    assert(print_if_ne(len(g.shortest_path(0, 7)), 4))
    assert(print_if_ne(len(g.shortest_path(0, 8)), 4))

def test_heap():
    h = BinaryMaxHeap()
    h.insert(3)
    assert(h.top() == 3)
    h.insert(5)
    assert(h.top() == 5)
    h.insert(2)
    assert(h.top() == 5)
    h.insert(1)
    assert(h.top() == 5)
    h.insert(1000)
    assert(h.top() == 1000)
    assert(h.extract() == 1000)
    assert(h.extract() == 5)
    assert(h.extract() == 3)
    assert(h.extract() == 2)
    assert(h.extract() == 1)

if __name__ == "__main__":
    main()
