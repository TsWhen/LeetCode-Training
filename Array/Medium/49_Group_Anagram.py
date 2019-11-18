# 将每个单词内的字符按字典序排好，然后作为key，用字典存储即可
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res_dict = {}
        for str in strs:
            
            temp_str = str
            temp_str = "".join(sorted(temp_str))
            
            if temp_str in res_dict:
                
                res_dict[temp_str].append(str)
            
            else:
                
                res_dict[temp_str] = [str]
        
        res_list = []
        for k,v in res_dict.items():
            res_list.append(v)
        
        return res_list