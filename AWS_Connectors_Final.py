import requests
import json
import base64
import csv
import os
import time

def Config_File():

    f=open("config.txt","r")
    lines=f.readlines()
    USERNAME=lines[0]
    PASSWORD=lines[1]
    URL=lines[2]
    f.close()
    user=USERNAME.rstrip()
    passw=PASSWORD.rstrip()
    return user, passw, URL

def Post_Call(username,password,URL,data_connector):

    usrPass = str(username)+':'+str(password)
    b64Val = base64.b64encode(usrPass)
    headers = {
        'Accept': '*/*',
        'content-type': 'application/json',
        'Authorization': "Basic %s" % b64Val
    }

    r = requests.post(URL, data=json.dumps(data_connector), headers=headers)
    return r.raise_for_status()


def Add_AWS_Connector():
    username=''
    password=''
    URL=''
    username = str(Config_File()[0]).strip()
    password = str(Config_File()[1]).strip()
    URL = str(Config_File()[2]).strip()

    print '------------------------------AWS Connectors--------------------------------'
    if not os.path.exists("debug"):
        os.makedirs("debug")
    debug_file_name = "debug/debug_file"+ time.strftime("%Y%m%d-%H%M%S") + ".txt"
    debug_file = open(debug_file_name, "w")
    debug_file.write('------------------------------AWS Connectors--------------------------------' + '\n')
    #df = pd.read_excel('AWS_CONNECTOR_INFO.xlsx', sheet_name='Sheet1')
    with open('AWS_CONNECTOR_INFO.csv', 'rb') as f:
        reader = csv.DictReader(f)
        a = list(reader)
        f.close()
    counter=0
    for i in a:
        counter += 1
        ARN = i['ARN']
        EXT = i['EXTID']
        DESC = i['DESC']
        NAME = i['NAME']
        print str(counter) + ' : AWS Connector'
        debug_file.write(str(counter) + ' : AWS Connector' + '\n')
        print '---' + 'ARN : ' + str(ARN)
        print '---' + 'EXT : ' + str(EXT)
        print '---' + 'DESC : ' + str(DESC)
        print '---' + 'NAME : ' + str(NAME)
        debug_file.write('---' + 'ARN : ' + str(ARN) + '\n')
        debug_file.write('---' + 'EXT : ' + str(EXT) + '\n')
        debug_file.write('---' + 'DESC : ' + str(DESC) + '\n')
        debug_file.write('---' + 'NAME : ' + str(NAME) + '\n')

        data_connector = {
            "arn": str(ARN),
            "description": str(DESC),
            "externalId": str(EXT),
            "name": str(NAME)
        }

        try:
            Post_Call(username, password, URL, data_connector)
            print str(counter) + ' : Connector Added Successfully'
            print '-------------------------------------------------------------'
            debug_file.write(str(counter) + ' : Connector Added Successfully' + '\n')

        except requests.exceptions.HTTPError as e:  # This is the correct syntax
            print str(counter) + ' : Failed to Add AWS Connector'
            print e
            print '-------------------------------------------------------------'
            debug_file.write(str(counter) + ' : Failed to Add AWS Connector' + '\n')
            debug_file.write(str(e) + '\n')

    debug_file.close()

Add_AWS_Connector()
