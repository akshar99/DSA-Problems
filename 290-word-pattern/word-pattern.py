class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_map = {}
        s_map = {}
        p_list = list(pattern)
        s_list = s.split()
        if len(p_list) != len(s_list):
            return False
        for s_ele, p_ele in zip(s_list, p_list):
            if p_ele in p_map:
                if p_map[p_ele] != s_ele:
                    return False
            else:
                p_map[p_ele] = s_ele

            if s_ele in s_map:
                if s_map[s_ele] != p_ele:
                    return False
            else:
                s_map[s_ele] = p_ele

        return True