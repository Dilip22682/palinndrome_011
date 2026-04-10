# Pangram = All alphabet present in sentance at least once.
s1="Pack my box with five dozen of liquor jugs"
s2="The quick brown fox jumped over the lazy dogs"
char1=set()

for i in s1:
    if i==" ":
        continue
    elif i>="A" and i<="Z":
        char1.add(ord(i.lower()))
    elif i>="a" and i<="z":
        # print(i, end=" ")
        char1.add(ord(i))
    
print(char1, end=" ")
print()
print(len(char1), end=" ")
print()       
# print("\n",len(char1))
for i in char1:
    print(chr(i), end=" ")
if len(char1)==26:
    print("\n","String is Paragram")
else:
    print("\n","String is not Paragram")
        

        
        