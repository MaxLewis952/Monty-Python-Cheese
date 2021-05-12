print ("*** Welcome to H. Wensleydale ***")
lines = ["Would you like some cheese?","Certainly Sir","Red Leicester?", "I'm afraid we are fresh out of red leicester Sir","Tilset?","Never at the end of the week Sir","Red Winsor?","I'm afraid the van broke down","Camembert?","We do have some camembert Sir\nIts rather runny Sir\nWell as a matter of fact it's very runny Sir\nAh\nThe cat's eaten it","Gouda?","No Sir","Edame?","No"]
count = 0
while count < len (lines):
    print (lines [count])
    answer = input ("(Y)es or (N)o?\n")
    answer = answer.lower ()
    if answer == "y":
        print (lines[count + 1])
        count = count + 2
    else:
        count = len (lines) + 1
        print ("That's good, we haven't got any")
