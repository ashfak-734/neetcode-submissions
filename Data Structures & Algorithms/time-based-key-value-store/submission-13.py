class TimeMap:

    def __init__(self):
        self.my_dic = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.my_dic:
            self.my_dic[key] = []

        self.my_dic[key].append((value,timestamp))
        
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.my_dic:
            lst = self.my_dic[key]
            l = 0
            r = len(lst)-1

            while l<=r:
                m = (l+r)//2

                if lst[m][1] == timestamp:
                    return lst[m][0]
                elif lst[m][1] < timestamp:
                    l = m+1
                else:
                    r = m-1

            if r >= 0:
              return lst[r][0]

        return ""

            
           





        

            
        
