#!/usr/bin/python

import sys

class CircularBuffer(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.size = k
        self.start = 0
        self.len = 0
        self.buf = [0] * k
        

    def enQueue(self, len, buf_in):
        """
        Insert elements into the circular queue. Return the number of elements successfully inserted.
        :type len: int
        :type buf_in: int[]
        :rtype: int
        """
        write_len = min(len, self.size - self.len)

        end = (self.start + self.len) % self.size
        first_len = min(write_len, self.size - end)
        self.buf[end:end+first_len] = buf_in[0:first_len]

        self.buf[0:write_len-first_len] = buf_in[first_len:write_len]
        self.len += write_len
        
        print('end of enQueue --')
        print(self.buf)

        return write_len
        

    def deQueue(self, len, buf_out):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        read_len = min(len, self.len);
        
        first_len = min(read_len, self.size - self.start);
        buf_out[0:first_len] = self.buf[self.start:self.start+first_len]

        buf_out[first_len:read_len] = self.buf[0:read_len-first_len]
        self.start = (self.start + read_len) % self.size
        self.len -= read_len

        return read_len

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        
        return self.buf[self.start]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        
        rear = (self.start + self.len -1) % self.size
        
        return self.buf[rear]
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return bool(self.len == 0)

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return bool(self.len == self.size)
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()


def main():
    print("hello world!")

    cb = CircularBuffer(20)

    buf_in = [1,3,6,7,23,27,34,38,44,48,52,57,61,68,70,75,88,92,93,99]
    buf_golden = [7,23,27,34,38,44,48,52,57,61,68,70,75,88,92,93,99,1,3,6]
    buf_out = [0] * 20

    ret = cb.enQueue(5, buf_in)
    print('write returns ' + str(ret))
    ret = cb.deQueue(3, buf_out)
    print('read returns ' + str(ret))

    print(buf_out)
#    for (byte b : buf_out)
#      System.out.print(b + " ");
#    System.out.println();

    cb.enQueue(15, buf_in[5:20])
    cb.enQueue(3, buf_in);
    cb.deQueue(20, buf_out);

    print(buf_out)
#    for (byte b : buf_out)
#      System.out.print(b + " ");
#    System.out.println();


if __name__ == "__main__":
    main()





