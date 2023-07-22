import subprocess
import re
import os
import colorama
colorama.init(wrap=True) # Initialize colorama, fix for Windows!

# data = re.sub('[()''"",]', '', str(ddm2)) ??? Do this at the return of ddm2?

# just some colors for QoL.
# I need to shorten these...
class b:
    blu = '\033[94m'
    cy = '\033[96m'
    grn = '\033[92m'
    warn = '\033[93m'
    fail = '\033[91m'
    end = '\033[0m'

version = f"{b.grn}Version - 1.3.2{b.end}\n"
file = '\coords_dms-ddm.txt'
filedd = '\coords_dd-dms.txt'
filefold = os.getcwd()+"\cordconvs"

# classes for more organization.
class cordconvme:
    def findit():
        if os.path.exists(filefold) != True:
            os.mkdir(filefold)
            print(f"{b.grn}cordconv folder created at " + filefold + f"{b.end} !")
    # have an idea to make game detection effect menu items. Right now it just prints if a game is running.
    def gamefind(game_name):
        call = 'TASKLIST', '/FI', 'imagename eq %s' % game_name
        output = subprocess.check_output(call).decode()
        last_line = output.strip().split('\r\n')[-1]
        return last_line.lower().startswith(game_name.lower())
    def gamecatch():
        if cordconvme.gamefind("DCS.exe") == True:
            print(f"{b.grn}DCS is running!{b.end}")
        elif cordconvme.gamefind("MicrosoftFlightSimulator.exe") == True:
            print(f"{b.grn}MSFS is running!{b.end}")
        elif cordconvme.gamefind("DCS.exe" or "MicrosoftFlightSimulator.exe") == False:
            print(f"{b.fail}No supported game is running!{b.end}")

def dms2ddm(deg,min,sec):
    sec1 = str(float(str(sec/60)[0:5])+min);ddm2 = int(deg), sec1
    return ddm2

def dd2dms(dd):
    is_positive = dd >= 0;dd = abs(dd)
    minutes,seconds = divmod(dd*3600,60);degrees,minutes = divmod(minutes,60)
    degrees = degrees if is_positive else -degrees
    return (int(degrees),int(minutes),str(seconds)[0:4]) # I should probably round seconds instead.

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

print(version)
cordconvme.gamecatch()
cordconvme.findit()

menu = {} # can I put the start of the colors here? and edn it at menu entry 3?
menu['1']=f"{b.cy}(DCS) Convert DMS to Degress Decimal Minutes{b.end}"
menu['2']=f"{b.cy}(MSFS) Convert LatLong DD to DMS{b.end}"
menu['3']=f"{b.cy}Exit{b.end}"
while True:
    options=menu.keys()
    for entry in options: 
        print(entry, menu[entry])
    selection=input("Please Select: ") 
    if selection =='1': 
        coords = []
        # Get the north coordinates from the user
        print(f"{b.grn}Convert DMS to Degrees Decimal Minutes \n {b.end}")
        print(f"{b.grn}Enter North Degrees \n {b.end}")
        deg = float(input())
        print(f"{b.grn}Enter North Minutes \n {b.end}")
        min = float(input())
        print(f"{b.grn}Enter North Seconds \n {b.end}")
        sec = float(input())
        ddmResult = dms2ddm(deg,min,sec)
        print(f'\n{b.blu}DDM: N', ddmResult, f'\n {b.end}')
        copy2clip(str(ddmResult))
        coords.append(str('N'+str(ddmResult)))
        print('NORTH Degrees Decimal Minutes copied to clipboard! \n')

        # Get the east coordinates from the user
        print(f"{b.grn}Enter East Degrees \n {b.end}")
        deg = float(input())
        print(f"{b.grn}Enter East Minutes \n {b.end}")
        min = float(input())
        print(f"{b.grn}Enter East Seconds \n {b.end}")
        sec = float(input())
        ddmResult = dms2ddm(deg,min,sec)
        ddmString = str(ddmResult) # this down to the else is new. get rid of it if it doesn't work.
        if ddmString[0:1] != '0':
            ddmResult = '0'+str(ddmString) # Zero is placed in front of the paranthesis. REGEX?
            print(f'\n{b.blu}DDM: E', ddmResult,f'\n {b.end}')
            copy2clip(str(ddmResult))
            coords.append(str('E'+str(ddmResult)))
            print(f'{b.warn}Zero Missing, Corrected!{b.end}')
            print('EAST Degrees Decimal Minutes copied to clipboard! \n')
        elif len(ddmString) != 17:
            ddmResult = str(ddmString)+'0'
            print(f'\n{b.blu}DDM: E', ddmResult,f'\n {b.end}')
            copy2clip(str(ddmResult))
            coords.append(str('E'+str(ddmResult)))
            print(f'{b.warn}Zero Missing, Corrected!{b.end}')
            print('EAST Degrees Decimal Minutes copied to clipboard! \n')
        else:
            print(f'\n{b.blu}DDM: E', ddmResult,f'\n {b.end}')
            copy2clip(str(ddmResult))
            coords.append(str('E'+str(ddmResult)))
            print('EAST Degrees Decimal Minutes copied to clipboard! \n')

        # Ask the user if they want to copy the coordinates to a notepad document.
        print('Copy both coordinates to a txt file/notepad? [Y/n]\n');print(f'{b.warn}!!!*** warn: This will overwrite the file coords_dms-ddm.txt where this is executed! ***!!!{b.end}\n')
        fnlchoice = str(input('Y/n: ').lower()) # convert user input to lower case
        if fnlchoice.startswith('y'):
            data = re.sub('[()''"",]', '', str(coords)[1:-1]) # GET RID OF SYMBOLS AND []
            with open(filefold+file, 'w') as f:
                for item in data:
                    f.write("%s" % item) # I cant use \n here because it will add a new line for every character. THANKS REGEX...
            subprocess.Popen(['notepad.exe', filefold+file])
            print('\nCopied to file: ',filefold+file, '\n')
        elif fnlchoice.startswith('n'):
            print('Ok! Not copying to notepad. \n')

# Issues fixed: each number was a decimal. repeating numbers removed. might want to round it instead.
# Issues TO FIX: make it easier to read. Painful.

    elif selection == '2':
        print("Convert LatLong DD to DMS \n")
        print(f"{b.grn}Enter Latitude \n {b.end}")
        lat = dd2dms(float(input()))
        print(f"{b.grn}Enter Longitude \n {b.end}")
        lon = dd2dms(float(input()))
        print(f'\n{b.blu}DMS: ', lat, lon, f'\n{b.end}')
        copy2clip(str(lat)+str(lon))
        print('DMS copied to clipboard! \n')
        print('Copy both coordinates to a txt file/notepad? [Y/n]\n');print(f'{b.warn}!!!*** warn: This will overwrite the file coords_dd-dms.txt where this is executed! ***!!!{b.end}\n')
        fnlchoice = str(input('Y/n: ').lower())
        if fnlchoice.startswith('y'):
            data = re.sub('[()''"",]', '', str(lat)+str(lon))
            with open(filefold+filedd, 'w') as f:
                for item in data:
                    f.write("%s" % item)
            subprocess.Popen(['notepad.exe', filefold+filedd])
            print('\nCopied to file: ',filefold+filedd, '\n')
        elif fnlchoice.startswith('n'):
            print('Ok! Not copying to notepad. \n')

    elif selection == '3': 
        break
    else: 
        print("Please select a valid option! \n")
