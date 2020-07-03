import random
from time import sleep
from os import system, name

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux
    else: 
        _ = system('clear') 

print('First snake to grow over 30m wins')
sleep(1)
print("3")
sleep(1)
print("2")
sleep(1)
print("1")
sleep(1)
print("GO!")
sleep(1)
clear()

green = 0
yellow = 0
blue = 0

print(f"\u001b[32mGre: =e {green}\n\u001b[33mYel: =e {yellow}\n\u001b[34mBlu: =e {blue}\u001b[37m")
sleep(1)
clear()

while green < 30 and yellow < 30 and blue < 30:
    
    green += random.randint(0,3)
    yellow += random.randint(0,3)
    blue += random.randint(0,3)
    
    gline = "="*green
    yline = "="*yellow
    bline = "="*blue

    print(f"\u001b[32mGre: {gline}=e {green}\n\u001b[33mYel: {yline}=e {yellow}\n\u001b[34mBlu: {bline}=e {blue}\u001b[37m")

    sleep(1)
    clear()

print(f"\u001b[32mGre: {gline}=e {green}\n\u001b[33mYel: {yline}=e {yellow}\n\u001b[34mBlu: {bline}=e {blue}\u001b[37m")

if green > yellow and green > blue:
    print("WINNER: \u001b[32mGreen Snake\u001b[37m")

elif yellow > green and yellow > blue:
    print("WINNER: \u001b[33mYellow Snake\u001b[37m") 

else:
    print("WINNER: \u001b[34mBlue Snake\u001b[37m")