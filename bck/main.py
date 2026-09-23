import random
import json
choosen_word = []
point = 4
value=True
with open("bck/words.json","r") as file:
    data = json.load(file)
i = random.randrange(1,4)
choosen_word.append(data[i]["word"])
choosen_word = str(choosen_word)

print(choosen_word)



while point>0:
        add_word = list(input("Add word:  "))
        mod_word="".join(add_word).lower()
        true_letters=[add_word[x].upper() if add_word[x] in choosen_word else add_word[x] for x in range(len(add_word)) ]
        print(f"true letters {true_letters}")
        str_true_letters="".join(true_letters).lower()
        
        print(f"str true letters{str_true_letters}")
        if mod_word in choosen_word:
              print("Congrats")
              break
              
        else:
              
              
              point-=1
              check=[]
              
        print(point)
        print(f"check {check}")
        print(f"choosen_word {choosen_word}")
        print(f"add_word{add_word}")
        print(f"mod word {mod_word}")
        
       
        
        






