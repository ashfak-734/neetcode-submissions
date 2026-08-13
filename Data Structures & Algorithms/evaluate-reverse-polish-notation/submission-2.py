class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        hashh = {"+","*","-","/"}
        stack = []

        for i in tokens:
            if i not in hashh:
                stack.append(int(i))
                continue

            b = stack.pop()
            a = stack.pop()
            

            if i == "+":
                result = a+b
            elif i == "-":
                result = a-b
            elif i == "*":
                result = a*b
            elif i == "/":
                result = int(a/b)
            
            stack.append(result)

        return stack[0]
