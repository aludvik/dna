# HeapSort

# For i from 1 to len - 1
#   For j from i to 0
#       A[j] = either the element originally at i or a copy of element j - 1
#
#               el
#               ^
#               |
#    |--------- choose a[j] = el or a[j - 1]
#    |          |
#    v          v
#  | a[j - 1] | a[j] |
#
def insertion_sort(l):
    for i in range(1, len(l)):
        el = l[i]
        for j in range(i, -1, -1):
            if j == 0 or el > l[j - 1]:
                l[j] = el
                break
            else:
                l[j] = l[j - 1]

# Find the min, put at start, repeat recursively with rest of the list
def selection_sort(l):
    for i in range(0, len(l)):
        m = i
        for j in range(i + 1, len(l)):
            if l[j] < l[m]:
                m = j
        l[i], l[m] = l[m], l[i]

# - BubbleSort
def bubble_sort(l):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(1, len(l)):
            if l[i - 1] > l[i]:
                l[i - 1], l[i] = l[i], l[i - 1]
                sorted = False

def quick_sort_select_pivot(l, start, end):
    return start

def quick_sort_partition(l, start, end):
    pivot = quick_sort_select_pivot(l, start, end)

    # swap pivot to start
    l[pivot], l[start] = l[start], l[pivot]

    # track division between highs and lows
    hi_part = start + 1
    for i in range(start + 1, end + 1):
        if l[i] < l[pivot]:
            l[hi_part], l[i] = l[i], l[hi_part]
            hi_part += 1

    # swap pivot with last element of lows
    l[start], l[hi_part - 1] = l[hi_part - 1], l[start]

    return hi_part - 1


# Select a pivot
# Partition into less than or equal and greater than
#   Trick is to track where the divide is and only swap when less than pivot
#   so that there is always a partition and we grow it each step
# Call recursively on two parts
def quick_sort_recursive(l, start=None, end=None):
    if start is None:
        start = 0
        end = len(l) - 1

    if start < end:
        p = quick_sort_partition(l, start, end)
        quick_sort_recursive(l, start, p - 1)
        quick_sort_recursive(l, p + 1, end)

def quick_sort_iterative(l):
    stack = [(0, len(l) - 1)]

    while stack:
        start, end = stack.pop()
        if (start < end):
            p = quick_sort_partition(l, start, end)
            stack.append((start, p - 1))
            stack.append((p + 1, end))

def merge_sort_merge(left, right):
    left_idx = 0
    right_idx = 0
    out = []
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            out.append(left[left_idx])
            left_idx += 1
        else:
            out.append(right[right_idx])
            right_idx += 1

    while left_idx < len(left):
        out.append(left[left_idx])
        left_idx += 1

    while right_idx < len(right):
        out.append(right[right_idx])
        right_idx += 1

    return out

def merge_sort_recursive_(l, start=None, end=None):
    if start is None:
        start = 0
        end = len(l) - 1

    if start < end:
        mid = (start + end) // 2
        left = merge_sort_recursive_(l, start, mid)
        right = merge_sort_recursive_(l, mid + 1, end)
        return merge_sort_merge(left, right)

    if start == end:
        return [l[start]]

    return []

# Split in 2, sort both, then merge into a new list
def merge_sort_recursive(l):
    sorted = merge_sort_recursive_(l)
    l.clear()
    l.extend(sorted)

def merge_sort_iterative(l):
    SPLIT = 0
    MERGE = 1

    call_stack = []
    list_stack = []

    call_stack.append((SPLIT, 0, len(l) - 1))
    while call_stack:
        op, start, end = call_stack.pop()
        if op == SPLIT:
            if start < end:
                mid = (start + end) // 2
                call_stack.append((MERGE, -1, -1))
                call_stack.append((SPLIT, mid + 1, end))
                call_stack.append((SPLIT, start, mid))
            elif start == end:
                list_stack.append([l[start]])
            else:
                list_stack.append([])
        if op == MERGE:
            left = list_stack.pop()
            right = list_stack.pop()
            list_stack.append(merge_sort_merge(left, right))

    l.clear()
    l.extend(list_stack[0])

def counting_sort(l, k=10):
    count = [0] * k
    for i in l:
        count[i] += 1
    i = 0
    for j in range(len(count)):
        for _ in range(count[j]):
            l[i] = j
            i += 1
