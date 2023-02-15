import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt

st.set_page_config(layout="wide")


st.title('Data Exploration App')

st.header('Created by Syed Suhaib')

df = pd.read_csv(r'C:\\Users\\Laptop_Zone\\Desktop\\Data Course\\Python - Last Assignment\\Olympicsdata.csv')
df1 = pd.read_csv(r'C:\\Users\\Laptop_Zone\\Desktop\\Data Course\\Python - Last Assignment\\noc_regions.csv')


age_mean = df['Age'].mean()

df['Age'] = df['Age'].fillna(age_mean)

height_mean = df['Height'].mean()

df['Height'] = df['Height'].fillna(height_mean)

weight_mean = df['Weight'].mean()

df['Weight'] = df['Weight'].fillna(weight_mean)

df['Medal'] = df['Medal'].fillna('No Medal')

merged=df.merge(df1, on='NOC',how='left')

a = pd.to_datetime(df['Year'])

# olympic_year = sorted(df['Year'].unique())
cntry = merged['region'].unique()



country = st.selectbox('Select year', cntry)

# st.table(df)

# olympic_noc = sorted(df['NOC'].unique())
# noc = st.selectbox('Select Team', olympic_noc)

unique = df['Name'].unique()
curr_count = len(unique)

# curr_count = df['ID'].unique()
st.header('Olympics - {}'.format(country))

medals = df['Medal'].value_counts()

gold = medals[1].astype(str)
bronze = medals[2].astype(str)
silver = medals[3].astype(str)


col1, col2, col3, col4= st.columns(4)
col1.metric('Number of Olympians', curr_count)
col2.metric('Gold Medals', gold)
col3.metric('Silver Medals', silver)
col4.metric('Bronze Medals', bronze)


#number of athletes over time

# df2 = df.groupby(['Medal'])['Medal'].count()
# df3 = df.groupby(['Year'])['Medal'].count()

# # plt.plot(df['Year'])
# plt.plot(, df2)
# plt.xlabel('Year')
# plt.ylabel('Medal')
# plt.title('Medal in Year')
# st.pyplot()

# chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c'])
# right.header('Line Chart Visual')
# right.line_chart(chart_data)

# df['Year']=pd.to_datetime(df['Year'])
time = df['Year']
value=df['Medal']

dfg=df.groupby(['Year', 'Medal']).Medal.count().reset_index(name='counts')
dfp = dfg.pivot(index='Year', columns='Medal', values='counts')

dfgg=df.groupby(['Name', 'Medal']).Medal.count().reset_index(name='counts')
dfpp = dfgg.pivot(index='Name', columns='Medal', values='counts')
dfpp['total'] = dfpp.sum(axis=1)
dfpp=dfpp.sort_values(by=['total'], ascending=False)
dfpp=dfpp.head()

dfggg=df.groupby(['Sport', 'Medal']).Medal.count().reset_index(name='counts')
dfppp = dfggg.pivot(index='Sport', columns='Medal', values='counts')
dfppp['total'] = dfppp.sum(axis=1)
dfppp=dfppp.sort_values(by=['total'], ascending=False)
dfppp=dfppp.head()

dfgg1=df.groupby(['Age', 'Medal']).Medal.count().reset_index(name='counts')
dfpp1 = dfgg1.pivot(index='Age', columns='Medal', values='counts')
dfpp1['total'] = dfpp1.sum(axis=1)
dfpp1=dfpp1[['total']]

dfgg2=df.groupby(['Sex', 'Medal']).Medal.count().reset_index(name='counts')
dfpp2 = dfgg2.pivot(index='Sex', columns='Medal', values='counts')
dfpp2['total'] = dfpp2.sum(axis=1)
dfpp2=dfpp2[['total']]

dfgg3=df.groupby(['Season', 'Medal']).Medal.count().reset_index(name='counts')
dfpp3 = dfgg3.pivot(index='Season', columns='Medal', values='counts')
dfpp3['total'] = dfpp3.sum(axis=1)
dfpp3=dfpp3[['total']]



with st.container():
    left, middle, right = st.columns(3)
    

    left.header('Medal distribution per year')
    fig, ax = plt.subplots()
    plt.plot(dfp)
    left.pyplot(fig)
    
    
    middle.header('Players with most medals')
    fig, ax = plt.subplots()
    plt.barh(dfpp.index,dfpp['total'])
    middle.pyplot(fig)
    
    right.header('Sports with most medals')
    # fig, ax = plt.subplots()
    # plt.barh(dfppp.index,dfppp['total'])
    right.table(dfppp)
    

with st.container():
    left, middle, right = st.columns(3)
    
    left.header('No of medals per age')
    fig, ax = plt.subplots()
    ax.hist(dfpp1, bins=10)

    left.pyplot(fig)
    
    middle.header('No of medals per gender')
    fig1, ax1 = plt.subplots()
    ax1.pie(dfpp2.total, labels=dfpp2.index, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    middle.pyplot(fig1) 
    
    right.header('No of medals in each season')
    fig, ax = plt.subplots()
    plt.bar(dfpp3.index,dfpp3['total'])
    right.pyplot(fig)
    
    

        

    