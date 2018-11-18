import datetime
import time

def remainder():
    now = datetime.datetime.now()
    today = now.strftime("%d/%m/%Y")
    totime = now.strftime("%I:%M")
    with open("Reminder.txt",'r') as file:
        #print(today,totime)
        for line in file:
            line = line.strip().split(" ")
            if today == line[0]:
                if totime == line[1]:
                    var = (" ".join(line[2:]))
                    return var
def rem_call():
    reminder_result = remainder()
    sleeptime = 60 - datetime.datetime.now().second
    time.sleep(sleeptime)
    return reminder_result



# if __name__ == "__main__":
#     while(True):
#         get_data()
#         remainder()
#         sleeptime = 60 - datetime.datetime.now().second
#         time.sleep(sleeptime)
