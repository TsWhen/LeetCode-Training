class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        pascal_list = []
        
        for i in range(numRows):
            
            row_list = [1] * (i+1)
            
            for j in range(1,i):
                row_list[j] = pascal_list[i-1][j-1] + pascal_list[i-1][j]
            
            pascal_list.append(row_list)
            
        return pascal_list
        