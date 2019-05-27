import random

from sort import *

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

    test_sort(counting_sort)

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

if __name__ == "__main__":
    main()
