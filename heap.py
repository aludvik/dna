class BinaryMaxHeap:
    def __init__(self):
        self.__heap = []

    def top(self):
        return self.__heap[0]

    def insert(self, data):
        i = len(self.__heap)
        self.__heap.append(data)

        while i != 0 and self.__heap[i] > self.__heap[self.__parent(i)]:
            self.__swap(i, self.__parent(i))
            i = self.__parent(i)

    def extract(self):
        data = self.__heap[0]
        last = self.__heap.pop()
        if self.__heap:
            self.__heap[0] = last

        i = 0
        while (
            self.__has_left_child_and_smaller(i)
            or self.__has_right_child_and_smaller(i)
        ):
            largest = -1
            if self.__has_left_child_and_smaller(i):
                largest = self.__left_child(i)

            if self.__has_right_child_and_smaller(i):
                if largest != -1:
                    if self.__heap[self.__right_child(i)] > self.__heap[largest]:
                        largest = self.__right_child(i)
                else:
                    largest = self.__right_child(i)

            assert(largest != -1)
            self.__swap(i, largest)
            i = largest

        return data

    @staticmethod
    def __left_child(i):
        return 2 * i + 1

    @staticmethod
    def __right_child(i):
        return 2 * i + 2

    @staticmethod
    def __parent(i):
        return (i - 1) // 2

    def __swap(self, i, j):
        self.__heap[i], self.__heap[j] = self.__heap[j], self.__heap[i]

    def __has_left_child(self, i):
        return self.__left_child(i) >= len(self.__heap)

    def __has_right_child(self, i):
        return self.__right_child(i) >= len(self.__heap)

    def __has_left_child_and_smaller(self, i):
        if self.__has_left_child(i):
            return False
        return self.__heap[i] < self.__heap[self.__left_child(i)]

    def __has_right_child_and_smaller(self, i):
        if self.__has_right_child(i):
            return False
        return self.__heap[i] < self.__heap[self.__right_child(i)]
