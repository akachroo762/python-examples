# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.

import pytz
import datetime

# print(menu[3])
# answer = 1
localFormat = "%Y-%m-%d %H:%M:%S %A %z"
menu = {"1": "Indian/Maldives",
        "2": "Indian/Mauritius",
        "3": "Indian/Mayotte",
        "4": "Indian/Reunion",
        "5": "Iran",
        "6": "Israel",
        "7": "Japan",
        "8": "Libya",
        "9": "Asia/Kolkata"}
print("Choose from the following options: ")
while True:

    for key in sorted(menu):
        print(str(key) + ": " + menu[key])
    selection = input()
    if selection in sorted(menu):
        value = menu[selection]
        tz_to_display = pytz.timezone(value)
        world_time = datetime.datetime.now(tz=tz_to_display)
        utc = datetime.datetime.utcnow()
        print("The world time in {} is {} ".format(value, world_time.strftime(localFormat)))
        print("The local time is {}".format(datetime.datetime.now().strftime(localFormat)))
        print("The UTC is {}".format(datetime.datetime.utcnow().strftime(localFormat)))
    elif selection == "0":
        print("Bye! Bye!")
        break
    else:
        print("Please choose the right option +++++")

# answer = menu[3]
# tz_to_display = pytz.timezone(answer)
# local_time = datetime.datetime.now(tz=tz_to_display)
# print(local_time)


# selection = 1
# while True:
#     menu = ["Quit", "Indian/Maldives", "Indian/Mauritius",
#             "Indian/Mayotte", "Indian/Reunion", "Iran", "Israel", "Japan", "Libya", "Asia/Kolkata"]
#     selection = int(input("Choose one of the options below: {}".format(menu))
#
#     for answers in enumerate(menu):
#         print(answers)
