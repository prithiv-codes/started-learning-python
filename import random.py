import random
opt=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
m=0
n=0
while m==0:
    i = random.choices(opt, k=25)
    n=n+1
    if i=='computeristhebesttodoay':
        m=1
        print('found')
        print(n)
        print(i)