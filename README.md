# California EV Charging Equity Analysis 

## Overview 
This project analyzes whether public EV charging infrastructure is keeping pace with electric vehicle adoption across California counties, and examines the role income plays in that relationship. 

## Research Question 
Are lower-income California counties being underserved by public charging infrastructure relative to their EV adoption rates?

## Data Sources 
- **EV Registrations:** California DMV via data.ca.gov (2025)
- **Charging Stations:** Alternative Fuels Data Center, U.S. DOE (2025)
- **Per Capita Income:** Bureau of Economic Analysis, CAINC1 (2024)
- **Zip-to-County Crosswalk:** US State County Zip (GitHub)

## Tools & Technologies 
- **SQL / SQLite** - data loading, querying, and aggregation 
- **Python** - pandas, statsmodels, scikit-learn, matplotlib, seaborn
- **Tableau Public** - interactive dashboard 

## Key Findings 
- EV adoption scale is the dominant predictor of charging infrastructure (RF importance: 97.2%), not income
- Income was statistically insignificant in OLS regression (p = 0.278) once EV adoption was controlled for 
- High-income counties like Marin and Santa Clara remain among the most underserved by ports per EV
- Random Forest outperformed OLS in predictive accuracy (RMSE: 0.578 vs 1.443)

## Dashboard 
[California EV Charging Equity — Tableau Public](https://public.tableau.com/app/profile/richie.bhardwaj/viz/CaliforniaEVChargingEquity/Dashboard1)

## Project Structure
```
ev_charging_equity/
├── setup_db.py          # loads CSVs into SQLite database
├── queries.py           # SQL queries for data extraction
├── analysis.ipynb       # full analysis pipeline
├── ev_equity_clean.csv  # cleaned county-level analysis table
├── ev_equity.db         # SQLite database
└── README.md
```

## How to Run
1. Clone the repo
2. Create a virtual environment: `python3 -m venv venv`
3. Activate it: `source venv/bin/activate`
4. Install dependencies: `pip install pandas jupyterlab numpy matplotlib seaborn scikit-learn statsmodels`
5. Run `setup_db.py` to build the database
6. Open `analysis.ipynb` in Jupyter
