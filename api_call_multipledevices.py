#%%
globals().clear()
import json
import requests
from pandas.io.json import json_normalize
import pandas as pd
from datetime import datetime, timedelta
import os

import dateutil.relativedelta
#%%

start_date=datetime(2020, 5, 7)
art='deviceType'
#art='environment'
#frequence='weekly'
frequence='daily'



#%%
body_deviceType={
    "rsid": "spiegel.ng.spieg.main",
    "globalFilters": [
        {
            "type": "dateRange",
            "dateRange": ""
        },
        {
            "type": "segment",
            "segmentId": "s3707_5e1c6a2c8d55e533b6600a38"
        },
        {
            "type": "segment",
            "segmentId": "s3707_5ebd0fd0e9eaeb7a6ec85ffb"
        }
    ],
    "metricContainer": {
        "metrics": [
            {
                "columnId": "0",
                "id": "metrics/visitors",
                "sort": "desc"
            },
            {
                "columnId": "1",
                "id": "cm_visits_visitor_defaultmetric"
            },
            {
                "columnId": "2",
                "id": "metrics/visits"
            },
            {
                "columnId": "4",
                "id": "metrics/visitors",
                "filters": [
                    "0"
                ]
            },
            {
                "columnId": "5",
                "id": "metrics/visitors",
                "filters": [
                    "1"
                ]
            },
            {
                "columnId": "6",
                "id": "metrics/visitors",
                "filters": [
                    "2"
                ]
            }
        ],
        "metricFilters": [
            {
                "id": "0",
                "type": "breakdown",
                "dimension": "variables/mobiledevicetype",
                "itemId": "2163986270"
            },
            {
                "id": "1",
                "type": "breakdown",
                "dimension": "variables/mobiledevicetype",
                "itemId": "0"
            },
            {
                "id": "2",
                "type": "breakdown",
                "dimension": "variables/mobiledevicetype",
                "itemId": "1728229488"
            }
        ]
    },
    "dimension": "variables/evar186",
    "settings": {
        "countRepeatInstances": True,
        "limit": 50000,
        "page": '',
        "nonesBehavior": "return-nones"
    },
    "statistics": {
        "functions": [
            "col-max",
            "col-min"
        ]
    }
}
#%%
body_environment={
    "rsid": "spiegel.ng.spieg.main",
    "globalFilters": [
        {
            "type": "dateRange",
            "dateRange": ""
        },
	    {
            "type": "segment",
            "segmentId": "s3707_5e1c6a2c8d55e533b6600a38"
        },
        {
            "type": "segment",
            "segmentId": "s3707_5ebd0fd0e9eaeb7a6ec85ffb"
        }
    ],
    "metricContainer": {
        "metrics": [
            {
                "columnId": "0",
                "id": "metrics/visitors",
                "sort": "desc"
            },
            {
                "columnId": "1",
                "id": "cm_visits_visitor_defaultmetric"
            },
            {
                "columnId": "2",
                "id": "metrics/visits"
            },
            {
                "columnId": "4",
                "id": "metrics/visitors",
                "filters": [
                    "0"
                ]
            },
            {
                "columnId": "5",
                "id": "metrics/visitors",
                "filters": [
                    "1"
                ]
            },
            {
                "columnId": "6",
                "id": "metrics/visitors",
                "filters": [
                    "2"
                ]
            }
        ],
        "metricFilters": [
            {
                "id": "0",
                "type": "breakdown",
                "dimension": "variables/evar3",
                "itemId": "3464274365"
            },
            {
                "id": "1",
                "type": "breakdown",
                "dimension": "variables/evar3",
                "itemId": "1174604723"
            },
            {
                "id": "2",
                "type": "breakdown",
                "dimension": "variables/evar3",
                "itemId": "1261512104"
            }
        ]
    },
    "dimension": "variables/evar186",
    "settings": {
        "countRepeatInstances": True,
        "limit": 50000,
        "page": 0,
        "nonesBehavior": "return-nones"
    },
    "statistics": {
        "functions": [
            "col-max",
            "col-min"
        ]
    }
}
#%%
if art=='environment':
    path1 = './data/apicall_environment/'
    body=body_environment
    col_names = []
    col_names.append('Visitors')
    col_names.append('Visits/Visitors')
    col_names.append('Visits')
    col_names.append('VisitorsApp')
    col_names.append('VisitorsWeb')
    col_names.append('VisitorsAmp')
elif art=='deviceType':
    path1 = './data/apicall_deviceType/'
    body = body_deviceType
    col_names = []
    col_names.append('Visitors')
    col_names.append('Visits/Visitors')
    col_names.append('Visits')
    col_names.append('VisitorsPhone')
    col_names.append('VisitorsDesktop')
    col_names.append('VisitorsTablet')

#%%
if frequence=='weekly':
    frequenz='W'
    intervall = timedelta(weeks=1)
    path=path1+'{}/'.format(frequence)
elif frequence=='daily':
    frequenz='D'
    intervall = timedelta(days=1)
    path = path1 + '{}/'.format(frequence)

elif frequence=='monthly':
    frequenz='M'
    intervall = dateutil.relativedelta.relativedelta(months=1)
    path = path1 + '{}/'.format(frequence)
else:
    print('Fehler')



#%%
end_date=datetime.now().replace(hour=0, minute=0,second=0, microsecond=0)-timedelta(days=1)

try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)

#%%
#col_names=[]
#metric0='visitorsPhone'
#metric1='visitorsDesktop'
#metric2='visitorsTablet'
#metric3='visitorsGes'
#metric4='visits/visitor'
#metric5='visits'

#col_names.append('Visitors')
#col_names.append('Visits/Visitors')
#col_names.append('Visits')
#col_names.append('VisitorsPhone')
#col_names.append('VisitorsDesktop')
#col_names.append('VisitorsTablet')


#%%

# API-call: automatischer Token

# set api params
#api_key = "5a8dcc2cfa71472cbfa4fb53671c45ed"
api_key='b126a48b6e704dbba3107de1d4cb3187'
#aa_token = readLines(paste(path_dir, "data/processed/token.txt", sep = ""))
#aa_token='eyJ4NXUiOiJpbXNfbmExLWtleS0xLmNlciIsImFsZyI6IlJTMjU2In0.eyJpZCI6IjE1OTAxMzY0MDE1MTZfOWQyNjVkMjEtMDAxNy00MzMxLWJjNzgtNWY4ODBiNjQ1NTk5X3VlMSIsImNsaWVudF9pZCI6ImIxMjZhNDhiNmU3MDRkYmJhMzEwN2RlMWQ0Y2IzMTg3IiwidXNlcl9pZCI6IjE5ODIxQjgzNUUyMDJBQkEwQTQ5NUMwOEB0ZWNoYWNjdC5hZG9iZS5jb20iLCJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiYXMiOiJpbXMtbmExIiwiZmciOiJVT1JXREJTUkZQTjVJN1VTQ01BM1FMUUFMTT09PT09PSIsIm1vaSI6IjdlYjJkMWJmIiwiYyI6InVGaDV5VndQQWVTUTMwdHlSNU1CckE9PSIsImV4cGlyZXNfaW4iOiI4NjQwMDAwMCIsInNjb3BlIjoib3BlbmlkLEFkb2JlSUQsYWRkaXRpb25hbF9pbmZvLnByb2plY3RlZFByb2R1Y3RDb250ZXh0IiwiY3JlYXRlZF9hdCI6IjE1OTAxMzY0MDE1MTYifQ.SnaMVVlCJnzCxwHRWs5wqLfGNu_B-cgZ1G5K_UXXwSXc1qk2qL1lOGMgM6CZ97NFsVyueTHSgkPFWU3mUQiLtIYjTRzoDFjnAtbi3M06_NkcEwLpI-uSVYR89MFeJdWivQlE321dz_DHZUOrQfrM7o8yUATpKUPAxmC04NB-L7wqb119L0wAe-y7m1vMLd0czqZQEpS8zscePmthQZ2QNnP_vBAJVkc-04_blKCi_5aw-XHTTeG-xAmVh1qd-kBF79-odIKh2QDIxDGiARpIJ_NOhnGdPAYz8pLR2enhy3gu3K5sv4FOta3HdJOWYtuYoJLGJJvcLS9PNXoRHpa8Xw'

f = open("data/token.txt", "r")
aa_token=f.read()
#%%

request_url = "https://analytics.adobe.io/api/spiege2/reports/"
url = "https://analytics.adobe.io/api/spiege2/reports/"
company_id = "spiege2"

headers = {'Content-type': 'application/json;charset=utf-8',
           'Accept': 'application/json',
           "x-api-key": api_key,
            "x-proxy-global-company-id": company_id,
           "Authorization": "Bearer "+aa_token}

#%%

# url= "https://appservice3-2.omniture.com/analytics/1.0/reports/ranked?locale=en_US"

# aa_token='eyJ4NXUiOiJpbXNfbmExLWtleS0xLmNlciIsImFsZyI6IlJTMjU2In0.eyJpZCI6IjE1ODk5ODAwNzA5MzhfNTU2ZjU3ZDEtYmEzZC00OTQ3LWFlYzQtMzFlZjU3MzhhYmU3X3VlMSIsImNsaWVudF9pZCI6IlNpdGVDYXRhbHlzdDIiLCJ1c2VyX2lkIjoiQjlGODBBMTk1QzdGN0FGNDBBNDk1REFEQGVjMmQxYWVmNWI0NDhjOGUwYTQ5NWRkNiIsInN0YXRlIjoie1wic2Vzc2lvblwiOlwiaHR0cHM6Ly9pbXMtbmExLmFkb2JlbG9naW4uY29tL2ltcy9zZXNzaW9uL3YxL09EYzBObVl3TlRJdE9UZzROaTAwTlRJMkxUa3haVEV0TkRka01ETTFaRGs0TURCakxTMUNPVVk0TUVFeE9UVkROMFkzUVVZME1FRTBPVFZFUVVSQVpXTXlaREZoWldZMVlqUTBPR000WlRCaE5EazFaR1EyXCJ9IiwidHlwZSI6ImFjY2Vzc190b2tlbiIsImFzIjoiaW1zLW5hMSIsImZnIjoiVU9NVEdCMktIUFA1NDdVWEM0STNRTFFBNkU9PT09PT0iLCJzaWQiOiIxNTg4ODUyMDc3OTEyXzJjZjYzYmU2LTEzNjQtNGRhZC04N2ZkLTk4ZjYyZWQ0YmFkYV91ZTEiLCJydGlkIjoiMTU4OTk4MDA3MDkzOF9jMmUzZDNjMi0zZDRmLTRlNTItOGY0NS0xNjhkODZkMzJkOTlfdWUxIiwib2MiOiJyZW5nYSpuYTFyKjE3MjMyMzI3YzlkKkozRjlFVDBKRlg1REg1RU1LNTU4WDYzVEtNIiwicnRlYSI6IjE1OTExODk2NzA5MzgiLCJtb2kiOiJjMmRkZWY5NSIsImMiOiI4bHZ0ZlVPY1FtMWVDbHcxSm5NTGRRPT0iLCJleHBpcmVzX2luIjoiODY0MDAwMDAiLCJzY29wZSI6Im9wZW5pZCxBZG9iZUlELHJlYWRfb3JnYW5pemF0aW9ucyxhZGRpdGlvbmFsX2luZm8ucHJvamVjdGVkUHJvZHVjdENvbnRleHQsYWRkaXRpb25hbF9pbmZvLmpvYl9mdW5jdGlvbixzZXNzaW9uIiwiY3JlYXRlZF9hdCI6IjE1ODk5ODAwNzA5MzgifQ.qt24GNUZMiQs8xD2nM_XOkbwiYd9CzorSRyu7Mj372YvsHG8TmtGA_s4ZIqSm54pyphjwDZR6I8HIi7e_HKIg6GY1kAFgLeRXzHPDapnaP9WZCPkAJQAEkeFc9-n1Pv9CjTjb4qaQZx6AgDL-QtsSWqp69sMMecYx4plqelZkWKmq6yZRUCtMiGQG2t-fjNiZ0kRTIegRtKSYumWQG2mtuuvq-xZUebZ5xCTo_9yb8je4JXiTYqfU4vErgVrgQUnMrHMiKf2x6-66pal539PVwEhy8KyKI7qnTXqQiJ1c8D_QSMRkGMUk3l0jLhqkam9TFEoXyEjnHefWBq7NSTt2w'

# headers = {'Content-type': 'application/json;charset=utf-8',
#           'Accept': 'application/json',
#           'x-proxy-company-id':'3707',
#           "x-proxy-userid": "200121610",
#           "x-request-id": "4599bf947bfb1f4ff7a377f3888981ad",
#           "Authorization": "Bearer "+aa_token}



#%%

print(start_date)

datelist = pd.date_range(start=start_date,end=end_date, freq=frequenz).tolist()


#%%
#body['globalFilters'][0]['dateRange']='{:%Y-%m-%dT%H:%M:%S.%f}/{:%Y-%m-%dT%H:%M:%S.%f}'.format((end_date- timedelta(weeks=1)),(end_date))
#print(body['globalFilters'][0])
#%%
#col_names.append('VisitorsApp')
#col_names.append('VisitorsWeb')
#col_names.append('VisitorsAmp')'

 #%%
#r = requests.post(url, json=body, headers=headers)
#d = json.loads(r.content)
#num_pages=d['totalPages']

#%%
for date in datelist:
    base_date=date+timedelta(days=1)
    print(base_date)
    print(base_date-intervall)
    body['globalFilters'][0]['dateRange'] = '{:%Y-%m-%dT%H:%M:%S.%f}/{:%Y-%m-%dT%H:%M:%S.%f}'.format(
        (base_date - intervall), (base_date))
    r = requests.post(url, json=body, headers=headers)
    d = json.loads(r.content)
    num_pages=d['totalPages']
    df_r2 = []
    df_api_final=pd.DataFrame()
    for page in range(0, num_pages):
        print(page)
        body['settings']['page'] = page
        r = requests.post(url, json=body, headers=headers)
        d = json.loads(r.content)
        df_response = pd.DataFrame(d.get('rows'))
        df_r2.append(df_response)
    df_api_final = pd.concat(df_r2)
    df = pd.DataFrame()
    df['SSOId'] = df_api_final['value']
    df[col_names] = pd.DataFrame(df_api_final.data.tolist())

    a = base_date - intervall
    b = a.strftime('%Y%m%d')

    df['StartDay'] = b

    path2 = path + b + '.csv'

    df.to_csv(path2)


#%%
#body['globalFilters'][0]['dateRange'] = '{:%Y-%m-%dT%H:%M:%S.%f}/{:%Y-%m-%dT%H:%M:%S.%f}'.format(
#        (base_date - intervall), (base_date))

#print(body["globalFilters"])
#%%
#r = requests.post(url, json=body, headers=headers)
#d = json.loads(r.content)
#print(d['totalPages'])
#   df_r2 = []
 #   df_api_final=pd.DataFrame()