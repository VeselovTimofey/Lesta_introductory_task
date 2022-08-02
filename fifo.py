from collections import deque


class FifoList(object):
    """
    The class of fifo list.

    Then called, it has fifo list and two method: put_in and put_out.
    """
    def __init__(self):
        self.fifo = []

    def put_in(self, element):
        """ Add element to fifo list. """
        self.fifo.append(element)

    def put_out(self):
        """ Return first element from fifo list. """
        return self.fifo.pop(0)


class FifoDeque(object):
    """
    The interface of deque.

    Then called, it has deque and two method: put_in and put_out.
    """
    def __init__(self):
        self.fifo = deque()

    def put_in(self, element):
        """ Add element to deque at the end. """
        self.fifo.append(element)

    def put_out(self):
        """ Return first element from deque. """
        return self.fifo.popleft()


if __name__ == "__main__":
    fifo_list = FifoList()
    fifo_deque = FifoDeque()
    for fifo in (fifo_list, fifo_deque):
        fifo.put_in(34)
        fifo.put_in("some")
        fifo.put_in(80085)
        print(fifo.put_out())
        print(fifo.put_out())
        fifo.put_in("number")
        print(fifo.put_out())
        print(fifo.put_out())
