# cordconv
A coordinate converter made for DCS and (Now) MSFS.

## Purpose
I made this primarily for the Hoggit GCI. The online GCI only uses DMS, which makes it harder for a A10 or F-16 to look for a new mission on the fly. You can only view the tac-map in-game with targets shown before you spawn/select role. Which is why I made this. Just had an idea and thought it would be a little project to help me in game as well as sharpen my Python. I'll continue to add features and automation (Web Scrapping, communicate with an in-game scratchpad, etc.).

## Install/Setup
There is no setup or install required at the moment. You just download and run!  
The tool will create a directory called 'cordconvs' in the location it is executed in. This is where the coordinate files will be saved.

## Usage
#### First time start-up  
1. Drag and drop the tool in the location you desire. Such as your desktop!  
2. Open the tool, you should see a green message say: 'coordconv folder created at C:\Users\You!\Desktop\cordconvs!'  
#### Normal Usage  
1. Follow the on screen prompts to convert.  
2. The tool will copy the outputs of each step (North DDM, East DDM, North and East DMS) to your clipboard and echos it on screen in blue text. **However**, you can opt to have the tool create a .txt file and it will paste the outputs there - to which it will open it for you!  
  
**That's it really!**

## Suspicious File Notice
It is known that when you download this application (from releases), it will warn you that the file has no known owner/developer signed. That is fine, the code is all here! If you do not trust it, thats ok. You can use a package called pyinstaller to convert it to a .exe yourself or just download this branch's cordconv2.py file and run it yourself!
