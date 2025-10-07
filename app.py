import streamlit as st
import pandas as pd
import pymysql
import plotly.express as px
import folium
from streamlit_folium import st_folium
import json
from streamlit_lottie import st_lottie

#database connection
def create_con():
    try:
        my_con=pymysql.connect(host='127.0.0.1',
                               user='root',
                               password='Jeevanick@91',
                               database='securecheck',
                               cursorclass=pymysql.cursors.DictCursor)
        return my_con
    except Exception as e:
        st.error(f"Error connecting to database:{e}")
        return None
def fetch_data(query):
    connection=create_con()
    if connection:
        try:
            with connection.cursor() as cur:
                cur.execute(query)
                result=cur.fetchall()
                df=pd.DataFrame(result)
                return df
        finally:
            connection.close()
    else:
        return pd.DataFrame()
    
#streamlit UI
def lottie_file(file):
    with open(file,"r", encoding="utf-8") as f:
        return json.load(f)
police=lottie_file("C:/Users/LOQ/Documents/GUVI DS/Project-SecureCheck/icon/Police car.json")
Book=lottie_file("C:/Users/LOQ/Documents/GUVI DS/Project-SecureCheck/icon/Book.json")
presentation=lottie_file("C:/Users/LOQ/Documents/GUVI DS/Project-SecureCheck/icon/presentation.json")
graph=lottie_file("C:/Users/LOQ/Documents/GUVI DS/Project-SecureCheck/icon/graph.json")
Globe2=lottie_file("C:/Users/LOQ/Documents/GUVI DS/Project-SecureCheck/icon/Globe2.json")
sandy=lottie_file("C:/Users/LOQ/Documents/GUVI DS/Project-SecureCheck/icon/sandy.json")
search=lottie_file("C:/Users/LOQ/Documents/GUVI DS/Project-SecureCheck/icon/search.json")
Files=lottie_file("C:/Users/LOQ/Documents/GUVI DS/Project-SecureCheck/icon/Files.json")
badge=lottie_file("C:/Users/LOQ/Documents/GUVI DS/Project-SecureCheck/icon/badge.json")
Motorcycle=lottie_file("C:/Users/LOQ/Documents/GUVI DS/Project-SecureCheck/icon/Motorcycle.json")
st.set_page_config(page_title="SecureCheck Dashboard",layout="wide")

col1,col2,col3=st.columns([0.8,2,15])
with col2:
    st_lottie(
        badge,
        speed=1,
        loop=True,
        width=100,   # small width to fit in line
        height=100,
        key="badge",
        quality="high"
    )
with col3:
    st.title("SecureCheck: Police Check Post Digital Ledger",anchor="center")
st.markdown("👮🏻 Real-Time Monitoring and Insights For Law Inforcement Analysis 🚨")
col1,col2=st.columns([1,13])
with col1:
     st_lottie(
        Book,
        speed=1,
        loop=True,
        width=90,   # small width to fit in line
        height=90,
        key="Book",
        quality="high"
    )
with col2:
    st.header("Police Logs Overview")
qurey="select * from police_logs"
data=fetch_data(qurey)
st.dataframe(data,use_container_width=True)

#column
col1, col2 = st.columns([1, 13])  # adjust ratio for spacing
with col1:
    st_lottie(
        presentation,
        speed=1,
        loop=True,
        width=90,   # small width to fit in line
        height=90,
        key="presentation",
        quality="high"
    )

with col2:
    st.markdown("<h2 style='margin-top:0;'>Key Metrics</h2>", unsafe_allow_html=True)

col1,col2,col3,col4=st.columns(4)

with col1:
    total_stop=data.shape[0]
    st.metric("Total Vechicle Stops",total_stop)
with col2:
    arrest_count=data[data['stop_outcome'].str.contains('Arrest',case=False,na=False)].shape[0]
    st.metric("Total Arrests",arrest_count)
with col3:
    Warning_count=data[data["stop_outcome"].str.contains("Warning",case=False,na=False)].shape[0]
    st.metric("Total Warnings",Warning_count)
with col4:
    drug_found_count=data[data["drugs_related_stop"]==1].shape[0]
    st.metric("Total Drugs Related Stops",drug_found_count)

 #visualizations
col1,col2=st.columns([1,10])
with col1:
     st_lottie(
        graph,
        speed=1,
        loop=True,
        width=90,   # small width to fit in line
        height=90,
        key="graph",
        quality="high"
    )
with col2:
    st.header("Insights")
tab1,tab2=st.tabs(["Stop By Violations","Gender Distribution"])

with tab1:
    if not data.empty and 'violation' in data.columns:
        vol_data=data['violation'].value_counts().reset_index()
        vol_data.columns=['violation','Count']
        fig=px.bar(vol_data,x='violation',y='Count',title="Stop By Violation Type",color='violation',labels={'Count':'Number of Stops','violation':'Violation Types'})
        st.plotly_chart(fig,use_container_width=True)
        #fig2=px.pie(vol_data,names="violation",values="Count",title="Violation Distribution")
        #st.plotly_chart(fig2,use_container_width=True)
    else:
        st.warning("No Data Available for Violation Analysis")
with tab2:
    if not data.empty and 'driver_gender' in data.columns:
        gen_data=data['driver_gender'].value_counts().reset_index()
        gen_data.columns=['Gender','Count']
        fig3=px.bar(gen_data,x='Gender',y='Count',title="Driver Gender Distribution ",color='Gender')
        st.plotly_chart(fig3,use_container_width=True)
    else:
        st.warning("No Data Available for Driver Gender Analysis")
st.markdown("----")   

#map visualization
@st.cache_data
def load_data():
    locations = [
        {"name": "CANADA "
        "Violations Count:21908", "lat": 56.1304, "lon": -106.3468},
        {"name": "INDIA "
        "Violations Count:21998", "lat": 20.5937, "lon": 78.9629},
        {"name": "USA "
        "Violations Count:21632", "lat": 37.0902, "lon": -95.7129}]
        
    m=folium.Map(location=[50,-2],zoom_start=2)
    for loc in locations: 
        folium.Marker(location=[loc['lat'],loc["lon"]],popup=loc['name'],tooltip=loc["name"]).add_to(m)
        
    return m   
map_data=load_data() 
col1,col2=st.columns([1,12])
with col1:
     st_lottie(
        Globe2,
        speed=1,
        loop=True,
        width=90,   # small width to fit in line
        height=90,
        key="Globe2",
        quality="high"
    )
with col2:   
    st.header("Geographical Country Wise Voilations Counts") 
st_folium(map_data,width=1300,height=500)  
st.markdown("-----")
#qurey section
col1,col2=st.columns([1,12])
with col1:
     st_lottie(
        sandy,
        speed=1,
        loop=True,
        width=90,   # small width to fit in line
        height=90,
        key="sandy",
        quality="high"
    )
with col2: 
    st.header("Advanced Insights" )
selected_query=st.selectbox("Select a qurey to Execute",[
    "Top 10 Vehicle Number Involved In Drugs Related Stops",
    "Most Frequently Searched Vehicles",
    "Highest Arrest Rate Driver Age Group",
    "Gender Distribution of Driver Stopped In Each Country",
    "Highest Search Rate In Race And Gender Combination",
    "Most Traffic Stops",
    "Average  Stop Duration For Different Violations",
    "During Night stops Its Lead to Arrest?",
    "Most Associated With Searchs or Arrests",
    "Younger Driver Under 25 In Most violations",
    "Violations Rarly Result in Search Or Arrest",
    "The Country Highest Rate Of Drugs Related Stops",
    "Arrest Rte By Country And Violations",
    "Country Has The Most Stops With Search Conducted",
    "Yearly Count Of Stops And Arrests By Country",
    "Driver Violation Trends Based on Age and Race",
    "Number of Stops by Year, Month, Hour of the Day",
    "Violations with High Search and Arrest Rates",
    "Driver Demographics by Country (Age, Gender, and Race)",
    "Top 5 Violations with Highest Arrest Rates"])

query_map={
    "Top 10 Vehicle Number Involved In Drugs Related Stops":"select vehicle_number from police_logs where drugs_related_stop=1 limit 10;",
    "Most Frequently Searched Vehicles":"select country_name as Country,vehicle_number as Vehicle_Number,violation as Violations,search_type as Search_Type from police_logs where search_type='Vehicle Search';",
    "Highest Arrest Rate Driver Age Group":"select driver_age as Driver_Age, count(stop_outcome) as Arrested_Count from police_logs where stop_outcome='Arrest' group by driver_age order by Arrested_Count desc;",
    "Gender Distribution of Driver Stopped In Each Country":"select country_name as Country, count( driver_gender) as Gender_Distribution_Count from police_logs group by country_name order by Gender_Distribution_Count desc;",
    "Highest Search Rate In Race And Gender Combination":"select driver_race as Race,driver_gender as Gender,concat(round(count(search_type)/21847*100,2),'%') as Search_Rate from police_logs where search_type='vehicle Search' group by driver_race,driver_gender order by Search_Rate;",
    "Most Traffic Stops":"select stop_date as Day , stop_duration as Traffic_Duration,count(stop_duration) as Traffic_Stops from police_logs group by stop_date, stop_duration order by traffic_stops desc;",
    "Average  Stop Duration For Different Violations":"select violation,concat(round(avg(stop_duration),2),' Minutes') as Average_Stop_Duration from police_logs group by violation order by Average_Stop_Duration desc;",
    "During Night stops Its Lead to Arrest?":"select case when hour(stop_time) between 20 and 23 then 'Night' when hour(stop_time) between 0 and 5 then 'Night' else 'Day' end as Time_Period,concat(round(count(stop_outcome)/21734*100,2),'%') as Arrest_Rate from police_logs where stop_outcome='Arrest' group by Time_period;",
    "Most Associated With Searchs or Arrests":"select violation as Violations,count(search_conducted) as Searches_or_Arrests_Counts from police_logs where search_conducted=1 or stop_outcome='Arrest' group by violation order by Searches_or_Arrests_Counts desc;",
    "Younger Driver Under 25 In Most violations":"select violation as Violations, count(driver_age) as Counts_Of_Under_25_Age from police_logs where driver_age<25 group by violation order by Counts_Of_Under_25_Age desc;",
    "Violations Rarly Result in Search Or Arrest":"select  violation as Violations,count(search_conducted) as Rarely_Resulted_Count  from police_logs where search_conducted=0 or stop_outcome='Arrest' group by violation order by Rarely_Resulted_Count limit 1;",
    "The Country Highest Rate Of Drugs Related Stops":"select country_name as Country,concat(round(count(drugs_related_stop)/32769*100,2),'%') as Rate_of_Drugs_Related_Stops from police_logs where drugs_related_stop=1 group by country_name order by Rate_of_Drugs_Related_Stops desc;",
    "Arrest Rate By Country And Violations":"select country_name as Country,violation as Violations,concat(round(count(stop_outcome)/21734*100,2),'%') as Arrest_Rate from police_logs where stop_outcome='Arrest' group by violation,country_name order by Arrest_Rate desc",
    "Country Has The Most Stops With Search Conducted":"select country_name as Country,count(search_conducted) as Search_Count from police_logs where search_conducted=1 group by country_name order by Search_Count desc;",
    "Yearly Count Of Stops And Arrests By Country":"SELECT row_number() over()as S_no,country_name ,EXTRACT(YEAR FROM stop_date) AS Year,COUNT(*) AS Stops_and_Arrests FROM police_logs WHERE stop_outcome = 'Arrest' GROUP BY country_name, EXTRACT(YEAR FROM stop_date) ORDER BY year, Stops_and_Arrests DESC;",
    "Driver Violation Trends Based on Age and Race":"select driver_age,driver_race,count(violation) as Total_Violations from police_logs group by driver_age,driver_race order by driver_age;",
    "Number of Stops by Year, Month, Hour of the Day":"select extract(year from stop_date) as Year,extract(month from stop_date) as Month,extract(hour from stop_date) as Hour,count(*) as Total_stops from police_logs group by Year,Month,Hour;",
    "Violations with High Search and Arrest Rates":"select distinct violation as Violation,count(*) over(partition by violation) as High_Search_and_Arrest from police_logs where search_conducted=1 and stop_outcome='Arrest' order by High_Search_and_Arrest desc limit 1;",
    "Driver Demographics by Country (Age, Gender, and Race)":"SELECT country_name as country,driver_gender as gender,driver_race as race, CASE WHEN driver_age < 18 THEN 'Under 18' WHEN driver_age BETWEEN 18 AND 30 THEN '18-30' WHEN driver_age BETWEEN 31 AND 50 THEN '31-50' WHEN driver_age BETWEEN 51 AND 70 THEN '51-70' ELSE '71+' END AS age_group,COUNT(*) AS driver_count FROM police_logs GROUP BY country, gender, race, age_group ORDER BY country, gender, race, age_group;",
    "Top 5 Violations with Highest Arrest Rates":"select violation,concat(round(count(stop_outcome)/21734*100,2),'%') Arrest_Rate from police_logs where stop_outcome='Arrest' group by violation order by Arrest_Rate desc;"
}
if st.button("Run a Query"):
    result=fetch_data(query_map[selected_query])
    if not result.empty:
        st.dataframe(result,use_container_width=True)
        
    else:
        st.warning("No Data Available For The Selected Query")
st.markdown("----")
st.markdown("Built With 🩷 For Law Enforcement By SecureCheck")
col1,col2=st.columns([1,12])
with col1:
     st_lottie(
        search,
        speed=1,
        loop=True,
        width=100,   # small width to fit in line
        height=100,
        key="search",
        quality="high"
    )
with col2: 
    st.header("Custom Natural Language Filter")
    st.markdown("Fill The Details Below to Get a Natural Language Prediction of The Stop Outcomes Based On Existing Data")
col1,col2=st.columns([1,11])
with col1:
     st_lottie(
        Files,
        speed=1,
        loop=True,
        width=100,   # small width to fit in line
        height=100,
        key="Files",
        quality="high"
    )
with col2:
    st.header("Add New Police Log Entry And Predict Outcome And Violations")

#create form for geting user input
with st.form("New Police Log Entry"):
    stop_date=st.date_input("Stop Date")
    stop_time=st.time_input("Stop Time")
    country_name=st.text_input("Country Name")
    driver_gender=st.selectbox("Driver Gender",['M','F'])
    driver_age=st.number_input("Driver Age",min_value=15,max_value=100,value=25,step=2)
    driver_race=st.text_input("Driver Race")
    search_conducted=st.selectbox("Was a Search Conducted?",['1','0'])
    search_type=st.text_input("Search Type")
    drugs_related_stop=st.selectbox("Was It a Drugs Realted Stop?",['1','0'])
    stop_duration=st.selectbox("Stop duration",data['stop_duration'].dropna().unique())
    vehicle_number=st.text_input("Vehicle Number")
    timestamp=pd.Timestamp.now()

    submitted=st.form_submit_button("🔎Predict Stop Outcome and Violation")
#filter data for prediction

    if submitted:
        filtered_data=data[
            (data['driver_age']==driver_age)&
            (data['driver_gender']==driver_gender)&
            (data['search_conducted']==int(search_conducted))&
            (data['stop_duration']==stop_duration)&
            (data['drugs_related_stop']==int(drugs_related_stop))
            ]
        
        #predict outcome
        if not filtered_data.empty:
            predicted_outcome=filtered_data['stop_outcome'].mode()[0]
            predicted_violation=filtered_data['violation'].mode()[0]
        else:
            predicted_outcome="Warning"
            predicted_violation="speeding"

        #natural Language Summary
        search_text="A Search Was Conducted" if search_conducted=='1' else "No Search Was Conducted"
        drug_text="It Was a Drugs Related Stop" if drugs_related_stop=='1' else "It Was Not a Drugs Related Stop"
        st.markdown("----")
        st.subheader("🚨Prediction Result")
        st.markdown("🚔**Prediction Summary**")
        col1,col2,col3=st.columns([19,23,28])
        with col2:
           st_lottie(
        Motorcycle,
        speed=1,
        loop=True,
        width=600,   # small width to fit in line
        height=300,
        key="Motorcycle",
        quality="high"
    )
        with col3:
          st_lottie(
        police,
        speed=1,
        loop=True,
        width=600,   # small width to fit in line
        height=300,
        key="police1",
        quality="high"
    )
        with col1:   
            st.markdown(f"""
🚦 **Predicted Violation:** `{predicted_violation}`  
📋 **Predicted Outcome:** `{predicted_outcome}`
""")

                    
            st.markdown(f"""
🚗 A **{driver_age}**-year-old **{driver_gender}** driver was stopped in **{country_name}**  
🕒 Time: **{stop_time.strftime('%I:%M %p')}** on **{stop_date}**  
🔍 {search_text} during the stop.  
💊 {drug_text}  
⏱️ Duration: **{stop_duration}**  
🔢 Vehicle Number: **{vehicle_number}**
""")
        
#animation def for local file and url

# def lottie_url(url:str):
#     r=requests.get(url)
#     if r.status_code!=200:
#         return None
#     return r.json()
#police_icon=lottie_url("https://app.lottiefiles.com/share/481bf29d-c0e9-4f35-9510-4b78bfb32150")





