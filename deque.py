class Deque:
    class __Node:
        def __init__(self, data):
            self.prev = None
            self.next = None
            self.data = data

    def __init__(self):
        self.__front = None
        self.__back = None
        self.__size = 0

    def push_front(self, data):
        n = Deque.__Node(data)
        if self.__front is None:
            self.__back = n
        else:
            n.next = self.__front
            self.__front.prev = n
        self.__front = n
        self.__size += 1

    def pop_front(self):
        if self.__front is None:
            return None
        n = self.__front
        self.__size -= 1

        self.__front = n.next
        if self.__front is None:
            self.__back = None
        else:
            self.__front.prev = None

        return n.data

    def peak_front(self):
        if self.__front is None:
            return None
        return self.__front.data

    def push_back(self, data):
        n = Deque.__Node(data)
        if self.__back is None:
            self.__front = n
        else:
            n.prev = self.__back
            self.__back.next = n
        self.__back = n
        self.__size += 1

    def pop_back(self):
        if self.__back is None:
            return None
        n = self.__back
        self.__size -= 1

        self.__back = n.prev
        if self.__back is None:
            self.__front = None
        else:
            self.__back.next = None

        return n.data

    def peak_back(self):
        if self.__back is None:
            return None
        return self.__back.data

    def size(self):
        return self.__size
