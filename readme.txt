*AWS_Connectors.py*
Info : Python File adds the AWS connector into CloudView w.r.t details provided in "./AWS_CONNECTOR_INFO.csv" & "./config.txt".
       Console output as well as debug_file.txt will have both success & failure logs.

*AWS_CONNECTOR_INFO.csv:*
Info : csv files contains below attributes required for AWS connector
Script looks for AWS_CONNECTOR_INFO.csv in the directory the script runs from
> ARN, EXTERNAL ID, DESCRIPTION & NAME (Kindly provide correct ARN & EXTERNAL ID's)

*EXTERNAL ID (EXTID) must be an INT from 9-90 in length* Example: 98765456787654567821

*config.txt*
Info : Kindly provide correct correct USERNAME, PASSWORD & CloudView URL in the ./config.txt
Script looks for config.txt in the directory the script runs from
URL = Please get the proper base URL For you Qualys API connection from your api portal
URL + /cloudview-api/rest/1.5/aws/connectors
Example file contents:
useranme
password
URL

* Script Requirements*
This script requires the following PIP modules to run
Modules: requests, json, base64, csv, os, time

MAC/Linux "pip install requests"
Windows "python -m pip install requests"

*Debug*
Debug file for script run, located in ./debug folder with time/date stamp
