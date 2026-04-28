# 🚔 SecureCheck: Police Check Post Digital Ledger

> Real-Time Monitoring and Insights For Law Enforcement Analysis

---

## 📌 Project Overview

**SecureCheck** is an interactive data dashboard built with **Streamlit** that digitizes and visualizes police check post logs. It enables law enforcement analysts to monitor vehicle stops, analyze violation patterns, explore demographic trends, and predict stop outcomes — all in real time through a clean, animated web interface.

---

## 🖥️ Project Screenshots

### 1. Dashboard Home & Police Logs Overview
![Dashboard Home](screenshots/p1.png)

### 2. Key Metrics Panel
![Key Metrics](screenshots/p2.png)

### 3. Stop by Violation Type – Bar Chart
![Violation Chart](screenshots/p3.png)

### 4. Gender Distribution of Drivers
![Gender Distribution](screenshots/p4.png)

### 5. Geographical Country-Wise Violations Map
![Geo Map](screenshots/p5.png)

### 6. Predict Stop Outcome – Natural Language Filter
![Prediction Form](screenshots/p6.png)

---

## ✨ Features

- **Police Logs Overview** — Full database table rendered interactively using Streamlit's `st.dataframe`.
- **Key Metrics** — At-a-glance KPIs: Total Vehicle Stops, Total Arrests, Total Warnings, Drug-Related Stops.
- **Visual Insights** — Interactive Plotly bar charts for violation types and gender distribution.
- **Geographical Map** — Folium-powered world map displaying country-wise violation counts (USA, India, Canada).
- **Advanced SQL Insights** — 20 pre-built analytical queries selectable from a dropdown, covering arrest rates, search patterns, demographic trends, and more.
- **Predict Stop Outcome** — A smart form that filters historical data to predict the likely violation and stop outcome for a new log entry, along with a natural language narrative summary.
- **Lottie Animations** — Smooth, looping animations throughout the UI for a polished look.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend / UI | Streamlit |
| Database | MySQL (via PyMySQL) |
| Data Processing | Pandas |
| Visualizations | Plotly Express |
| Maps | Folium + streamlit-folium |
| Animations | Lottie + streamlit-lottie |
| Language | Python 3.x |

---

## 🗃️ Database

- **Database Name:** `securecheck`
- **Table:** `police_logs`
- **Key Columns:**
  - `stop_date`, `stop_time`, `country_name`
  - `driver_gender`, `driver_age`, `driver_race`
  - `violation`, `stop_outcome`, `stop_duration`
  - `search_conducted`, `search_type`
  - `drugs_related_stop`, `vehicle_number`

---

## 📂 Project Structure

```
Project-Police Secure Check 01/
│
├── app.py                    # Main Streamlit application
├── icon/                     # Lottie animation JSON files
│   ├── Police car.json
│   ├── Book.json
│   ├── presentation.json
│   ├── graph.json
│   ├── Globe2.json
│   ├── sandy.json
│   ├── search.json
│   ├── Files.json
│   ├── badge.json
│   └── Motorcycle.json
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/securecheck-dashboard.git
cd securecheck-dashboard
```

### 2. Install Dependencies
```bash
pip install streamlit pandas pymysql plotly folium streamlit-folium streamlit-lottie
```

### 3. Configure the Database
Update the database credentials in `app.py`:
```python
my_con = pymysql.connect(
    host='127.0.0.1',
    user='your_username',
    password='your_password',
    database='securecheck',
    cursorclass=pymysql.cursors.DictCursor
)
```

### 4. Update Lottie File Paths
Update the absolute paths to your local `icon/` directory in `app.py`:
```python
police = lottie_file("path/to/icon/Police car.json")
```

### 5. Run the App
```bash
streamlit run app.py
```

---

## 📊 Advanced SQL Queries Included

| # | Query |
|---|---|
| 1 | Top 10 Vehicle Numbers Involved in Drug-Related Stops |
| 2 | Most Frequently Searched Vehicles |
| 3 | Highest Arrest Rate Driver Age Group |
| 4 | Gender Distribution by Country |
| 5 | Highest Search Rate by Race & Gender |
| 6 | Most Traffic Stops by Day |
| 7 | Average Stop Duration by Violation |
| 8 | Night Stops Leading to Arrest |
| 9 | Violations Most Associated with Searches or Arrests |
| 10 | Younger Drivers (Under 25) in Most Violations |
| 11 | Violations Rarely Resulting in Search or Arrest |
| 12 | Country with Highest Drug-Related Stop Rate |
| 13 | Arrest Rate by Country and Violation |
| 14 | Country with Most Stops with Search Conducted |
| 15 | Yearly Count of Stops and Arrests by Country |
| 16 | Driver Violation Trends by Age and Race |
| 17 | Number of Stops by Year, Month, Hour |
| 18 | Violations with High Search and Arrest Rates |
| 19 | Driver Demographics by Country (Age, Gender, Race) |
| 20 | Top 5 Violations with Highest Arrest Rates |

---

## 🔮 Predict Stop Outcome

The prediction form collects the following inputs and matches them against historical records:

- Stop Date & Time
- Country Name
- Driver Gender, Age & Race
- Search Conducted (Yes/No)
- Search Type
- Drugs-Related Stop (Yes/No)
- Stop Duration
- Vehicle Number

**Output:** Predicted violation type, predicted stop outcome, and a natural language narrative summary of the stop.

---

## 🌍 Geographical Coverage

| Country | Violations Count |
|---|---|
| India | 21,998 |
| Canada | 21,908 |
| USA | 21,632 |

---

## 📝 Notes

- Ensure your MySQL server is running locally before launching the app.
- All Lottie animation files must be available at the configured local paths.
- The prediction engine is rule-based (data filtering), not an ML model. It matches inputs against existing records.

---

## 🩷 Built With Love For Law Enforcement By SecureCheck
