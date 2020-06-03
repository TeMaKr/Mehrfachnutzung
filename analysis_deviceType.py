#%%
globals().clear()
#%%

import pandas as pd
import glob
import seaborn as sns
import matplotlib.pyplot as plt
import cufflinks as cf
import numpy as np
cf.go_offline()
pd.set_option("display.max_columns", 20)

import os


#%%
frequence='daily'
#frequence='weekly'

art='deviceType'
#art='environment'


#Pfad der einzulesenden csv.-Dateien
path = './data/apicall_{}/{}/'.format(art,frequence)
all_files = glob.glob(path + "/*.csv")
#%%

my_colors = ['darkslateblue','lightgreen',  'darkgreen']



if frequence=='weekly':
    e1='Wöchentliche'
    e2='weekly'
    teilen=1
elif frequence=='daily':
    e1 = 'Tägliche'
    e2 = 'daily'
    teilen=5
elif frequence=='monthly':
    e1 = 'Monatliche'
    e2 = 'monthly'
    teilen=1
else:
    print('Fehler')

#%%
savePath='./data/plots/{}/{}/'.format(art,frequence)
#%%
try:
    os.mkdir(savePath)
except OSError:
    print ("Creation of the directory %s failed" % savePath)
else:
    print ("Successfully created the directory %s " % savePath)

#%%
title = 'Entwicklung: {} Mehrfachnutzung der Abozugänge (SSO-Ids)'.format(e1)

Title1='Entwicklung Zusammensetzung der Mehfachnutzungssegmente \n nach {} ({} Nutzung)'.format(art,e1)
Title2='Zusammensetzung der Mehfachnutzungssegmente nach nach {} \n ({} Nutzung)'.format(art,e1)


#%%
savePath1=savePath+'{}_bar_{}.png'.format(art,e2)
savePath2=savePath+'{}_bar_ges_{}.png'.format(art,e2)
savePath3=savePath+'{}_barpct_{}.png'.format(art,e2)
savePath4=savePath+'{}_barpct_ges_{}.png'.format(art,e2)
savePath5=savePath+'{}_development_bar_{}.png'.format(art,e2)
savePath6=savePath+'{}_development_line_{}.png'.format(art,e2)
savePath7=savePath+'{}_development_bar_pct_{}.png'.format(art,e2)
savePath8=savePath+'{}_development_line_pct_{}.png'.format(art,e2)

#%%
li = []

for filename in all_files:
    print(filename)
    df0 = pd.read_csv(filename, index_col=None, header=0)
    li.append(df0)
dfu = pd.concat(li, axis=0, ignore_index=True)

df=dfu.loc[(dfu['Visits/Visitors']>=2) &
                         (dfu['SSOId']!='Unspecified') &
           (dfu['Visitors']<= 80)]

#%%

# Definition der Segmente anhand Anzahl genutzter Geräte

df.loc[df['Visitors'] <= 2, 'DeviceCount'] = '01-02 Geräte'
df.loc[(df['Visitors']> 2) & (df['Visitors'] <=3), 'DeviceCount'] = '03 Geräte'
df.loc[(df['Visitors']> 3) & (df['Visitors'] <=5), 'DeviceCount'] = '03-05 Geräte'
df.loc[(df['Visitors']> 5) & (df['Visitors'] <=7), 'DeviceCount'] = '06-07 Geräte'
df.loc[(df['Visitors']> 7) & (df['Visitors'] <=10), 'DeviceCount'] = '08-10 Geräte'
df.loc[(df['Visitors']> 10) & (df['Visitors'] <=15), 'DeviceCount'] = '10-15 Geräte'
#df.loc[(df['Visitors']> 15) & (df['Visitors'] <=30), 'DeviceCount'] = '15-30 Geräte'
df.loc[df['Visitors']> 15, 'DeviceCount'] = '> 15 Geräte'

df.loc[df['Visitors'] <= 5, 'DeviceCount2'] = '< 5 Geräte'
df.loc[df['Visitors']> 5, 'DeviceCount2'] = '> 5 Geräte'

#%%
df['StartDay1']=pd.to_datetime(df['StartDay'],format='%Y%m%d')
df['StartDay2']=pd.to_datetime(df['StartDay'],format='%Y%m%d').dt.date

#%%
df_g5=df.loc[df['Visitors']> 5]
df_g5_devices=df_g5[['SSOId','StartDay1','StartDay2','StartDay', 'Visitors', 'VisitorsPhone', 'VisitorsTablet', 'VisitorsDesktop', 'DeviceCount','DeviceCount2']]
df_g5_devices['pctPhone']=df_g5_devices['VisitorsPhone'].div(df_g5_devices['Visitors'])
df_g5_devices['pctDesktop']=df_g5_devices['VisitorsDesktop'].div(df_g5_devices['Visitors'])
df_g5_devices['pctTablet']=df_g5_devices['VisitorsTablet'].div(df_g5_devices['Visitors'])

#%%
df_pct_device=df_g5_devices.groupby('DeviceCount').agg({'pctPhone': 'mean',
                                                        'pctDesktop': 'mean',
                                                        'pctTablet': 'mean',
                                                        'VisitorsPhone': 'mean',
                                                        'VisitorsDesktop': 'mean',
                                                        'VisitorsTablet': 'mean',
                                                        'Visitors': 'mean'})

df_pct_device_ges=df_g5_devices.groupby('DeviceCount2').agg({'pctPhone': 'mean',
                                                        'pctDesktop': 'mean',
                                                        'pctTablet': 'mean',
                                                        'VisitorsPhone': 'mean',
                                                        'VisitorsDesktop': 'mean',
                                                        'VisitorsTablet': 'mean',
                                                        'Visitors': 'mean'})
#df_pct_device=df.groupby('DeviceCount').mean()
#df_counts=df.groupby(['StartDay','DeviceCount'])['Visitors'].count().to_frame()
#df.groupby("Gender").agg({'Age' : 'mean', 'Salary' : 'mean', 'Yr_exp': 'mean'})




df_pct_device['pctPhone2']=df_pct_device['VisitorsPhone'].div(df_pct_device['Visitors'])
df_pct_device['pctDesktop2']=df_pct_device['VisitorsDesktop'].div(df_pct_device['Visitors'])
df_pct_device['pctTablet2']=df_pct_device['VisitorsTablet'].div(df_pct_device['Visitors'])

#%%
#df_pct_device_gesamt=df_g5_devices.agg({'pctPhone': 'mean',
#                                                        'pctDesktop': 'mean',
#                                                        'pctTablet': 'mean',
#                                                        'VisitorsPhone': 'mean',
#                                                       'VisitorsDesktop': 'mean',
#                                                        'VisitorsTablet': 'mean',
#                                                        'Visitors': 'mean'})

#%%
#my_colors = plt.cm.cool(np.linspace(0, 1, 3))

#%%
fig1=plt.figure()
#ax=df_pct_device[['VisitorsDesktop','VisitorsPhone','VisitorsTablet']].plot(kind='bar', stacked=True,color=my_colors)
ax=df_pct_device[['VisitorsDesktop','VisitorsPhone','VisitorsTablet']].plot(kind='bar', color=my_colors)
#for i, t in enumerate(ax.get_xticklabels()):
#    if (i % 1) != 0:
#        t.set_visible(False)
plt.xticks( rotation=0, horizontalalignment="center")
plt.title(Title2)
plt.xlabel('')
plt.ylabel("durchschn. Anzahl")
ax.legend(loc=4)
ax.grid(True)
ax.set_axisbelow(True)
#ax.grid(color='b', linestyle='-', linewidth=1)
plt.legend( ('Desktop', 'Phone', 'Tablet'))
plt.savefig(savePath1)
plt.show()
#%%
#my_colors = plt.cm.cool(np.linspace(0, 1, 3))
#my_colors = ['darkslateblue','lightgreen',  'darkgreen']

fig1=plt.figure()
#ax=df_pct_device[['VisitorsDesktop','VisitorsPhone','VisitorsTablet']].plot(kind='bar', stacked=True,color=my_colors)
ax=df_pct_device_ges[['VisitorsDesktop','VisitorsPhone','VisitorsTablet']].plot(kind='bar', color=my_colors)
plt.xticks( rotation=0, horizontalalignment="center")
plt.title(Title2)
plt.xlabel('')
plt.ylabel("durchschn. Anzahl")
ax.legend(loc=4)
ax.grid(True)
ax.set_axisbelow(True)
#ax.grid(color='b', linestyle='-', linewidth=1)
plt.legend( ('Desktop', 'Phone', 'Tablet'))
plt.savefig(savePath2,bbox_inches='tight')
plt.show()
#%%
fig2=plt.figure()
ax=df_pct_device[['pctDesktop2','pctPhone2','pctTablet2']].plot(kind='bar', stacked=True, color=my_colors)
#for i, t in enumerate(ax.get_xticklabels()):
#    if (i % 1) != 0:
#        t.set_visible(False)
plt.xticks( rotation=0,horizontalalignment="center")
plt.title(Title2)
#plt.xlabel('Starttag')
#plt.ylabel("Anzahl")
ax.legend(loc='upper center')
ax.grid(True)
ax.set_axisbelow(True)
#ax.grid(color='b', linestyle='-', linewidth=1)
plt.legend( ('Desktop', 'Phone', 'Tablet'))
plt.savefig(savePath3,bbox_inches='tight')
plt.show()
#%%
fig1=plt.figure()
#ax=df_pct_device[['VisitorsDesktop','VisitorsPhone','VisitorsTablet']].plot(kind='bar', stacked=True,color=my_colors)
ax=df_pct_device_ges[['pctDesktop','pctPhone','pctTablet']].plot(kind='bar',stacked=True, color=my_colors)
plt.xticks( rotation=0, horizontalalignment="center")
plt.title(Title2)
plt.xlabel('')
plt.ylabel("durchschn. Anzahl")
ax.legend(loc=4)
ax.grid(True)
ax.set_axisbelow(True)
#ax.grid(color='b', linestyle='-', linewidth=1)
plt.legend( ('Desktop', 'Phone', 'Tablet'))
plt.savefig(savePath4,bbox_inches='tight')
plt.show()

#%%
df_startday_device=df_g5_devices.groupby('StartDay2').agg({'pctPhone': 'mean',
                                                        'pctDesktop': 'mean',
                                                        'pctTablet': 'mean',
                                                        'VisitorsPhone': 'sum',
                                                        'VisitorsDesktop': 'sum',
                                                        'VisitorsTablet': 'sum',
                                                        'Visitors': 'sum'})
#                                                             ,
#                                                        'VisitorsPhone': 'sum',
#                                                        'VisitorsDesktop': 'sum',
#                                                        'VisitorsTablet': 'sum',
#                                                        'Visitors': 'sum'
#                                                          })
df_startday_device['pctPhone2']=df_startday_device['VisitorsPhone'].div(df_startday_device['Visitors'])
df_startday_device['pctDesktop2']=df_startday_device['VisitorsDesktop'].div(df_startday_device['Visitors'])
df_startday_device['pctTablet2']=df_startday_device['VisitorsTablet'].div(df_startday_device['Visitors'])

df_startday_device_ges = df_g5_devices.groupby('StartDay1').agg({'pctPhone': 'mean',
                                                             'pctDesktop': 'mean',
                                                             'pctTablet': 'mean',
                                                             'VisitorsPhone': 'sum',
                                                             'VisitorsDesktop': 'sum',
                                                             'VisitorsTablet': 'sum',
                                                             'Visitors': 'sum'})
#                                                             ,
#                                                        'VisitorsPhone': 'sum',
#                                                        'VisitorsDesktop': 'sum',
#                                                        'VisitorsTablet': 'sum',
#                                                        'Visitors': 'sum'
#                                                          })
df_startday_device_ges['pctPhone2'] = df_startday_device_ges['VisitorsPhone'].div(df_startday_device_ges['Visitors'])
df_startday_device_ges['pctDesktop2'] = df_startday_device_ges['VisitorsDesktop'].div(df_startday_device_ges['Visitors'])
df_startday_device_ges['pctTablet2'] = df_startday_device_ges['VisitorsTablet'].div(df_startday_device_ges['Visitors'])

#%%
fig1=plt.figure()
ax=df_startday_device[['VisitorsDesktop','VisitorsPhone','VisitorsTablet']].plot(kind='bar', stacked=True, color=my_colors)
for i, t in enumerate(ax.get_xticklabels()):
    if (i % teilen) != 0:
        t.set_visible(False)
plt.xticks( horizontalalignment="center")
plt.title(Title1)
plt.xlabel('Sarttag')
plt.ylabel("durchschn. Anzahl")
ax.legend(loc=4)
ax.yaxis.grid(True)
ax.set_axisbelow(True)
#ax.grid(color='b', linestyle='-', linewidth=1)
plt.legend( ('Desktop', 'Phone', 'Tablet'))
plt.savefig(savePath5 ,bbox_inches='tight')
plt.show()


#%%
fig1=plt.figure()
ax=df_startday_device_ges[['VisitorsDesktop','VisitorsPhone','VisitorsTablet']].plot( color=my_colors)
for i, t in enumerate(ax.get_xticklabels()):
    if (i % teilen) != 0:
        t.set_visible(False)
plt.xticks( horizontalalignment="center")
plt.title(Title1)
plt.xlabel('Sarttag')
plt.ylabel("durchschn. Anzahl")
ax.legend(loc=4)
ax.yaxis.grid(True)
ax.set_axisbelow(True)
#ax.grid(color='b', linestyle='-', linewidth=1)
plt.legend( ('Desktop', 'Phone', 'Tablet'))
plt.savefig(savePath6 ,bbox_inches='tight')
plt.show()

#%%
fig2=plt.figure()
ax=df_startday_device[['pctDesktop2','pctPhone2','pctTablet2']].plot(kind='bar', stacked=True, color=my_colors)
for i, t in enumerate(ax.get_xticklabels()):
    if (i % teilen) != 0:
        t.set_visible(False)
plt.xticks( horizontalalignment="center")
plt.title(Title1)
plt.xlabel('Starttag')
#plt.ylabel("Anzahl")
plt.legend(loc=3)
ax.yaxis.grid(True)
ax.set_axisbelow(True)
#ax.grid(color='b', linestyle='-', linewidth=1)
plt.legend( ('Desktop', 'Phone', 'Tablet'))
plt.savefig(savePath7,bbox_inches='tight')
plt.show()

#%%
fig2=plt.figure()
ax=df_startday_device_ges[['pctDesktop2','pctPhone2','pctTablet2']].plot( color=my_colors)
#for i, t in enumerate(ax.get_xticklabels()):
#    if (i % teilen) != 0:
#       t.set_visible(False)
plt.xticks( horizontalalignment="center")
plt.title(Title1)
plt.xlabel('Starttag')
#plt.ylabel("Anzahl")
plt.legend(loc=3)
ax.yaxis.grid(True)
ax.set_axisbelow(True)
#ax.grid(color='b', linestyle='-', linewidth=1)
plt.legend( ('Desktop', 'Phone', 'Tablet'))
plt.savefig(savePath8,bbox_inches='tight')
plt.show()