import random
opt=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
m=0
n=0
while m==0:
    i = random.choices(opt, k=25)
    n=n+1
    if i[0] == 'c' and i[1] == 'o' and i[2] == 'm' and i[3] == 'p'and i[4] == 'u' and i[5] == 't'and i[6] == 'e' and i[7] == 'r' and i[8] == 'i' and i[9] == 's' and i[10] == 'g' and i[11] == 'r' and i[12] == 'e' and i[13] == 't' and i[14] == 'o' and i[15] == 'p' and i[16] == 'q' and i[17] == 'r' and i[18] == 's' and i[19] == 't' and i[20] == 'u' and i[21] == 'v' and i[22] == 'w' and i[23] == 'x' and i[24] == 'y':
        print('found')
        m=1