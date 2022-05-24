# coding=utf-8
import os
import requests
import subprocess


critical = False
high = 50
too_high = 70

# At First we have to get the current CPU-Temperature with this defined function
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

# Now we convert our value into a float number
temp = float(getCPUtemperature())

# Check if the temperature is abouve 60°C (you can change this value, but it shouldn't be above 70)
if (temp > high):
    if temp > too_high:
        critical = True
        subject = "Pi3B+ critical temperature!!".format(temp)
        body = "{}".format(temp)
    else:
        subject = "Pi3B+ temperature high".format(temp)
        body = "{} ".format(temp)


    headers = {
    # Already added when you pass json= but not when you pass data=
     'Content-Type': 'application/json',
    }

    json_data = {
    'device_iden': '****',
    'type': 'note',
    'title': subject,
    'body': body,
    }

    
    response = requests.post('pushes', headers=headers, json=json_data, verify=False, auth=('xxx', ''))
    if critical:
        os.popen('sudo halt')



