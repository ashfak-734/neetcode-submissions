class Solution:
    def trap(self, height: List[int]) -> int:
        l_wall_arr = [0]*len(height)
        r_wall_arr = [0]*len(height)

        l_wall = 0
        r_wall = 0
        
        for i in range(len(height)):
            j = -i-1

            l_wall_arr[i] = l_wall
            r_wall_arr[j] = r_wall

            l_wall = max(height[i],l_wall) 
            r_wall = max(height[j],r_wall)

        result = 0

        for i in range(len(height)):
            water_trapped = min(l_wall_arr[i],r_wall_arr[i]) - height[i]

            if water_trapped > 0:
                result += water_trapped

        return result





       




            

