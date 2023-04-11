import DiceModule

# This section defines empty variables for the number of dice rolled and the
# type of dice

rollDice = True
reroll = 1
diceTotal = []

# This section takes user input to determine what type and number of dice to roll
# within a loop until the user decides they're finished.

while rollDice == True:
    diceNum = int(input("How many dice are you rolling?\n"))
    diceType = int(input(f"And what kind of dice do you need? (2,4,6,8,10,12,20)\n{diceNum}D"))
    modifier = int(input("What are your roll modifiers?\n"))
    print("Let's roll some dice!")
    for num in range(0, diceNum):
        if diceType == 2:
            DiceModule.coinflip()
        elif diceType == 4:
            diceTotal.append(DiceModule.dfour())
        elif diceType == 6:
            diceTotal.append(DiceModule.dsix())
        elif diceType == 8:
            diceTotal.append(DiceModule.deight())
        elif diceType == 10:
            diceTotal.append(DiceModule.dten())
        elif diceType == 12:
            diceTotal.append(DiceModule.dtwelve())
        elif diceType == 20:
            diceTotal.append(DiceModule.dtwenty())
        else:
            print("I don't have that kind of dice. Please enter a valid type.")
            break
    print(f"Your dice scatter across the table with a clikety-clack.\n{diceTotal}")
    print(f"Your total before modifiers is {sum(diceTotal)}.")
    print(f"With modifiers, your total is {sum(diceTotal) + modifier}.")
    diceTotal = []

    reroll = int(input("Would you like to roll again?\n0=no\n1=yes\n"))
    if reroll == 0:
        rollDice = False




