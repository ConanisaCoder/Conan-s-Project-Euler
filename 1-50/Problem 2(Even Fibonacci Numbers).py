a,b = 1,1
count = 0
while a<4000000: 
    if a % 2 == 0:
        count += a
    a,b = b, a+b
print(count)