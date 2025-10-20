a=int(input())
b=int(input())
a>0 and a<9999
b>0 and b<9999
if a>9999:
    a=a-9999
if b>9999:
    b=b-9999
n=b-a #использованно
c=n-300 #не фиксированное кол-во
if c>300 and c<=600:
    price=c*0.06
if c>600 and c<=800:
    price=c*0.04
if c>800:
    price=c*0.025
total_price=21+price
print(f'{total_price:.2f}')