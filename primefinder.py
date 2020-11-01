
print("")

n = int(input())
p = [2]
d = 0

for i in range(3,n+1):
    d = 0
    for j in range(2,i):
        if i%j == 0:
            d+=1
    if d == 0:
        p.append(i)

print("Prime Numbers: ")

for x in p:
    print(x)

print("There are ", len(p), " prime numbers till ", n)