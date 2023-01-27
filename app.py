import pandas as pd
import streamlit as st


st.set_page_config(page_title='Hourly Energy Consumption',
                   page_icon=':bar_char:',
                   layout='wide')


@st.cache
def get_data():
    df = pd.read_csv('data/AEP_hourly.csv', parse_dates=['Datetime'], index_col='Datetime')  
    df["year"] = df.index.year
    df["month"] = df.index.month
    df["week"] = df.index.isocalendar().week.astype(int)
    df["day_of_week"] = df.index.isocalendar().day.astype(int)
    df["day_of_year"] = df.index.dayofyear
    df["day_of_month"] = df.index.day
    df["hour"] = df.index.hour 
    df["date"] = df.index.date 
    df['day_name'] = df.index.day_name()
    df['month_name'] = df.index.month_name()
    
    return df

df = get_data()    

"""
# Hourly Energy Consumption
Over 10 years of hourly energy consumption data from PJM in Megawatts

## About Dataset
## PJM Hourly Energy Consumption Data
PJM Interconnection LLC (PJM) is a regional transmission organization (RTO) in the United States. It is part of the Eastern Interconnection grid operating an electric transmission system serving all or parts of Delaware, Illinois, Indiana, Kentucky, Maryland, Michigan, New Jersey, North Carolina, Ohio, Pennsylvania, Tennessee, Virginia, West Virginia, and the District of Columbia.

The hourly power consumption data comes from PJM's website and are in megawatts (MW).

The regions have changed over the years so data may only appear for certain dates per region.

src: https://www.kaggle.com/datasets/robikscube/hourly-energy-consumption
"""

st.sidebar.header('Please Filter Here')

year = st.sidebar.multiselect(
    'Select the Year',
    options=df['year'].unique(),
    default=df['year'].unique()
)

month_name = st.sidebar.multiselect(
    'Select the Month Name',
    options=df['month_name'].unique(),
    default=df['month_name'].unique()
)

day_name = st.sidebar.multiselect(
    'Select the Day Name',
    options=df['day_name'].unique(),
    default=df['day_name'].unique()
)

df_selection = df.query(
    'year == @year & day_name == @day_name & month_name == @month_name'
)

daily_trends = df_selection.pivot_table(index=df_selection['hour'], 
                     columns='day_name', 
                     values='AEP_MW',
                     aggfunc='sum')
                     
                     
monthly_trends = df_selection.pivot_table(index=df_selection['hour'], 
                     columns='month_name', 
                     values='AEP_MW',
                     aggfunc='sum')
                     
annual_comparison = df_selection.groupby(['year'])['AEP_MW'].sum()


with st.container():  
    tab1, tab2 = st.tabs(["Charts", "Data"])
       
    with tab1:
        """ 
        ## AEP - Daily Trends
        """
                
        st.line_chart(daily_trends)
        
        """ 
        ## AEP - Monthly Trends
        """    
        st.line_chart(monthly_trends)
        
        """ 
        ## AEP - Annual Comparison
        """    
        st.bar_chart(annual_comparison)
                
    with tab2:
        """ 
        ## AEP_hourly Dataset
        """
        df_selection 
        