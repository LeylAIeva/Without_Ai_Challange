import random
import json
choosen_word = []
point = 4
value=True
with open("bck/words.json","r") as file:
    data = json.load(file)
i = random.randrange(1,3)
choosen_word.append(data[i]["word"])
choosen_word = str(choosen_word)

print(choosen_word)

check = []

while point>0:
        add_word = list(input("Add word:  "))
        true_letters=[add_word[x].upper() if add_word[x] in choosen_word else add_word[x] for x in range(len(add_word)) ]
        print(true_letters)
        str_true_letters="".join(true_letters).lower()
        check.append(str_true_letters)
        if check == choosen_word:
              print("Congrats")
              break
        
        else:
              
              
              point-=1
              
        print(point)
        print(check)
        print(choosen_word)
       
        
        
              





