"""Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
import string
def get_score(word,position):
    score=0
    for char in word:
        
        score=score+ord(char.lower())-97+1
        position
    return score*position

name_list=[]
with open ("p022_names.txt","r") as names_file:
    for line in names_file:
        line=line.replace("\"","")
        name_list=line.split(",")

sum_of_scores=0

for i,name in enumerate(sorted(name_list)):
    score = get_score(name,i+1)
    # if name =="COLIN":print(i+1,name,score)
    sum_of_scores=sum_of_scores+score
print(f"sum of all socres:{sum_of_scores}")


    