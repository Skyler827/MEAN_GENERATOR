import sys
import os
import subprocess
import shutil
##### STEP 0: MAKE SURE WE ARE READY TO GO #####
def testCommands():
    if not shutil.which("ng"):
        print("ng command is missing")
        print("make sure you've installed angular cli tools with `npm install -g @angular/cli`")
        exit(1)
##### STEP 1: INITIALIZE DIRECTORY #####
def initializeDirectory():
    try:
        arg_path = os.path.abspath(sys.argv[1])
        print(arg_path)
    except IndexError:
        print("Error: must run with a file path as an argument")
        exit(1)
    if os.path.isfile(arg_path):
        print("Error: given path is an existing file, exiting")
    print(f"Creating express app at {arg_path}")
    if os.path.isdir(arg_path):
        shutil.rmtree(arg_path)
    os.makedirs(arg_path)
    os.chdir(arg_path)

##### STEP TWO: INITIALIZE PROJECT BACKEND #####
def initializeBackend():
    # create the following files/directories:
    directories = {
        "public": {},
        "server": {
            "config": {},
            "controllers": {},
            "models": {},
            "server.js": "templates/server.js_"
        }
    }
    # run npm init -y in the server directory
    # run npm install this that whatever

##### STEP THREE: INITIALIZE PROJECT FRONTEND #####
# run npm init in the public directory

def main():
    testCommands()
    initializeDirectory()
    initializeBackend()
main()