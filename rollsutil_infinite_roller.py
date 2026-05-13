from time import sleep
import pyautogui as auto
from tqdm import trange
import argparse

parser = argparse.ArgumentParser(description="Automate Mudae rolls with command of your choice.")
parser.add_argument("--roll", "-r", type=str, choices=['/wa ', '/ha ', '/wg ', '/hg ', '/wx ', '/hx '], default='/wa', help="The command to use for rolling (default: /wa).")
parser.add_argument("--input_mode", "-i", action='store_true', help="Use input mode to ask for confirmation after each roll (default: False). If not set, the script will wait for a fixed time after each roll.")
args = parser.parse_args()

message = args.roll
input_mode = args.input_mode or None

def write(message):
    auto.write(message, interval=0.1)
    auto.press("enter")
    
def repeat_command():
    auto.press('up')
    auto.press("enter")
    
def time_to_roll():
    write('/rollsutil usestack 20')
    sleep(1)
    for j in trange(20):
        sleep(0.5)
        if j == 0:
            write(message)
        else:
            repeat_command()


if __name__ == "__main__":
    roll = input("Time to roll ? (y/n) : ")
    while roll.lower() == 'y':
        for i in range(5,0,-1):
            print(f"Executing in {i}...")
            sleep(1)
        
        time_to_roll()   
        
        if input_mode:    
            roll = input("Rolls complete. Roll again ? (y/n) : ")
        else:
            # Wait with progress bar
            for _ in trange(45, desc="Waiting for commands to process...", unit="s", leave=False):
                sleep(1)

    print("Thank you for using MudaeBotTM")