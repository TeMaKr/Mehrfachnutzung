#%%
globals().clear()
import json
import requests
from pandas.io.json import json_normalize
import pandas as pd
from datetime import datetime, timedelta
import os
import time

import dateutil.relativedelta

#%%
start_date=datetime(2020, 5, 26,18)
end_date=datetime.now().replace(hour=0, minute=0,second=0, microsecond=0)-timedelta(days=1)

path1 = './data/apicall_minutes/all_days/'
datelist = pd.date_range(start=start_date, end=end_date, freq='D').tolist()
datelist_test=pd.date_range(start=start_date, end=end_date, freq='H').tolist()
#%%
body={
    "rsid": "spiegel.ng.spieg.main",
    "globalFilters": [
        {
            "type": "dateRange",
            "dateRange": ""
        },
        {
            "type": "segment",
            "segmentDefinition": {
                "container": {
                    "func": "container",
                    "context": "hits",
                    "pred": {
                        "func": "streq",
                        "str": "",
                        "val": {
                            "func": "attr",
                            "name": "variables/evar35"
                        },
                        "description": "Hour / Minute"
                    }
                },
                "func": "segment",
                "version": [
                    1,
                    0,
                    0
                ]
            }
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
                "columnId": "2",
                "id": "metrics/visitors",
                "filters": [
                    "0"
                ]
            },
            {
                "columnId": "3",
                "id": "metrics/visitors",
                "filters": [
                    "1"
                ]
            },
            {
                "columnId": "4",
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
col_names = []
col_names.append('Visitors')
col_names.append('VisitorsApp')
col_names.append('VisitorsWeb')
col_names.append('VisitorsAmp')
#%%
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
#r = requests.post(url, json=body, headers=headers)
#d = json.loads(r.content)

#%%
for Stunde in datelist_test:
    df_api_stunde = []
    datelist2 = pd.date_range(Stunde, periods=2, freq='1min')
    for date2 in datelist2:
        tagesfilter = date2.replace(hour=0, minute=0, second=0, microsecond=0)
        print(tagesfilter)
        print(tagesfilter+ timedelta(days=1))
        # print(date2)
        # print('-----')
        # print(date2.strftime("%H:%M"))
        # print(date2.strftime("%Y-%m-%dT%H:%M:%S"))
        datum = date2.strftime("%Y-%m-%dT%H:%M:%S")
        minute = date2.strftime("%H:%M")
        day = date2.strftime("%Y-%m-%d")
        b = date2.strftime('%Y%m%d_%H')
        #c = date2.strftime('%Y%m%d_%H')
        print(datum)
        print(b)
        # print('----')

        body['globalFilters'][0]['dateRange'] = \
            '{:%Y-%m-%dT%H:%M:%S.%f}/{:%Y-%m-%dT%H:%M:%S.%f}'.format(tagesfilter, tagesfilter + timedelta(days=1))
        body['globalFilters'][1]['segmentDefinition']['container']['pred']['str'] = \
            '{}'.format(date2.strftime("%H:%M"))

        r = requests.post(url, json=body, headers=headers)
        d = json.loads(r.content)
        num_pages = d['totalPages']
        df_r2 = []
        df_api_final = pd.DataFrame()

        for page in range(0, num_pages):
            # print(page)
            body['settings']['page'] = page
            r = requests.post(url, json=body, headers=headers)
            d = json.loads(r.content)
            df_response = pd.DataFrame(d.get('rows'))
            df_r2.append(df_response)
            df_api_final = pd.concat(df_r2)
            time.sleep(20)


        df = pd.DataFrame()
        df['SSOId'] = df_api_final['value']
        df['date'] = datum
        df['minute'] = minute
        df['day'] = day
        df[col_names] = pd.DataFrame(df_api_final.data.tolist())
        df_api_stunde.append(df)
        df_api_final2 = pd.concat(df_api_stunde)

        path2 = path1 + b + '.csv'

        df_api_final2.to_csv(path2)
        time.sleep(10)


