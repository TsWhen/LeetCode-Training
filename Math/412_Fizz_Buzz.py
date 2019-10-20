class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        answer = [0] * n
        
        pos = 2
        while pos < n:
            answer[pos] -= 1
            pos += 3
        
        pos = 4
        while pos < n:
            answer[pos] -= 2
            pos += 5
        
        for i in range(n):
            
            if answer[i] == 0:
                answer[i] = str(i+1)
            elif answer[i] == -1:
                answer[i] = "Fizz"
            elif answer[i] == -2:
                answer[i] = "Buzz"
            elif answer[i] == -3:
                answer[i] = "FizzBuzz"
                
        return answer