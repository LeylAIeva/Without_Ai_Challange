import random
import json
choosen_word = []
point = 4
value=True
with open("bck/words.json","r") as file:
    data = json.load(file)
i = random.randrange(1,4)
choosen_word.append(data[i]["word"])
choosen_word_str = choosen_word[0]
origin_dict={}
value_of_letter=0
for  letter in choosen_word_str:
      if origin_dict is None:
            origin_dict.update({letter:0})
            
      else:
            value_of_letter+=1
            
            origin_dict.update({letter:value_of_letter})
            
print(origin_dict)


print(choosen_word)


count = len(choosen_word_str)
"""print(count)"""
while point>0:
        
        add_word = list(input("Add word:  "))
        mod_word="".join(add_word).lower()
        true_letters={add_word[x]:True if add_word[x] in choosen_word_str else add_word[x] for x in range(len(add_word)) }
        
        
        
                    
        
        
      
        if len(mod_word) == count:
              
            if mod_word in choosen_word_str:
                  print("Congrats")
                  break

            else:
                  for key in true_letters:
                        if true_letters[key]==True:
                              pass
                  point-=1
        else: 
              print("oh no")

              
              
        print(point)
        print(f"true letters {true_letters}")
        """print(f"choosen_word {choosen_word}")
        
        print(f"mod word {mod_word}")
        
        
        print(count)
        """
        






