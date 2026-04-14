# =========================================
# 📊 SALES DATA ANALYSIS PROJECT (MASTER CODE)
# =========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# =========================================
# LOAD DATA
# =========================================
def load_data(path):
    try:
        df = pd.read_csv("C:/Users/krunal/superstore_1/superstore.csv")
        print("✅ Data Loaded Successfully\n")
        return df
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

# =========================================
# DATA CLEANING
# =========================================
def clean_data(df):
    print("🧹 Cleaning Data...\n")

    # Handle missing values
    df = df.dropna()

    # Convert Date column
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors='coerce')

    # Remove duplicates
    df = df.drop_duplicates()

    return df

# =========================================
# BASIC INFO
# =========================================
def basic_info(df):
    print("📊 Dataset Info:\n")
    print(df.info())

    print("\n📈 Statistical Summary:\n")
    print(df.describe())

# =========================================
# EDA
# =========================================
def perform_eda(df):
    print("\n🔍 Performing EDA...\n")

    # Correlation Heatmap
    plt.figure()
    sns.heatmap(df.select_dtypes(include=np.number).corr(), annot=True)
    plt.title("Correlation Heatmap")
    plt.show()

    # Sales by Region
    if "Region" in df.columns and "Sales" in df.columns:
        df.groupby("Region")["Sales"].sum().plot(kind='bar')
        plt.title("Sales by Region")
        plt.ylabel("Sales")
        plt.show()

    # Sales Trend
    if "Date" in df.columns and "Sales" in df.columns:
        df.sort_values("Date").groupby("Date")["Sales"].sum().plot()
        plt.title("Sales Trend Over Time")
        plt.ylabel("Sales")
        plt.show()

    # Profit by Product
    if "Product" in df.columns and "Profit" in df.columns:
        df.groupby("Product")["Profit"].sum().plot(kind='bar')
        plt.title("Profit by Product")
        plt.ylabel("Profit")
        plt.show()

# =========================================
# BUSINESS INSIGHTS
# =========================================
def generate_insights(df):
    print("\n🧠 BUSINESS INSIGHTS:\n")

    if "Sales" in df.columns:
        print(f"💰 Total Sales: {df['Sales'].sum():,.2f}")

    if "Profit" in df.columns:
        print(f"📈 Total Profit: {df['Profit'].sum():,.2f}")

    if "Region" in df.columns and "Sales" in df.columns:
        best_region = df.groupby("Region")["Sales"].sum().idxmax()
        print(f"🏆 Best Performing Region: {best_region}")

    if "Product" in df.columns and "Profit" in df.columns:
        top_product = df.groupby("Product")["Profit"].sum().idxmax()
        print(f"🔥 Most Profitable Product: {top_product}")

    if "Sales" in df.columns:
        print(f"📊 Average Sales: {df['Sales'].mean():,.2f}")

# =========================================
# SAVE RESULTS
# =========================================
def save_results(df):
    df.to_csv("cleaned_data.csv", index=False)
    print("\n💾 Cleaned data saved as 'cleaned_data.csv'")

# =========================================
# MAIN FUNCTION
# =========================================
def main():
    print("="*60)
    print("📊 SALES DATA ANALYSIS SYSTEM")
    print("="*60)

    path = input("📂 Enter CSV file path: ").strip().replace('"', '')

    df = load_data(path)
    if df is None:
        return

    df = clean_data(df)

    basic_info(df)

    perform_eda(df)

    generate_insights(df)

    save_results(df)

    print("\n✅ Analysis Complete!")

# =========================================
# RUN
# =========================================
if __name__ == "__main__":
    main()