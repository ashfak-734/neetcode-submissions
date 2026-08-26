class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        my_list = [[p,s] for p,s in zip(position,speed)]

        for p,s in sorted(my_list)[::-1]:
            t = float((target-p)/s)

            if not stack:
               stack.append(t)
            else:
               if t > stack[-1]:
                  stack.append(t)
                  
        return len(stack)

        