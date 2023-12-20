import os
 
print("Elevated Privileges are not required for this application depending on the following settings")
gotReqPackages = input("Do you have git, gcc and wget installed? [y/n]: ")
movetoUSRBIN = input("Do you want to make 2048 to run with the command \"2048\"? [y/n]: ")

def execute_cmd(command):
    stream = os.popen(command)
    output = stream.read()
    output

    return output

if gotReqPackages == "n":
    installPackages = input("Would you like to install the required packages? \nThis requires this script to be run as sudo: [y/n]")
    if installPackages == "y":
        execute_cmd("apt-get install gcc wget git")
    else:
        print("[FAIL] You cannot install 2048 since you do not have the required packages to do so: gcc, wget git.")
        
    if movetoUSRBIN == "y":
        execute_cmd("git clone https://github.com/CyberDudeJ/2048 && cd 2048")
        print("[INFO] To continue you must have gcc installed.")
        execute_cmd("gcc -o ./2048/2048 ./2048/2048.c")
        print("[INFO] Now moving 2048 to /usr/bin - requires elevated privilages/sudo or root access")
        execute_cmd("mv ./2048/2048 /usr/bin")
        print("[INFO] If no error has occured, 2048 may now be run. Exiting setup")
    
    elif movetoUSRBIN == "n":
        execute_cmd("git clone https://github.com/CyberDudeJ/2048 && cd 2048")
        print("[INFO] To continue you must have gcc installed.")
        execute_cmd("gcc -o ./2048/2048 ./2048/2048.c")
        print("[INFO] You can now run 2048 if no errors occured by using ./2048 \n[INFO] To make it executable system-wide, do \"mv 2048 /usr/bin/\" (this reqires sudo access)")
        
    else:
        print("Option must be either y or n")
        
elif gotReqPackages == "y":
    if movetoUSRBIN == "y":
        execute_cmd("git clone https://github.com/CyberDudeJ/2048 && cd 2048")
        execute_cmd("gcc -o ./2048/2048 ./2048/2048.c")
        print("[INFO] Now moving to 2048 to /usr/bin - requires elevated privilages/sudo or root access")
        execute_cmd("mv ./2048/2048 /usr/bin")
        print("[INFO] If no error has occured, 2048 may now be run. Exiting setup")
        
    elif movetoUSRBIN == "n":
        execute_cmd("git clone https:///github.com/CyberDudeJ/2048 && cd 2048")
        execute_cmd("gcc -o ./2048/2048 ./2048/2048.c")
        print("[INFO] If no error has occured, 2048 may now be run using ./2048 \n[INFO] To make it executable system-wide, do \"mv 2048 /usr/bin/\" (this requires sudo access)")
        
else:
    print("Option must be either y or n")
