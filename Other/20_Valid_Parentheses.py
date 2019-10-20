class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_bracket = ['(','{','[']
        bracket_dict = {')':'(','}':'{',']':'['}
        bracket_stack = []
        
        for bracket in s:
            if bracket in left_bracket:
                bracket_stack.append(bracket)
            elif len(bracket_stack) == 0:
                return False
            elif bracket_stack.pop() != bracket_dict[bracket]:
                return False
        
        if len(bracket_stack) != 0:
            return False
        
        return True