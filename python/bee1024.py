casos = int(input())

for i in range(casos):
    texto = input()
    newString = ""
    for j in texto:
        if j.isalpha():
            newString = newString + chr(ord(j) + 3)
        else:
            newString = newString + j
    
    newString2 = newString[::-1]
    newString3 = newString2[:len(newString2) //2]
    newString5 = newString2[len(newString2) //2 :]
    newString4 = ''
    for k in newString5:
        newString4 = newString4 + chr(ord(k) -1)
    stringFinal = newString3 + newString4
    print(stringFinal)