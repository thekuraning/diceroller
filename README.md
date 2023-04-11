# diceroller
A basic python project to generate dice rolls for TTRPGs.

v0.1

Currently includes two files:

DiceModule.py: a separately created module that handles the dice type (coin, d4, d6, d8, d10, d12, and d20)
as well as the value range for each to produce. Required for DiceRollerMain.

DiceRollerMain.py: the main script, which allows you to select which type of dice and how many of them to roll.
You can also include a modifier number to increase or decrease the total roll value. The script will return a list
of the individual values rolled, and will calculate the total value both with and without the modifier.

Future improvements will include:
- GUI
- Multiple dice types in a single roll
- Optional calculation for a critical success (double the rolled value)
- Dice logger to keep track of all rolls while using the script.
