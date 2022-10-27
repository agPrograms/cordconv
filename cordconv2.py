import subprocess

# Convert Degreess Minutes Seconds to Degrees Decimal Minutes
def dms2ddm(deg,min,sec):
    sec1 = float(str(sec/60)[0:5])+min # improved since 1.0. 
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
        print("Convert DMS to Degrees Decimal Minutes \n")
        print("Enter Degrees \n")
        deg = float(input())
        print("Enter Minutes \n")
        min = float(input())
        print("Enter Seconds \n")
        sec = float(input())
        ddmResult = dms2ddm(deg,min,sec)
        print('\nDDM: ', ddmResult, '\n')
        #print(dms2ddm(deg,min,sec))
        copy2clip(str(ddmResult))
        print('Degrees Decimal Minutes copied to clipboard! \n')
    elif selection == '2': 
        break
    else: 
        print("Please select a valid option! \n")
