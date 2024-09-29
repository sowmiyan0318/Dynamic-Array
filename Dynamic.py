class DynamicArray:
    def __init__(self, initial_size=1):
        self.array = [None] * initial_size
        self.size = 0
        self.capacity = initial_size

    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def add(self, element):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.size] = element
        self.size += 1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.array[index]

    def __str__(self):
        return str(self.array[:self.size])

# Example usage:
arr = DynamicArray()
arr.add(10)
arr.add(20)
arr.add(30)
print(arr)  # Output: [10, 20, 30]
print(arr.get(1))  # Output: 20
