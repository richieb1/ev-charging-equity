import sqlite3
import pandas as pd

conn = sqlite3.connect('ev_equity.db')

# --- Query 1: EV registrations (Battery Electric + Plug-in Hybrid) by zip code ---
ev_by_zip = pd.read_sql_query("""
    SELECT 
        "ZIP Code" as zip,
        SUM(Vehicles) as ev_count
    FROM ev_registrations
    WHERE Fuel IN ('Battery Electric', 'Plug-in Hybrid')
    GROUP BY "ZIP Code"
""", conn)

# --- Query 2: Charging ports by zip code ---
chargers_by_zip = pd.read_sql_query("""
    SELECT
        ZIP as zip,
        COUNT(*) as station_count,
        SUM(COALESCE("EV Level2 EVSE Num", 0) + 
            COALESCE("EV DC Fast Count", 0)) as total_ports
    FROM charging_stations
    GROUP BY ZIP
""", conn)

# --- Query 3: Per capita income by county (2024 only) ---
income_by_county = pd.read_sql_query("""
    SELECT
        GeoName as county,
        "2024" as per_capita_income
    FROM county_income
    WHERE LineCode = 3
    AND GeoName != 'California'
""", conn)

print("EV registrations sample:")
print(ev_by_zip.head())
print("\nChargers sample:")
print(chargers_by_zip.head())
print("\nIncome sample:")
print(income_by_county.head())

conn.close()