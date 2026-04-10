
def possible_string(words,games,verbs):
    s1=""
    for i in words:
        for j in verbs:
            for k in games:
                s1+=i+" "+j+" "+k+"\n"
                
    print(s1)
                

words=["I","You"]
games=["Volleyball","Cricket","Badminton"]
verbs=["See","loves","play"]
possible_string(words,games,verbs)