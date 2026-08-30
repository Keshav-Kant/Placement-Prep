class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        if len(s) < 2:
            return False
        for i in s:
            if i == "(" or i == "{" or i == "[":
                l.append(i)
                # print(*l)
            elif i == ")":
                if not l or l.pop() != "(":
                    return False
            elif i == "}":
                if not l or l.pop() != "{":
                    return False
            elif i == "]":
                if not l or l.pop() != "[":
                    return False
        return len(l) == 0

        