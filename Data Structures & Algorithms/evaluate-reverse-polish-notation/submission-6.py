class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
      ops = {"+","-","*","/"}
      stack = []
      result = 0 
      a = 0
      b = 0

      for c in tokens:
         if c not in ops:
            stack.append(int(c))
         else:
            b = stack.pop()
            a = stack.pop()
         
            if c == "+":
               stack.append(a+b)
            elif c == "-":
               stack.append(a-b)
            elif c == "*":
               stack.append(a*b)
            else:
               stack.append(int(a/b))

      return stack[0]
         



        