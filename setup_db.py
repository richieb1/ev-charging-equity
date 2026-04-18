import sqlite3
import pandas as pd

conn = sqlite3.connect('ev_equity.db')

# Load CSVs
stations = pd.read_csv('charging_stations.csv', low_memory=False)
registrations = pd.read_csv('ev_registrations.csv', low_memory=False)
income = pd.read_csv('county_income.csv', encoding='latin1')

# Write raw tables to SQLite
stations.to_sql('charging_stations', conn, if_exists='replace', index=False)
registrations.to_sql('ev_registrations', conn, if_exists='replace', index=False)
income.to_sql('county_income', conn, if_exists='replace', index=False)

print("Tables loaded:")
for row in conn.execute("SELECT name FROM sqlite_master WHERE type='table'"):
    print(" -", row[0])

conn.close()