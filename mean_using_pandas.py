"""
conducting a basic level statistical analysis using pandas
"""
import pandas as pd
import matplotlib.pyplot as plt

# URL of the CSV file
url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/covid-geography/mmsa-icu-beds.csv"

# Read the CSV data into a Pandas DataFrame
df = pd.read_csv(url)

# Calculate summary statistics for the "total_at_risk" column
total_at_risk_stats = df['total_at_risk'].describe()

# Print the summary statistics
print(total_at_risk_stats)


# Create a DataFrame with your summary statistics
summary_data = pd.DataFrame({
    'Statistic': ['Mean', 'Median', 'Standard Deviation'],
    'Value': [667188.7, 396081.5, 884786.8]
})

# Create a bar chart
plt.figure(figsize=(8, 6))
plt.bar(summary_data['Statistic'], summary_data['Value'], color=['blue', 'green', 'red'])
plt.ylabel('Value')
plt.title('Summary Statistics for "total_at_risk"')
plt.show()

