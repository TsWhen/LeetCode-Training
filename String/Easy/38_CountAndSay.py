# 循环迭代
class Solution:
    def countAndSay(self, n: int) -> str:
        output_str = "1"
        for i in range(1,n):
            temp_char = output_str[0]
            temp_num = 1
            temp_output = ""
            for i in range(1,len(output_str)):

                if output_str[i] != temp_char:
                    temp_output += str(temp_num) + temp_char
                    temp_char = output_str[i]
                    temp_num = 1
                else:
                    temp_num += 1

            output_str = temp_output + str(temp_num) + output_str[len(output_str) - 1]

        return output_str