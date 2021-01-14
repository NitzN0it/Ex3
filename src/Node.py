class Node:
    def __init__(self, k=0, i=0, t=0, loc=(0, 0, 0), w=0):
        self.key = k
        self.info = i
        self.tag = t
        self.location = loc
        self.weight = w

    def setKey(self, k):
        self.key = k

    def getKey(self) -> int:
        return self.key

    def setInfo(self, i):
        self.info = i

    def getInfo(self) -> int:
        return self.info

    def setTag(self, t):
        self.tag = t

    def getTag(self) -> int:
        return self.tag

    def setWeight(self, w):
        self.weight = w

    def getWeight(self) -> float:
        return self.weight

    def setLocation(self, loc):
        self.location = loc

    def getLocation(self) -> tuple:
        return self.location
