#Hangman Game
import random
word_list=['ardvark', 'baboon', 'camel']
x=random.randint(0,len(word_list)-1)
lives=5
word=list(word_list[x])
contor_litere_corecte=0
linii=list()
for i in range(len(word)):
    linii.append('_')
print(linii)
while lives!=0 and contor_litere_corecte<len(word):
    ok=0
    key=input('what is the letter ?').lower()
    poz=0    
    for letter in word:
        if letter == key:
            #print('right')
            ok=1
            contor_litere_corecte+=1
            linii.insert(poz,letter)
            linii.pop(poz+1)
        # else:
        #     print('wrong')
        poz+=1
    print(linii)    
    if ok==0:
        lives-=1
        print(lives)
if contor_litere_corecte==len(word):
    print('you won')
else:
    print('you lost') 
    
    


