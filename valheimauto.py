import pyautogui
import time

screenWidth, screenHeight = pyautogui.size()
print('what skill would you like to train')
print('j = jump')
print('r = run')
print('s = sneak')
print('a = attack')
print('sw = swim')
print('please not their is currently no way ')


train = input()

print('now please put the number of loops requested')

loop = input()

pyautogui.click(screenWidth / 2, screenHeight / 2)


def thedict(train):
    switcher = {
    j: jump(loop),
    'r' : run(loop),
    's' : sneak(loop),
    'a' : attack(loop),
    'sw' : swim(loop)
}

time.sleep(1)
pyautogui.press('3')
time.sleep(1)

def jump(loop):
    for x in range(loop):
        time.sleep(2.5)
        pyautogui.press("space")

def run(loop):
    for x in range(loop):
        time.sleep(2.5)
        pyautogui.keyDown("shift")
        pyautogui.keyDown("w")
        time.sleep(2)
        pyautogui.keyUp("w")
        pyautogui.keyUp("shift")
        time.sleep(5)

def sneak(loop):
    for x in range(loop):
        time.sleep(2.5)
        pyautogui.keyDown("ctrl")
        pyautogui.keyDown("w")
        time.sleep(2)
        pyautogui.keyUp("w")
        pyautogui.keyUp("ctrl")
        time.sleep(5)

def attack(loop):
    for x in range(loop):
        time.sleep(2.2)
        pyautogui.click(screenWidth / 2, screenHeight / 2)


