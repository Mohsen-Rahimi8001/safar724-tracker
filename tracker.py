import requests
import json
from playsound import playsound
import sys

n = len(sys.argv)
args = sys.argv[1:]

SILENT = False
DATE = None

if "-h" == args[0]:
    print("""
    -d [YYYY-MM-DD]
        specify the date you want to track for bus tickets
    -s 
        silent mode: the noise will not play when a ticket get found
            """)
else:

    for i, arg in enumerate(args):
        if arg == "-d":
            try:
                date = args[i+1]
                year, month, day = map(int, date.split("-"))

            except ValueError:
                print("wrong format of date.")
                exit(1)

            except IndexError:
                print("You should enter date [YYYY-MM-DD] after -d.")
                exit(2)

        elif arg == "-s":
            SILENT = True


    req = f"https://safar724.com/bus/getservices?origin=11320000&destination=95310000&date={year}%2F{month}%2F{day}"

    try:
        res = requests.get(req)
    except Exception as e:
        print("something went wrong")
        if not SILENT:
            playsound("beep-09.mp3")

        exit(3)

    data = json.loads(res.text)

    print(f"searching for {year}/{month}/{day}\n")

    if len(data["Items"]) == 0:
        print("No tickets")
    
    found = False
    for item in data["Items"]:
        if item["AvailableSeatCount"] > 0:
            found = True
            print(item["ID"], item["DepartureTime"], item["DepartureDate"], item["AvailableSeatCount"])

    if found and not SILENT:
        playsound("beep-09.mp3")

