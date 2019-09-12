# 逐位相加

digits = [9,9,9]
plus_num = 1

for i in range(len(digits)-1,-1,-1):
    
    digits[i] += 1
    plus_num = digits[i] // 10
    digits[i] = digits[i] % 10
    
    if plus_num == 0:
        break

if plus_num > 0 :
    digits = [1] + digits
print (digits)