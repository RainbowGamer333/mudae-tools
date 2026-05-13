from time import sleep
import pyautogui as auto
from tqdm import tqdm

def write(message):
    auto.write(message, interval=0.1)
    auto.press("enter")
    
def typeChat(key):
    auto.press(key)
    auto.press("enter")


input_mode = True


roll = input("Time to roll ? (y/n) : ")
while roll.lower() == 'y':
    for i in range(5,0,-1):
        print(f"Executing in {i}...")
        sleep(1)
    
    write('/rollsutil usestack 20')
    sleep(1)
    for j in tqdm(range(20)):
        sleep(0.5)
        if j == 0:
            write('/ha ')
        else:
            typeChat('up')
    
    if input_mode:    
        roll = input("Rolls complete. Roll again ? (y/n) : ")
    else:
        for _ in tqdm(range(50),
                      desc="Waiting for rolls to complete...",
                      leave=True,
                      unit="s",
                      mininterval=1):
            sleep(1)

print("Thank you for using MudaeBotTM")