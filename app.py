import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# =========================
# DATABASE CONNECTION
# =========================
engine = create_engine(
    "postgresql+psycopg2://postgres:shree@localhost:5432/globalsesmic_db"
)

st.markdown("""
<h1 style='
text-align: center;
font-size: 55px;
font-weight: 800;
color: #38bdf8;
margin-bottom: 0px;
'>
🌍 Global Seismic Trends Dashboard
</h1>
""", unsafe_allow_html=True)



st.set_page_config(
    page_title="Global Seismic Trends Dashboard",
    page_icon="🌍",
    layout="wide"
)

# PASTE CSS HERE
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}

[data-testid="metric-container"] {
    background: linear-gradient(135deg,#2563eb,#7c3aed);
    padding:15px;
    border-radius:15px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="main-title">🌍 Global Seismic Trends Dashboard</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

total_eq = pd.read_sql(
    "SELECT COUNT(*) AS total FROM earthquakes",
    engine
)

avg_mag = pd.read_sql(
    "SELECT ROUND(AVG(mag)::numeric,2) AS avg_mag FROM earthquakes",
    engine
)

max_mag = pd.read_sql(
    "SELECT MAX(mag) AS max_mag FROM earthquakes",
    engine
)

countries = pd.read_sql(
    "SELECT COUNT(DISTINCT country) AS countries FROM earthquakes",
    engine
)
st.success(
    "📊 Explore earthquake magnitudes, tsunami alerts, seismic trends and deep-focus events worldwide."
)
col1.metric("🌎 Total Earthquakes", int(total_eq.iloc[0, 0]))
col2.metric("🌊 Average Magnitude", avg_mag.iloc[0, 0])
col3.metric("🌋 Maximum Magnitude", max_mag.iloc[0, 0])
col4.metric("🌍 Countries Affected", int(countries.iloc[0, 0]))

st.divider()



queries = {

1: """SELECT place, mag
      FROM earthquakes
      ORDER BY mag DESC
      LIMIT 10""",

2: """SELECT place,depth_km
      FROM earthquakes
      WHERE mag > 7.0
      ORDER BY depth_km DESC
      LIMIT 10""",

3: """SELECT depth_km,place,mag
      FROM earthquakes
      WHERE depth_km < 50
      AND mag > 7.5
      ORDER BY mag DESC""",

5: """SELECT "magType",
             AVG(mag) AS avg_magnitude
      FROM earthquakes
      GROUP BY "magType"
      ORDER BY avg_magnitude DESC""",

6: """SELECT year,
             COUNT(*) AS total_earthquakes
      FROM earthquakes
      GROUP BY year
      ORDER BY year DESC""",

7: """SELECT month,
             COUNT(*) AS total_earthquakes
      FROM earthquakes
      GROUP BY month
      ORDER BY total_earthquakes DESC""",

8: """SELECT day_of_week,
             COUNT(*) AS total_earthquakes
      FROM earthquakes
      GROUP BY day_of_week
      ORDER BY total_earthquakes DESC""",

9: """SELECT EXTRACT(HOUR FROM time::TIMESTAMP) AS hour_of_day,
             COUNT(*) AS total_earthquakes
      FROM earthquakes
      GROUP BY hour_of_day
      ORDER BY hour_of_day""",

10: """SELECT net,
              COUNT(*) AS total_earthquakes
       FROM earthquakes
       GROUP BY net
       ORDER BY total_earthquakes DESC
       LIMIT 10""",

11: """SELECT country,
              sig,
              felt,
              mag,
              depth_km
       FROM earthquakes
       ORDER BY felt DESC
       LIMIT 5""",
13: """SELECT alert, COUNT(*) AS count
        FROM earthquakes
        GROUP BY alert""",

14: """SELECT status,
              COUNT(*) AS total_earthquakes
       FROM earthquakes
       GROUP BY status""",

15: """SELECT type,
              COUNT(*) AS total_earthquakes
       FROM earthquakes
       GROUP BY type""",

16: """SELECT types,
              COUNT(*) AS total_earthquakes
       FROM earthquakes
       GROUP BY types""",

18: """SELECT place,
              mag,
              nst
       FROM earthquakes
       WHERE nst IS NOT NULL
       ORDER BY nst DESC
       LIMIT 10""",

19: """SELECT year,
              tsunami,
              COUNT(*) AS total_earthquakes
       FROM earthquakes
       GROUP BY year, tsunami
       ORDER BY year DESC""",

20: """SELECT alert,
              COUNT(*) AS total_earthquakes
       FROM earthquakes
       GROUP BY alert
       ORDER BY alert""",

21: """SELECT country,
              AVG(mag) AS average_magnitude
       FROM earthquakes
       GROUP BY country
       ORDER BY average_magnitude DESC
       LIMIT 5""",

22: """SELECT year,
              month,
              COUNT(CASE WHEN depth_flag='Shallow' THEN 1 END) AS shallow_count,
              COUNT(CASE WHEN depth_flag='Deep' THEN 1 END) AS deep_count
       FROM earthquakes
       GROUP BY year, month
       HAVING COUNT(CASE WHEN depth_flag='Shallow' THEN 1 END) > 0
       AND COUNT(CASE WHEN depth_flag='Deep' THEN 1 END) > 0
       ORDER BY year""",

23: """SELECT year,
              COUNT(*) AS total_earthquakes
       FROM earthquakes
       GROUP BY year
       ORDER BY year""",

24: """SELECT place,
              COUNT(*) AS frequency,
              ROUND(AVG(mag)::numeric,2) AS avg_magnitude
       FROM earthquakes
       GROUP BY place
       ORDER BY frequency DESC, avg_magnitude DESC
       LIMIT 10""",

25: """SELECT country,
              AVG(depth_km) AS average_depth,
              COUNT(*) AS total_earthquakes
       FROM earthquakes
       WHERE latitude BETWEEN -5 AND 5
       GROUP BY country
       ORDER BY average_depth DESC""",

26: """SELECT country,
              COUNT(CASE WHEN depth_flag='Shallow' THEN 1 END) AS shallow_count,
              COUNT(CASE WHEN depth_flag='Deep' THEN 1 END) AS deep_count,
              ROUND(
                COUNT(CASE WHEN depth_flag='Shallow' THEN 1 END)::NUMERIC /
                NULLIF(COUNT(CASE WHEN depth_flag='Deep' THEN 1 END),0),
                2
              ) AS shallow_to_deep_ratio
       FROM earthquakes
       GROUP BY country
       HAVING COUNT(CASE WHEN depth_flag='Deep' THEN 1 END) > 0
       ORDER BY shallow_to_deep_ratio DESC
       LIMIT 10""",

27: """SELECT
       ROUND(AVG(CASE WHEN tsunami=1 THEN mag END)::NUMERIC,2) AS avg_mag_with_tsunami,
       ROUND(AVG(CASE WHEN tsunami=0 THEN mag END)::NUMERIC,2) AS avg_mag_without_tsunami,
       ROUND(
           (
           AVG(CASE WHEN tsunami=1 THEN mag END) -
           AVG(CASE WHEN tsunami=0 THEN mag END)
           )::NUMERIC,2
       ) AS magnitude_difference
       FROM earthquakes""",

28: """SELECT place,
              gap,
              rms,
              mag
       FROM earthquakes
       WHERE gap IS NOT NULL
       AND rms IS NOT NULL
       ORDER BY gap DESC, rms DESC
       LIMIT 10""",

30: """SELECT
    place,
    COUNT(*) AS total_earthquakes,
    AVG(depth_km) AS avg_depth,
    MAX(depth_km) AS max_depth,
    AVG(mag) AS avg_magnitude
FROM earthquakes
WHERE depth_km > 300
GROUP BY place
ORDER BY total_earthquakes DESC;"""
}


questions = {
    "1. Top 10 Strongest Earthquakes": 1,
    "2. Top 10 Deepest Earthquakes": 2,
    "3. Shallow Earthquakes (<50km & Mag>7.5)": 3,
    "4. Average Depth Per Continent": 4,
    "5. Average Magnitude Per Magnitude Type": 5,
    "6. Year With Most Earthquakes": 6,
    "7. Month With Highest Number Of Earthquakes": 7,
    "8. Day Of Week With Most Earthquakes": 8,
    "9. Earthquakes Per Hour": 9,
    "10. Most Active Reporting Network": 10,
    "11. Top 5 Places With Highest Casualties": 11,
    "12. Economic Loss Per Continent": 12,
    "13. Economic Loss By Alert Level": 13,
    "14. Reviewed Vs Automatic": 14,
    "15. Earthquake Types": 15,
    "16. Earthquake Data Types": 16,
    "17. Average RMS & Gap": 17,
    "18. High Station Coverage Events": 18,
    "19. Tsunamis Triggered Per Year": 19,
    "20. Earthquakes By Alert Levels": 20,
    "21. Top 5 Countries By Average Magnitude": 21,
    "22. Shallow And Deep Earthquakes In Same Month": 22,
    "23. Year Over Year Growth": 23,
    "24. Most Seismically Active Regions": 24,
    "25. Average Depth Near Equator": 25,
    "26. Highest Shallow To Deep Ratio": 26,
    "27. Magnitude Difference (Tsunami vs Non-Tsunami)": 27,
    "28. Lowest Data Reliability Events": 28,
    "29. Consecutive Earthquakes Within 50km": 29,
    "30. Deep Focus Earthquakes": 30
}

st.divider()
st.subheader("📊 Select Analysis Question")

selected_question = st.selectbox(
    "Choose Question",
    list(questions.keys())
)

question_number = questions[selected_question]

st.subheader(selected_question)

if question_number in [4, 12, 17, 29]:

    st.info("Required data not available in dataset.")

else:

    df = pd.read_sql(
        queries[question_number],
        engine
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    # Charts

    if question_number in [5, 8, 9, 10, 20]:

        st.bar_chart(
            df.set_index(df.columns[0])
        )

    elif question_number in [6, 23]:

        st.line_chart(
            df.set_index(df.columns[0])
        )

    elif question_number == 19:

        st.area_chart(
            df.set_index(df.columns[0])
        )