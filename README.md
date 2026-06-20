# 🌍 Global Seismic Trends Dashboard

An interactive data analytics dashboard that analyzes global earthquake data using SQL queries and visualizes seismic trends through a Streamlit web application.

---

## 📌 Project Overview

This project explores global earthquake patterns by performing 30 analytical SQL queries on a cleaned earthquake dataset stored in PostgreSQL. The insights are visualized through an interactive Streamlit dashboard with dynamic charts and filters.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| PostgreSQL | Database for storing and querying earthquake data |
| Streamlit | Interactive web dashboard |
| Pandas | Data manipulation and analysis |
| Matplotlib | Data visualization |
| SQLAlchemy | Database connection |

---

## 📁 Project Structure

```
Global-Seismic-Trends/
│
├── app.py                        # Streamlit dashboard application
├── sql_query.ipynb               # 30 SQL analytical queries (Jupyter Notebook)
├── requirements.txt              # Python dependencies
├── Global_Seismic_Trends.pdf     # Project documentation
└── README.md                     # Project overview
```

---

## 📊 Key Features

- ✅ 30 SQL analytical queries covering magnitude, depth, frequency, and regional trends
- ✅ Interactive Streamlit dashboard with dynamic query rendering
- ✅ Charts and visualizations (line, bar, scatter, histogram, map)
- ✅ Deep-focus earthquake analysis (depth > 300 km)
- ✅ Yearly, monthly, and regional trend analysis
- ✅ Tsunami risk and alert level insights

---

## 🚀 How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/Shreejeevanchinnadurai/Global-Seismic-Trends.git
cd Global-Seismic-Trends
```

**2. Create and activate virtual environment**
```bash
python -m venv .venv
.venv\Scripts\activate       # Windows
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up PostgreSQL**
- Create a database named `globalsesmic_db`
- Import your earthquake dataset
- Update the database connection string in `app.py`

**5. Run the Streamlit app**
```bash
streamlit run app.py
```

---

## 📄 Documentation

For detailed project report, methodology, and analysis findings:
👉 [Global_Seismic_Trends.pdf](./Global_Seismic_Trends.pdf)

---

## 🙋‍♂️ Author

**Shreejeevan Chinnadurai**
- 🔗 LinkedIn: [linkedin.com/in/shreejeevan-chinnadurai](https://linkedin.com/in/shreejeevan-chinnadurai)
- 💻 GitHub: [github.com/Shreejeevanchinnadurai](https://github.com/Shreejeevanchinnadurai)
- 🌐 Portfolio: [shreejeevanchinnadurai.github.io/portfolio](https://shreejeevanchinnadurai.github.io/portfolio)

---

## 📃 License

This project is open source and available under the [MIT License](LICENSE).
