import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

df = pd.read_csv('Data.csv')

def raw_data():
    return df.to_html(index=False)
'''
# Display the plot
plt.show()

df.drop('S.no.', axis =1, inplace = True)
f, ax = plt.subplots(figsize=(10,7))
sns.heatmap(df.corr(), annot = True)
plt.show()
'''


#statewise groundwater reserve
state_list = []
total_frnd_water_recharge = []
curr_gw_extr_list = []
future_available_GW_list = []

#Net Ground Water Availability for future use

for state, subset in df.groupby('Name of State'):
    #print(state, sum(subset['Net Ground Water Availability for future use']))
    state_list.append(state)
    total_frnd_water_recharge.append(sum(subset['Total Annual Ground Water Recharge']))
    curr_gw_extr_list.append(sum(subset['Total Current Annual Ground Water Extraction']))
    future_available_GW_list.append(sum(subset['Net Ground Water Availability for future use'])) 
dfnew = pd.DataFrame({"State":state_list, "GW_Recharge":total_frnd_water_recharge, "GW_Extraction": curr_gw_extr_list, "Future_GW_Available": future_available_GW_list})




dfnew.sort_values(['GW_Recharge','GW_Extraction'], inplace= True)
dfnew['annual_reserve'] = dfnew['GW_Recharge']-dfnew['GW_Extraction']


def fea_data():
    return dfnew.to_html(index=False)




f, ax = plt.subplots(figsize=(10,8))
plt.barh(dfnew['State'],dfnew['annual_reserve'], color=(dfnew['annual_reserve']>0).map({True: 'g',False: 'r'}))


'''
f, ax = plt.subplots(figsize=(10, 9))

sns.set_color_codes("muted")
sns.barplot(x='GW_Recharge', y= 'State', data = dfnew, label = 'Available Ground Water', color='b')
sns.barplot(x='GW_Extraction', y= 'State', data = dfnew, label = 'GroundWater Extraction', color='r')
ax.legend(ncol=2, loc="lower right", frameon=True)
plt.show()


# In[20]:


dfnew.sort_values('Future_GW_Available', inplace = True)
f, ax = plt.subplots(figsize=(10, 10))
sns.barplot(x='Future_GW_Available', y = 'State',data = dfnew)
plt.show()


# In[23]:


dfnew.count()

'''
# In[26]:

'''
#lets do for telangana
df_telangana = df[df['Name of State']=='TELANGANA']
df_telangana.head()


# In[33]:
'''
def generate_plots1(data):
    value = str(data)
    f, ax = plt.subplots(figsize=(9, 7))
    sns.barplot( x = 'Annual GW Allocation for Domestic Use as on 2025', y = 'Name of District', data = df[df['Name of State']==value])
    bytes_image1 = io.BytesIO()
    plt.savefig(bytes_image1, format='png')
    bytes_image1.seek(0)
    base64_image1 = base64.b64encode(bytes_image1.getvalue()).decode('utf-8')
    return base64_image1

def generate_plots2(data):
    value = str(data)
    plt.figure(figsize=(9,7))
    sns.barplot(x='Recharge from rainfall During Monsoon Season', y='Name of State', data = df)
    bytes_image2 = io.BytesIO()
    plt.savefig(bytes_image2, format='png')
    bytes_image2.seek(0)
    base64_image2 = base64.b64encode(bytes_image2.getvalue()).decode('utf-8')
    return base64_image2
'''
# In[45]:


fig,axs = plt.subplots(6,6,figsize=(12,8))

for idx,state in enumerate(df['Name of State'].value_counts().sort_values(ascending=False)[0:36].index):
    #print(idx,state)
    axs[idx//6,idx%6].hist(x = df[df['Name of State']==state]['Stage of Ground Water Extraction (%)'], color='b')
    axs[idx//6,idx%6].set_title(state)
plt.suptitle("State wise GW Extraction distribution")
plt.tight_layout()
fig.subplots_adjust(top=0.88)
plt.show()

'''
