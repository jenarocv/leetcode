class Solution:
    def isValid(self, s):
        stack = []
        pairs = {")": "(", "}": "{", "]": "[", }

        for c in s:
            if c in pairs:
                if stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True


print(Solution().isValid("()[]{}"))
print(Solution().isValid("(}"))
