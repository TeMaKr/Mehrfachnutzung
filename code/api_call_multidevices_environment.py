#%%
globals().clear()
import json
import requests
from pandas.io.json import json_normalize
import pandas as pd
from datetime import datetime, timedelta
import os


#%%
url= "https://appservice3-2.omniture.com/analytics/1.0/reports/ranked?locale=en_US"

aa_token='eyJ4NXUiOiJpbXNfbmExLWtleS0xLmNlciIsImFsZyI6IlJTMjU2In0.eyJpZCI6IjE1ODk4MTU2NDMwMjVfYTA0NTRlZDAtNmQyMi00M2RiLTgzNmYtMDc5NzhiMTllZmE0X3VlMSIsImNsaWVudF9pZCI6IlNpdGVDYXRhbHlzdDIiLCJ1c2VyX2lkIjoiQjlGODBBMTk1QzdGN0FGNDBBNDk1REFEQGVjMmQxYWVmNWI0NDhjOGUwYTQ5NWRkNiIsInN0YXRlIjoie1wic2Vzc2lvblwiOlwiaHR0cHM6Ly9pbXMtbmExLmFkb2JlbG9naW4uY29tL2ltcy9zZXNzaW9uL3YxL01UbGtPR0UyTlRJdE5EVXhOUzAwWXpsaExUZzJZbVV0TVdWaU9EbGxNamcxWXpkakxTMUNPVVk0TUVFeE9UVkROMFkzUVVZME1FRTBPVFZFUVVSQVpXTXlaREZoWldZMVlqUTBPR000WlRCaE5EazFaR1EyXCJ9IiwidHlwZSI6ImFjY2Vzc190b2tlbiIsImFzIjoiaW1zLW5hMSIsImZnIjoiVU9ISDZCMktIUFA1NDdVU0M0STNRTFFBUFE9PT09PT0iLCJzaWQiOiIxNTg4ODUyMDc3OTEyXzJjZjYzYmU2LTEzNjQtNGRhZC04N2ZkLTk4ZjYyZWQ0YmFkYV91ZTEiLCJydGlkIjoiMTU4OTgxNTY0MzAyNV80NzkwYTAzNi1iNmMxLTQwNjYtYTIxMi0xNDRiNTBhNzllN2ZfdWUxIiwib2MiOiJyZW5nYSpuYTFyKjE3MjI4NjU4NDgzKkZOV0NHNDVXSlg0Qzk0U0pUTVBBVzE2MFYwIiwicnRlYSI6IjE1OTEwMjUyNDMwMjUiLCJtb2kiOiIxZGQxZDZlZSIsImMiOiJGY2h0WmJpZW5aSzV0YkJBOTFCQVpRPT0iLCJleHBpcmVzX2luIjoiODY0MDAwMDAiLCJzY29wZSI6Im9wZW5pZCxBZG9iZUlELHJlYWRfb3JnYW5pemF0aW9ucyxhZGRpdGlvbmFsX2luZm8ucHJvamVjdGVkUHJvZHVjdENvbnRleHQsYWRkaXRpb25hbF9pbmZvLmpvYl9mdW5jdGlvbixzZXNzaW9uIiwiY3JlYXRlZF9hdCI6IjE1ODk4MTU2NDMwMjUifQ.fyZqRGhBUMomEkOMMoE-akyb5iL6zZWVzG4Qr5SeluFEnkrY-pR1zPw4eYZgAgr0Abdjlvvaj3NXDDBpXoC5i7uNNxu3rBs3R30DLzKxFOlKh4pb241BSYnKvO1j049BATiiOSwVF960Pd0nGG40ioLFLymwhBewoPAB08NnPK36Jgil1UlKCr87oqf3BOBkZ3XrI63-eheGnWzZ_tMhQCkhNRdMDOCFhWK20c74vg12phmEBiluaaTv0_c4bWuq8CNT8N0vncpahNrKi3grGBCJXSQqlgmYrAhFGwsyv7Dm2PDDhgQ7vDLmr5uZtZtOoXEO6xKB8yw5s1sP2IEgwQ'

headers = {'Content-type': 'application/json;charset=utf-8',
           'Accept': 'application/json',
           'x-proxy-company-id':'3707',
           "x-proxy-userid": "200121610",
           "x-request-id": "4599bf947bfb1f4ff7a377f3888981ad",
           "Authorization": "Bearer "+aa_token}

body={
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
        "limit": 500000,
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
col_names=[]
#metric0='visitorsPhone'
#metric1='visitorsDesktop'
#metric2='visitorsTablet'
#metric3='visitorsGes'
#metric4='visits/visitor'
#metric5='visits'

col_names.append('Visitors')
col_names.append('Visits/Visitors')
col_names.append('Visits')
col_names.append('VisitorsApp')
col_names.append('VisitorsWeb')
col_names.append('VisitorsAmp')

#%%
base_date=datetime.now().replace(hour=0, minute=0,second=0, microsecond=0)-timedelta(days=1)

datelist = pd.date_range(end=base_date,freq='W', periods=20).tolist()

#%%
for date in datelist:
    base_date=date+timedelta(days=1)
    print(base_date)

    body['globalFilters'][0]['dateRange'] = '{:%Y-%m-%dT%H:%M:%S.%f}/{:%Y-%m-%dT%H:%M:%S.%f}'.format(
        (base_date - timedelta(weeks=1)), (base_date))

    r = requests.post(url, json=body, headers=headers)
    d = json.loads(r.content)
    df_response = pd.DataFrame(d.get('rows'))
    df = pd.DataFrame()
    df['SSOId'] = df_response['value']
    df[col_names] = pd.DataFrame(df_response.data.tolist())

    a = base_date - timedelta(weeks=1)
    b = a.strftime('%Y%m%d')

    df['WeekStartDay'] = b

    path = 'data/apicall_multidevices_environment/' + b + '.csv'

    df.to_csv(path)


#%%

body['globalFilters'][0]['dateRange']='{:%Y-%m-%dT%H:%M:%S.%f}/{:%Y-%m-%dT%H:%M:%S.%f}'.format((base_date- timedelta(weeks=1)),(base_date))

r = requests.post(url, json=body, headers=headers)
d = json.loads(r.content)
df_response=pd.DataFrame(d.get('rows'))

df = pd.DataFrame()
df['SSOId']=df_response['value']
df[col_names]=pd.DataFrame(df_response.data.tolist())

#%%
a=base_date- timedelta(weeks=1)
b=a.strftime('%Y%m%d')

df['WeekStartDay']=b