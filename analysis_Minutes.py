#%%
globals().clear()
#%%
import numpy as np
import pandas as pd
import glob
import seaborn as sns
import matplotlib.pyplot as plt
import cufflinks as cf
from datetime import datetime
cf.go_offline()
pd.set_option("display.max_columns", 20)
import os

#%%

#Pfad der einzulesenden csv.-Dateien
path = './data/apicall_minutes/all_days'
all_files = glob.glob(path + "/*.csv")

#%%
#Erstellung eines df

li = []

for filename in all_files:
    print(filename)
    df0 = pd.read_csv(filename, index_col=None, header=0)
    li.append(df0)
dfu = pd.concat(li, axis=0, ignore_index=True)
#%%
dfu['date'] =  pd.to_datetime(dfu['date'],
                              format='%Y-%m-%dT%H:%M:%S')

#%%
df=dfu.loc[(dfu['SSOId']!='Unspecified')  & (dfu['date']>datetime(2020,5,20))  & (dfu['date']<datetime(2020,5,30))]

#%%
#df=dfu.loc[(dfu['SSOId']!='Unspecified')  & (dfu['date']>datetime(2020,5,22))  & (dfu['date']<datetime(2020,5,23))]
#%%
df_grouped=df[df['Visitors']>1].groupby(['date', 'Visitors'])['SSOId'].count().to_frame().unstack()
df_grouped_app=df[df['VisitorsApp']>1].groupby(['date', 'VisitorsApp'])['SSOId'].count().to_frame().unstack()
#%%

fig=plt.figure()
ax=df_grouped.plot()
plt.show()

#%%

fig=plt.figure()
ax=df_grouped.plot(kind='bar',stacked=True)
for i, t in enumerate(ax.get_xticklabels()):
    if (i % 12) != 0:
        t.set_visible(False)
plt.show()

#%%

fig=plt.figure()
ax=df_grouped_app.plot(kind='bar',stacked=True)
for i, t in enumerate(ax.get_xticklabels()):
    if (i % 12) != 0:
        t.set_visible(False)
plt.show()
#%%

fig=plt.figure()
ax=df_grouped.plot(kind='scatter')
plt.show()
#%%
fig = px.scatter(df,x='date',  y='Visitors')


fig.show()

#%%
fig = px.scatter(df,x='date',  y='Visitors', color='Channel',
                 marginal_x="box", marginal_y='box',
                animation_frame="Stunden", hover_data=["Title", 'IndexGesamtPIX', 'IndexRWPIX', 'IndexLDPIX'])

fig.show()
