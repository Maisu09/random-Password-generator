#Password generator


import random
nr_litere=input('How many characters ?')
nr_numbers=input('How many numbers?')
nr_simbol=input('How many simbols ?')
letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number=['0','1','2','3','4','5','6','7','8','9']
simbol=['!','#','$','%','&','(',')','*','+']
s=[]
for nr in range(int(nr_litere)):
    s.append(letter[random.randint(0,len(letter)-1)])
# print(s)
for nr in range(int(nr_numbers)):
    s.append(number[random.randint(0,len(number)-1)])
# print(s)
for nr in range(int(nr_simbol)):
    s.append(simbol[random.randint(0,len(simbol)-1)])
print(''.join(random.sample(s,len(s))))
