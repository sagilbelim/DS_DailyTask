l=[]

def undo(l):
    u=l.pop()
    print("removed last character=",u)
    str="".join(l)
    print("after removing last character=",str)
while str!="no":
    str=input("Enter a character=")
    if str!="no":
        l.append(str)

print(l)
undo(l)