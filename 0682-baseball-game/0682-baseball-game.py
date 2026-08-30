from collections import deque

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []
        for i in operations:
            if i == "C":
                a = s.pop()
                print(f"pop {a}: ",s)

            elif i == "+":
                a = s[-1]
                b = s[-2]
                s.append(a+b)
                print(f"adding {a}+{b}: ",s)
            elif i == "D":
                a = s[-1]*2
                s.append(a)
                print(f"adding {a}: ",s)
            else:
                s.append(int(i))
                print(s)
        print(s)
        return sum(s)
