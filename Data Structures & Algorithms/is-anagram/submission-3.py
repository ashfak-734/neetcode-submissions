class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dic_s = {}
        my_dic_t = {}
        alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j",            "k","l","m","n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in my_dic_s:
              my_dic_s[s[i]] = 1
            else:
               my_dic_s[s[i]] += 1

        for i in range(len(t)):
            if t[i] not in my_dic_t:
              my_dic_t[t[i]] = 1
            else:
               my_dic_t[t[i]] += 1
  
        """
        {b:2,  
         c:2}

        {c:3,
         b:1}   
        """   
        for i in alphabet:
            if my_dic_s.get(i , 0) != my_dic_t.get(i , 0):
                return False
        return True 

    
        