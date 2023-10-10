import os
import sys
import json
import time
import subprocess

def is_watch_available():
    # Get the PATH environment variable
    path_dirs = os.environ.get('PATH', '').split(os.pathsep)

    # Check if 'watch' is present in any of the directories
    for directory in path_dirs:
        watch_path = os.path.join(directory, 'watch')
        if os.path.isfile(watch_path) and os.access(watch_path, os.X_OK):
            return True

    return False

oc = None
while not oc:
    q = input("Enter origin city name: ")

    with open("dump.json", "r", encoding="utf-8") as f:
        cities = json.load(f)

    for city in cities:
        if q in city.get("SearchExpressions"):
            oc = city
            break
    
    if not oc:
        print("no city found, try again!")

dc = None
while not dc:
    q = input("Enter destination city name: ")

    with open("dump.json", "r", encoding="utf-8") as f:
        cities = json.load(f)

    for city in cities:
        if q in city.get("SearchExpressions"):
            dc = city
            break
    
    if not dc:
        print("no city found, try again!")

date = input("Enter date:(YYYY-MM-DD) ")

oc_code = oc.get("Code")
dc_code = dc.get("Code")

SILENT = True
if input("Do you want to run the program with the beep sound?(yes/no) ").lower() == "yes":
    SILENT = False

command = f"{sys.executable} tracker.py --orig={oc_code} --dest={dc_code} -d {date}"

if SILENT:
    command += " -s"

if is_watch_available():
    command = "watch -n 5 " + command
    os.system(command)
else:
    while True:
        os.system("clear")
        print("Exit with ctrl+c")
        os.system(command)
        time.sleep(5)
