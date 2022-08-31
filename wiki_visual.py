import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

data= pd.read_excel("final_visual.xlsx")
df=pd.DataFrame(data,columns=['wiki_layer3','Median_difference_x','tag_follower_count',"Average_difference_x",'wiki_Layer2','signal_strength','recurring_cycle'])

def NormalizeData(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))

x = NormalizeData(df["tag_follower_count"])
y1=df['Median_difference_x']
y2=df['Average_difference_x']
y3=NormalizeData(df["signal_strength"])
y4=NormalizeData(df["recurring_cycle"])
y5=df['wiki_Layer2']
val=df['wiki_layer3']

# df1 = pd.DataFrame(np.c_[x,y1,y2,y3,y4],columns=['popularity', 'median_knee','average_knee','signal_strength','recurring_cycle'])
# df2 = pd.DataFrame(np.c_[y1,y3,y4],columns=['median_knee','signal_strength','recurring_cycle'])
#
# sns.pairplot(df2,kind="hist")
# plt.show()

df_sns=pd.DataFrame(np.c_[x,y1],columns=['popularity','median_knee'])
ax = sns.lmplot('popularity', # Horizontal axis
           'median_knee', # Vertical axis
           data=df_sns, # Data source
           fit_reg=False, # Don't fix a regression line
           size = 6,
           aspect =2 ) # size and dimension

plt.title('Example Plot')
# Set x-axis label
plt.xlabel('popularity')
# Set y-axis label
plt.ylabel('median_knee')

def label_point(x, y, val, ax):
    a = pd.concat({'x': x, 'y': y1, 'val': val}, axis=1)
    for i, point in a.iterrows():
        ax.text(point['x']+.01, point['y']-.01, str(point['val']))

label_point(x, y1, val, plt.gca())