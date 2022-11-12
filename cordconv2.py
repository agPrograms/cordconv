import subprocess
import re
import os

# just some colors for QoL.
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

version = f"{bcolors.OKGREEN}Version - 1.3.0{bcolors.ENDC}\n"
file = '\coords_dms-ddm.txt'
filedd = '\coords_dd-dms.txt'
filefold = os.getcwd()+"\cordconvs"

# classes for more organization.
class cordconvme:
    def findit():
        if os.path.exists(filefold) != True:
            os.mkdir(filefold)
            print(f"{bcolors.OKGREEN}cordconv folder created at " + filefold + f"{bcolors.ENDC} !")
    # have an idea to make game detection effect menu items. Right now it just prints if a game is running.
    def gamefind(game_name):
        call = 'TASKLIST', '/FI', 'imagename eq %s' % game_name
        output = subprocess.check_output(call).decode()
        last_line = output.strip().split('\r\n')[-1]
        return last_line.lower().startswith(game_name.lower())
    def gamecatch():
        if cordconvme.gamefind("DCS.exe") == True:
            print(f"{bcolors.OKGREEN}DCS is running!{bcolors.ENDC}")
        elif cordconvme.gamefind("MicrosoftFlightSimulator.exe") == True:
            print(f"{bcolors.OKGREEN}MSFS is running!{bcolors.ENDC}")
        elif cordconvme.gamefind("DCS.exe" or "MicrosoftFlightSimulator.exe") == False:
            print(f"{bcolors.FAIL}No game is running!{bcolors.ENDC}")

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
menu['1']=f"{bcolors.OKCYAN}(DCS) Convert DMS to Degress Decimal Minutes{bcolors.ENDC}"
menu['2']=f"{bcolors.OKCYAN}(MSFS) Convert LatLong DD to DMS{bcolors.ENDC}"
menu['3']=f"{bcolors.OKCYAN}Exit{bcolors.ENDC}"
while True:
    options=menu.keys()
    for entry in options: 
        print(entry, menu[entry])
    selection=input("Please Select: ") 
    if selection =='1': 
        coords = []
        # Get the north coordinates from the user
        print(f"{bcolors.OKGREEN}Convert DMS to Degrees Decimal Minutes \n {bcolors.ENDC}")
        print(f"{bcolors.OKGREEN}Enter North Degrees \n {bcolors.ENDC}")
        deg = float(input())
        print(f"{bcolors.OKGREEN}Enter North Minutes \n {bcolors.ENDC}")
        min = float(input())
        print(f"{bcolors.OKGREEN}Enter North Seconds \n {bcolors.ENDC}")
        sec = float(input())
        ddmResult = dms2ddm(deg,min,sec)
        print(f'\n{bcolors.OKBLUE}DDM: N', ddmResult, f'\n {bcolors.ENDC}')
        copy2clip(str(ddmResult))
        coords.append(str('N'+str(ddmResult)))
        print('NORTH Degrees Decimal Minutes copied to clipboard! \n')

        # Get the east coordinates from the user
        print(f"{bcolors.OKGREEN}Enter East Degrees \n {bcolors.ENDC}")
        deg = float(input())
        print(f"{bcolors.OKGREEN}Enter East Minutes \n {bcolors.ENDC}")
        min = float(input())
        print(f"{bcolors.OKGREEN}Enter East Seconds \n {bcolors.ENDC}")
        sec = float(input())
        ddmResult = dms2ddm(deg,min,sec)
        print(f'\n{bcolors.OKBLUE}DDM: E', ddmResult,f'\n {bcolors.ENDC}')
        copy2clip(str(ddmResult))
        coords.append(str('E'+str(ddmResult)))
        print('EAST Degrees Decimal Minutes copied to clipboard! \n')

        # Ask the user if they want to copy the coordinates to a notepad document.
        print('Copy both coordinates to a txt file/notepad? [Y/n]\n');print(f'{bcolors.WARNING}!!!*** WARNING: This will overwrite the file coords_dms-ddm.txt where this is executed! ***!!!{bcolors.ENDC}\n')
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
        print(f"{bcolors.OKGREEN}Enter Latitude \n {bcolors.ENDC}")
        lat = dd2dms(float(input()))
        print(f"{bcolors.OKGREEN}Enter Longitude \n {bcolors.ENDC}")
        lon = dd2dms(float(input()))
        print(f'\n{bcolors.OKBLUE}DMS: ', lat, lon, f'\n{bcolors.ENDC}')
        copy2clip(str(lat)+str(lon))
        print('DMS copied to clipboard! \n')
        print('Copy both coordinates to a txt file/notepad? [Y/n]\n');print(f'{bcolors.WARNING}!!!*** WARNING: This will overwrite the file coords_dd-dms.txt where this is executed! ***!!!{bcolors.ENDC}\n')
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
