class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [0] * self.capacity
        self.length = 0
    
    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if i >= 0 and i < self.length:
            self.arr[i] = n
        

    def pushback(self, n: int) -> None:
        if self.capacity == self.length:
            self.resize()

        self.arr[self.length] = n
        self.length += 1


    def popback(self) -> int:
        last_element = float("-inf")
        if self.length > 0:
            last_element = self.arr[self.length - 1]
            self.arr[self.length - 1 ] = 0
            self.length -= 1
        return last_element

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        arr = [0] * self.capacity
        for idx in range(self.length):
            arr[idx] = self.arr[idx]
        self.arr = arr

    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity
