class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        for s_ele, t_ele in zip(s, t):
            if s_ele in s_to_t:
                if s_to_t[s_ele] != t_ele:
                    return False
            else:
                s_to_t[s_ele] = t_ele
        
            if t_ele in t_to_s:
                if t_to_s[t_ele] != s_ele:
                    return False
            else:
                t_to_s[t_ele] = s_ele

        return True
