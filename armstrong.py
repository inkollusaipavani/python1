for n in range(360,380):
  temp=n
  sum=0
  while temp>0:
        digit=temp%10
        sum=sum+digit**3
        temp=temp//10
        if sum==n:
            print (n)
