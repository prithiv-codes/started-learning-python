import random
opt = 'abcdefghijklmnopqrstuvwxyz '
target = 'computer is the best todoay but love doing it since this is of computer'
m=0
n=0
l=[]
i=random.choice(opt)
while m!=len(target):
    n+=1
    if i == target[m]:
        l.append(i[0])
        m+=1
        i=random.choice(opt)
        print(''.join(l),n)
    else:
        i=random.choice(opt)