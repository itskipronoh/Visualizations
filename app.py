import pandas as pd
from matplotlib import pyplot as plt

def create_pie_chart(data, column, title):
    counts = data[column].value_counts()
    plt.figure(figsize=(8, 6))
    plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140)
    plt.title(title)
    plt.show()

# Load the data into a DataFrame
housing_df = pd.read_csv('/content/housing.csv')

# Generate pie charts for each specified column
create_pie_chart(housing_df, 'hotwaterheating', 'Distribution of Hot Water Heating')
create_pie_chart(housing_df, 'airconditioning', 'Distribution of Air Conditioning')
create_pie_chart(housing_df, 'parking', 'Distribution of Parking')
create_pie_chart(housing_df, 'bathrooms', 'Distribution of Bathrooms')
