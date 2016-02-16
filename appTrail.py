personalMessage = ""
firstLink = False
    
with open ("Sample.txt", "r") as sample:
    wholeMessage = sample.read().replace('\n', '')
	
for x in range (0, len(wholeMessage)):
    if wholeMessage[x] == "-":
        personalMessage += "\n\n"
        for y in range (x, len(wholeMessage)):
            if wholeMessage[y] == "h" and wholeMessage[y + 1] == "t":
                if firstLink == True:
                    while(wholeMessage[y] != " "):
                        personalMessage += wholeMessage[y]
                        y += 1
                    break
                else:
                    firstLink = True
        break
    else:
        personalMessage += wholeMessage[x]

with open ("PersonalMessage.txt", "a") as personal:
    personal.write(personalMessage)
