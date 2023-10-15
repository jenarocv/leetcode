class Solution:
    def calPoints(self, operations):

        stack = []

        for op in operations:
            if op == "+":
                stack.append(stack[len(stack) - 1] + stack[-2])
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))

        #        result = 0
        #        for element in stack:
        #            result += element

        result = sum(stack)
        return result
