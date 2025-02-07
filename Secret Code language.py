import random
choice=input("Do you want to encode(en) or decode(dec)?: ").lower()
if(choice=="en"):
    message=input("Enter your message: ")
    l=message.split(" ")
    for index,i in enumerate(l):
        copy=i
        if(len(i)>=3):
            str=i[1:]+i[0]
            for j in range(0,3):
                c=random.randint(0,len(copy)-1)
                str=copy[c]+str+copy[c]
            l.pop(index)
            l.insert(index,str)
        else:
            str=i[::-1]
            l.pop(index)
            l.insert(index,str)

    encoded=" ".join(l)
    print(encoded)
elif(choice=="dec"):
    encoded=input("Enter your message: ")
    l1=encoded.split(" ")
    for index,i in enumerate(l1):
        if len(i)>=3:
            en=i[-4]+i[3:-4]
            l1.pop(index)
            l1.insert(index,en)
        else:
            en=i[::-1]
            l1.pop(index)
            l1.insert(index,en)
    decoded=" ".join(l1)
    print(decoded)
else:
    print("Invalid input")