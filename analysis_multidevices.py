#%%
globals().clear()
#%%
import numpy as np
import pandas as pd
import glob
import seaborn as sns
import matplotlib.pyplot as plt
import cufflinks as cf
cf.go_offline()
pd.set_option("display.max_columns", 20)
import os

#%%

#Pfad der einzulesenden csv.-Dateien
path = './data/apicall_deviceType/weekly'
all_files = glob.glob(path + "/*.csv")
#%%
colors={}

colors['1-2 Geräte']='tab:red'
colors['3 Geräte']='tab:blue'
colors['4-5 Geräte']='tab:olive'
colors['6-7 Geräte']='tab:green'
colors['8-10 Geräte']='tab:orange'
colors['10-15 Geräte']='tab:purple'
colors['> 15 Geräte']='tab:cyan'

my_colors1=list(colors.values())
my_label1=list(colors.keys())

my_label3 = [ '6-7 Geräte','8-10 Geräte','10-15 Geräte','> 15 Geräte']
my_colors3 = list(({key: colors[key] for key in my_label3}).values())

colors2={}
colors2['< 5 Geräte']='tab:red'
colors2['> 5 Geräte']='tab:green'

my_colors2=list(colors2.values())
my_label2=list(colors2.keys())




#my_colors2=['tab:green','tab:red' ]
#my_label2=['< 5 Geräte','> 5 Geräte']
#%%

if path=='./data/apicall_deviceType/weekly':
    e1='Wöchentliche'
    e2='weekly'
    teilen=1
elif path=='./data/apicall_multidevices_daily':
    e1 = 'Tägliche'
    e2 = 'daily'
    teilen=5
elif path=='./data/apicall_multidevices_monthly':
    e1 = 'Monatliche'
    e2 = 'monthly'
    teilen=1
else:
    print('Fehler')

#%%
savePath='./data/plots/gesamt/{}/'.format(e2)
#%%
try:
    os.mkdir(savePath)
except OSError:
    print ("Creation of the directory %s failed" % savePath)
else:
    print ("Successfully created the directory %s " % savePath)

#%%
title = 'Entwicklung: {} Mehrfachnutzung der Abozugänge (SSO-Ids)'.format(e1)

savePath1='./data/plots/gesamt/{}/verlauf_{}.png'.format(e2,e2)
savePath1_2='./data/plots/gesamt/{}/verlauf_pct_{}.png'.format(e2,e2)
savePath2='./data/plots/gesamt/{}/bar_{}.png'.format(e2,e2)
savePath3='./data/plots/gesamt/{}/bar_pct_{}.png'.format(e2,e2)
savePath4='./data/plots/gesamt/{}/bar2_{}.png'.format(e2,e2)
savePath5='./data/plots/gesamt/{}/bar_pct2_{}.png'.format(e2,e2)
savePath6='./data/plots/gesamt/{}/verlauf2_{}.png'.format(e2,e2)
savePath6_2='./data/plots/gesamt/{}/verlauf2_pct_{}.png'.format(e2,e2)
savePath7='./data/plots/gesamt/{}/g5_bar_{}.png'.format(e2,e2)
savePath8='./data/plots/gesamt/{}/g5_bar_pct_{}.png'.format(e2,e2)
savePath9='./data/plots/gesamt/{}/g5_verlauf_{}.png'.format(e2,e2)
savePath9_2='./data/plots/gesamt/{}/g5_verlauf_pct_{}.png'.format(e2,e2)
#%%
#Erstellung eines df

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
df.loc[(df['Visitors']> 3) & (df['Visitors'] <=5), 'DeviceCount'] = '04-05 Geräte'
df.loc[(df['Visitors']> 5) & (df['Visitors'] <=7), 'DeviceCount'] = '06-07 Geräte'
df.loc[(df['Visitors']> 7) & (df['Visitors'] <=10), 'DeviceCount'] = '08-10 Geräte'
df.loc[(df['Visitors']> 10) & (df['Visitors'] <=15), 'DeviceCount'] = '10- 15 Geräte'
#df.loc[(df['Visitors']> 15) & (df['Visitors'] <=30), 'DeviceCount'] = '15-30 Geräte'
df.loc[df['Visitors']> 15, 'DeviceCount'] = '> 15 Geräte'

#%%
df.loc[df['Visitors'] <= 5, 'DeviceCount2'] = '< 5 Geräte'
df.loc[df['Visitors']> 5, 'DeviceCount2'] = '> 5 Geräte'

#%%
df['StartDay1']=pd.to_datetime(df['StartDay'],format='%Y%m%d')
df['StartDay2']=pd.to_datetime(df['StartDay'],format='%Y%m%d').dt.date
#df['StartDay']=pd.to_datetime(df.StartDay, format='%Y%m%d').date()
#%%
# Analyse, how many subscribers use more than 5 Devices/accesses

df_counts2=df.groupby(['StartDay2','DeviceCount2'])['Visitors'].count().to_frame()
df_counts=df.groupby(['StartDay2','DeviceCount'])['Visitors'].count().to_frame()

df_counts_unstacked=df_counts.unstack()
df_counts2_unstacked=df_counts2.unstack()

to_plot_transpose = df_counts_unstacked.transpose()
to_plot_transpose2 = df_counts2_unstacked.transpose()

df_counts_unstacked_pct = ((to_plot_transpose.div(to_plot_transpose.sum()))*100).transpose()
df_counts2_unstacked_pct = ((to_plot_transpose2.div(to_plot_transpose2.sum()))*100).transpose()
#df_counts_unstacked_pct=df_counts_unstacked.transpose().div(to_plot_transpose.sum()).transpose()
#df_counts_unstacked_pct=to_plot_transpose_pct.transpose()


#%%
#my_colors=plt.cm.Accent(np.linspace(1, 3, 2))
#rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))

#%%
#Line Plot

fig=plt.figure()
#ax=df_counts_unstacked.plot(kind='bar', stacked=True)
ax=df.groupby(['StartDay1','DeviceCount'])['Visitors'].count().to_frame().unstack().plot(color=my_colors1)
#for i, t in enumerate(ax.get_xticklabels()):
#    if (i % teilen) != 0:
#        t.set_visible(False)
plt.xticks( horizontalalignment="center")
plt.title(title)
plt.xlabel('Starttag')
plt.ylabel("Anzahl")
ax.legend(my_label1)
#ax.legend(loc=4)
ax.yaxis.grid(True)
ax.set_axisbelow(True)
#ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#ax.grid(color='b', linestyle='-', linewidth=1)
#plt.legend( ('< 5 Geräte', '> 5 Geräte'))
plt.savefig(savePath1,bbox_inches='tight')
plt.show()

#%%

# Line Plot pct

fig2 = plt.figure()
ax = ((df.groupby(['StartDay1','DeviceCount'])['Visitors'].count().to_frame().unstack().transpose().
      div(df.groupby(['StartDay1','DeviceCount'])['Visitors'].count().to_frame().unstack().transpose().sum()))*100).transpose()\
    .plot(color=my_colors1)
for i, t in enumerate(ax.get_xticklabels()):
    if (i % teilen) != 0:
        t.set_visible(False)
plt.xticks( horizontalalignment="center")
plt.title(title)
plt.xlabel("Starttag")
plt.ylabel("Anteil [%]")
ax.legend(my_label1, fontsize='small')
ax.yaxis.grid(True)
ax.set_axisbelow(True)
# plt.legend( ('< 5 Geräte', '> 5 Geräte'))
plt.savefig(savePath1_2 ,bbox_inches='tight')
plt.show()
#%%
#my_colors=plt.cm.Accent(np.linspace(1, 3, 2))

#stacked Bar Blot
fig1=plt.figure()
#ax=df_counts_unstacked.plot(kind='bar', stacked=True)
ax=df_counts_unstacked.plot(kind='bar', stacked=True, color=my_colors1)
for i, t in enumerate(ax.get_xticklabels()):
    if (i % teilen) != 0:
        t.set_visible(False)
plt.xticks( horizontalalignment="center")
plt.title(title)
plt.xlabel('Starttag')
plt.ylabel("Anzahl")
ax.legend(my_label1, loc=4)
ax.yaxis.grid(True)
ax.set_axisbelow(True)
#ax.grid(color='b', linestyle='-', linewidth=1)
#plt.legend( ('< 5 Geräte', '> 5 Geräte'))
plt.savefig(savePath2,bbox_inches='tight')
plt.show()


#%%

#stacked Bar Plot pct

fig2=plt.figure()
ax=df_counts_unstacked_pct.plot(kind='bar', stacked=True, color=my_colors1)
for i, t in enumerate(ax.get_xticklabels()):
    if (i % teilen) != 0:
        t.set_visible(False)
plt.xticks(rotation=90, horizontalalignment="center")
plt.title(title)
plt.xlabel("Starttag")
plt.ylabel("Anteil [%]")
ax.legend(my_label1,fontsize='small')
ax.yaxis.grid(True)
ax.set_axisbelow(True)
#plt.legend( ('< 5 Geräte', '> 5 Geräte'))
#plt.savefig(savePath3 ,bbox_inches='tight')
plt.show()

#%%
fig3=plt.figure()
#ax=df_counts2_unstacked.plot(kind='bar', stacked=True,color=['mediumblue','red'])
ax=df_counts2_unstacked.plot(kind='bar', stacked=True, color=my_colors2)
for i, t in enumerate(ax.get_xticklabels()):
    if (i % teilen) != 0:
        t.set_visible(False)
plt.xticks(rotation=90, horizontalalignment="center")
#plt.yticks(step=10)
plt.title(title)
plt.xlabel("Starttag")
plt.ylabel("Anzahl")
#plt.legend( ('< 5 Geräte', '> 5 Geräte'))
ax.legend(my_label2,fontsize='small')
ax.yaxis.grid(True)
ax.set_axisbelow(True)
plt.savefig(savePath4,bbox_inches='tight')
plt.show()

#%%
fig4=plt.figure()
ax=df_counts2_unstacked_pct.plot(kind='bar', stacked=True, color=my_colors2)
plt.xticks(rotation=90, horizontalalignment="center")
for i, t in enumerate(ax.get_xticklabels()):
    if (i % teilen) != 0:
       t.set_visible(False)
plt.title(title)
plt.xlabel("Starttag")
plt.ylabel("Anteil [%]")
ax.legend(my_label2,fontsize='small')
ax.yaxis.grid(True)
ax.set_axisbelow(True)
ax.legend(loc=4)
#ax.yaxis.grid(color='gray')
plt.savefig(savePath5,bbox_inches='tight')
plt.show()
#df.set_index(['WeekStartDay', 'DeviceCount2'], inplace=True)
#df['DeviceCount'] = df.apply(alert, axis=1)

#%%
#Line Plot 2

fig=plt.figure()
#ax=df_counts_unstacked.plot(kind='bar', stacked=True)
ax=df.groupby(['StartDay1','DeviceCount2'])['Visitors'].count().to_frame().unstack().plot(color=my_colors2)
#for i, t in enumerate(ax.get_xticklabels()):
#    if (i % teilen) != 0:
#        t.set_visible(False)
plt.xticks( horizontalalignment="center")
plt.title(title)
plt.xlabel('Starttag')
plt.ylabel("Anzahl")
ax.legend(my_label2)
#ax.legend(loc=4)
ax.yaxis.grid(True)
ax.set_axisbelow(True)
#ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#ax.grid(color='b', linestyle='-', linewidth=1)
#plt.legend( ('< 5 Geräte', '> 5 Geräte'))
plt.savefig(savePath6,bbox_inches='tight')
plt.show()

#%%
# Line Plot pct 2

fig2 = plt.figure()
ax = ((df.groupby(['StartDay1','DeviceCount2'])['Visitors'].count().to_frame().unstack().transpose().
      div(df.groupby(['StartDay1','DeviceCount2'])['Visitors'].count().to_frame().unstack().transpose().sum()))*100).transpose()\
    .plot(color=my_colors2)
for i, t in enumerate(ax.get_xticklabels()):
    if (i % teilen) != 0:
        t.set_visible(False)
plt.xticks( horizontalalignment="center")
plt.title(title)
plt.xlabel("Starttag")
plt.ylabel("Anteil [%]")
ax.legend(my_label2, fontsize='small')
ax.yaxis.grid(True)
ax.set_axisbelow(True)
# plt.legend( ('< 5 Geräte', '> 5 Geräte'))
plt.savefig(savePath6_2 ,bbox_inches='tight')
plt.show()
##%
# Betrachtung der SSO-Ids mit mehr als 5 Geräten pro Woche
#%%
df_g5=df.loc[df['Visitors']> 5]

# Analyse, how many subscribers use more than 5 Devices/accesses


df_g5_counts=df_g5.groupby(['StartDay','DeviceCount'])['Visitors'].count().to_frame()

df_g5_counts_unstacked=df_g5_counts.unstack()
to_plot_transpose_g5 = df_g5_counts_unstacked.transpose()
df_g5_counts_unstacked_pct = ((to_plot_transpose_g5.div(to_plot_transpose_g5.sum()))*100).transpose()

#%%
fig5=plt.figure()
ax=df_g5_counts_unstacked.plot(kind='bar', stacked=True, color=my_colors3)
for i, t in enumerate(ax.get_xticklabels()):
    if (i % teilen) != 0:
        t.set_visible(False)
plt.xticks( horizontalalignment="center")
plt.title(title)
plt.xlabel('Starttag')
plt.ylabel("Anzahl")
ax.legend(my_label3)
ax.yaxis.grid(True)
ax.set_axisbelow(True)
#ax.grid(color='b', linestyle='-', linewidth=1)
#plt.legend( ('< 5 Geräte', '> 5 Geräte'))
plt.savefig(savePath7,bbox_inches='tight')
plt.show()
#%%
fig6=plt.figure()
ax=df_g5_counts_unstacked_pct.plot(kind='bar', stacked=True, color=my_colors3)
for i, t in enumerate(ax.get_xticklabels()):
    if (i % teilen) != 0:
        t.set_visible(False)
plt.xticks(rotation=90, horizontalalignment="center")
plt.title(title)
plt.xlabel("Starttag")
plt.ylabel("Anteil [%]")
ax.legend(my_label3)
ax.yaxis.grid(True)
ax.set_axisbelow(True)
#plt.legend( ('< 5 Geräte', '> 5 Geräte'))
plt.savefig(savePath8,bbox_inches='tight')
plt.show()

#%%
#Line Plot 3

fig=plt.figure()
#ax=df_counts_unstacked.plot(kind='bar', stacked=True)
ax=df_g5.groupby(['StartDay1','DeviceCount'])['Visitors'].count().to_frame().unstack().plot(color=my_colors3)
#for i, t in enumerate(ax.get_xticklabels()):
#    if (i % teilen) != 0:
#        t.set_visible(False)
plt.xticks( horizontalalignment="center")
plt.title(title)
plt.xlabel('Starttag')
plt.ylabel("Anzahl")
ax.legend(my_label3)
#ax.legend(loc=4)
ax.yaxis.grid(True)
ax.set_axisbelow(True)
#ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#ax.grid(color='b', linestyle='-', linewidth=1)
#plt.legend( ('< 5 Geräte', '> 5 Geräte'))
plt.savefig(savePath9,bbox_inches='tight')
plt.show()

#%%
fig2 = plt.figure()
ax = ((df_g5.groupby(['StartDay1','DeviceCount'])['Visitors'].count().to_frame().unstack().transpose().
      div(df_g5.groupby(['StartDay1','DeviceCount'])['Visitors'].count().to_frame().unstack().transpose().sum()))*100).transpose()\
    .plot(color=my_colors3)
for i, t in enumerate(ax.get_xticklabels()):
    if (i % teilen) != 0:
        t.set_visible(False)
plt.xticks( horizontalalignment="center")
plt.title(title)
plt.xlabel("Starttag")
plt.ylabel("Anteil [%]")
ax.legend(my_label3, fontsize='small')
ax.yaxis.grid(True)
ax.set_axisbelow(True)
# plt.legend( ('< 5 Geräte', '> 5 Geräte'))
plt.savefig(savePath9_2 ,bbox_inches='tight')
plt.show()
##%