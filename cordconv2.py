import subprocess

# Convert Degreess Minutes Seconds to Degrees Decimal Minutes
def dms2ddm(deg,min,sec):
    deg1 = int(deg) # we need to convert due to 1the fact that the inpu1t deosnt need a deciaml point.
    sec1 = str(sec/60)[0:5] # Divide sec by 60 for DMS -> DDM conversion. Convert to string and count length up to 5 from 0 for use. No more is needed for DCS.
    sec2 = float(sec1) # Convert back to float for use in the next line.
    ddm2 = deg1, min + sec2 # Add the minutes and seconds together to complete the DDM conversion.
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