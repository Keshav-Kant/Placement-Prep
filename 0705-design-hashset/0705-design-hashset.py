class MyHashSet:

    def __init__(self):
        self.hashDict = []
        

    def add(self, key: int) -> None:
        if key not in self.hashDict:
            self.hashDict.append(key)
        

    def remove(self, key: int) -> None:
        if key in self.hashDict:
            self.hashDict.remove(key)


    def contains(self, key: int) -> bool:
        return key in self.hashDict

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)