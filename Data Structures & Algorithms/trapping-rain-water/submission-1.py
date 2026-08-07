class Solution:
    def trap(self, height: List[int]) -> int:

        max_wall_l = [0]*len(height)
        max_wall_r = [0]*len(height)
        
        l_max_wall_seen = 0  # 
        r_max_wall_seen = 0

        for i in range(len(height)):
            j = -i-1

            max_wall_l[i] = l_max_wall_seen 
            max_wall_r[j] = r_max_wall_seen

            l_max_wall_seen = max(l_max_wall_seen,height[i]) 
            r_max_wall_seen = max(r_max_wall_seen,height[j])

        result = 0

        for i in range(len(height)):
            trapped_water = min(max_wall_l[i], max_wall_r[i]) - height[i]

            if trapped_water > 0:
                result += trapped_water

        return result


    
#[4,2,3]
#[0,4,4]
#[3,3,0]            




            

