from pynput.keyboard import Key, Controller as keyboard_controller
from time import sleep
import random, re, os

os.system("cls")
keyboard = keyboard_controller()
numPara = int(input("\nEnter number of paragraphs: "))
inputDelay = float(input("\nEnter input delay (~0.2): "))
farKeys = ["q", "w", "t", "y", "u", "i", "o", "p", "g", "j", "h", "k", "l", "v", "c", "b", "m", "n"]
keyboardKeys = [["q","w","e","r","t","y","u","i","o","p", " "],
["a","s","d","f","g","h","j","k","l", " "],
["z","x","c","v","b","n","m", " "]]
paragraphs = []


for i in range(numPara):
    paragraphs.append(input(f"\nEnter Paragraph {i}: "))

print("\n-------------------")
print("|Writing in 5 secs|")
print("-------------------")
sleep(1)
print("|Writing in 4 secs|")
print("-------------------")
sleep(1)
print("|Writing in 3 secs|")
print("-------------------")
sleep(1)
print("|Writing in 2 secs|")
print("-------------------")
sleep(1)
print("|Writing in 1 secs|")
print("-------------------")
sleep(1)

chance2 = 0

for i in range(numPara):
    for j in range(len(paragraphs[i])):
        if paragraphs[i][j] in farKeys or not bool(re.match('^[a-zA-Z0-9]*$', paragraphs[i][j])):
            chance0 = round(random.uniform(0, 1), 10)
            if chance0 <= chance2:
                keyboard.type(random.choice(random.choice(random.choice(keyboardKeys))))
                sleep(round(random.uniform(0, inputDelay), 3) + round(random.uniform(0, inputDelay), 3) * 1.5)
            else:
                keyboard.type(paragraphs[i][j])
                sleep(round(random.uniform(0, inputDelay), 3) + round(random.uniform(0, inputDelay), 3) * 1.5)
        else:
            chance1 = round(random.uniform(0, 1), 10)
            if chance1 <= chance2:
                keyboard.type(random.choice(random.choice(random.choice(keyboardKeys))))
                sleep(round(random.uniform(0, inputDelay), 3))
            elif chance1 >= chance2:
                keyboard.type(paragraphs[i][j])
                sleep(round(random.uniform(0, inputDelay), 3))
    keyboard.press(Key.enter)

print("\nDone!")
os.system("cls")
os.system("py main.py")