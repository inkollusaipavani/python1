num=int(raw_input())
rev=0
while(num>0):
    remainder=num%10
    rev=rev*10+remainder
    num=num/10
print rev    
