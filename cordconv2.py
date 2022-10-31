import subprocess
import re
import os

version = 'Version 1.2.0\n'
file = 'coords123.txt'
# Convert Degreess Minutes Seconds to Degrees Decimal Minutes
def dms2ddm(deg,min,sec):
    sec1 = str(float(str(sec/60)[0:5])+min) # improved since 1.0.
    ddm2 = int(deg), sec1 # improved since 1.0
    return ddm2

# Copy output to clipboard
def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)
menu = {}
menu['1']="Convert DMS to Degress Decimal Minutes"
menu['2']="Exit"
while True:
    options=menu.keys()
    for entry in options: 
        print(entry, menu[entry])
    selection=input("Please Select: ") 
    if selection =='1': 
        coords = []
        # Get the north coordinates from the user
        print("Convert DMS to Degrees Decimal Minutes \n")
        print("Enter North Degrees \n")
        deg = float(input())
        print("Enter North Minutes \n")
        min = float(input())
        print("Enter North Seconds \n")
        sec = float(input())
        ddmResult = dms2ddm(deg,min,sec)
        print('\nDDM: N', ddmResult, '\n')
        copy2clip(str(ddmResult))
        coords.append(str('N'+str(ddmResult)))
        print('NORTH Degrees Decimal Minutes copied to clipboard! \n')

        # Get the east coordinates from the user
        print("Enter East Degrees \n")
        deg = float(input())
        print("Enter East Minutes \n")
        min = float(input())
        print("Enter East Seconds \n")
        sec = float(input())
        ddmResult = dms2ddm(deg,min,sec)
        print('\nDDM: E', ddmResult, '\n')
        copy2clip(str(ddmResult))
        coords.append(str('E'+str(ddmResult)))
        print('EAST Degrees Decimal Minutes copied to clipboard! \n')
        
        # Ask the user if they want to copy the coordinates to a notepad document.
        print('Copy both coordinates to a txt file/notepad? [Y/n]\n');print('!!!*** WARNING: This will overwrite the file coords123.txt where this is executed! ***!!!\n')
        fnlchoice = str(input('Y/n: ').lower()) # convert user input to lower case
        if fnlchoice.startswith('y'):
            data = re.sub('[()''"",]', '', str(coords)[1:-1]) # GET RID OF SYMBOLS AND []
            with open(file, 'w') as f:
                for item in data:
                    f.write("%s" % item) # I cant use \n here because it will add a new line for every character. THANKS REGEX...
            subprocess.Popen(['notepad.exe', file])
            print('\nCopied to file: ',os.getcwd()+file, '\n')
        elif fnlchoice.startswith('n'):
            print('Ok! Not copying to notepad. \n')
    elif selection == '2': 
        break
    else: 
        print("Please select a valid option! \n")
