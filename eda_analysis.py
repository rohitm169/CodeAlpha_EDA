import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset created in Task 1
df = pd.read_csv('books_dataset.csv')

# 2. Explore Data Structure
print("=== Dataset Information ===")
print(df.info())
print("\n=== First 5 Rows ===")
print(df.head())

# 3. Data Cleaning and Preprocessing
# Remove '$' sign from Price and convert to float
df['Price_Clean'] = df['Price'].str.replace('$', '').astype(float)

# Convert Word Ratings to Numeric values
rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
df['Rating_Numeric'] = df['Rating'].map(rating_map)

# Check for missing values
print("\n=== Missing Values Check ===")
print(df.isnull().sum())

# 4. Statistical Summary
print("\n=== Summary Statistics ===")
print(df[['Price_Clean', 'Rating_Numeric']].describe())

# 5. Data Analysis & Insights
avg_price = df['Price_Clean'].mean()
print(f"\nAverage Book Price: ${avg_price:.2f}")

avg_price_by_rating = df.groupby('Rating_Numeric')['Price_Clean'].mean()
print("\n=== Average Price by Rating ===")
print(avg_price_by_rating)

# 6. Visualizations
plt.figure(figsize=(14, 5))

# Plot 1: Price Distribution
plt.subplot(1, 2, 1)
sns.histplot(df['Price_Clean'], kde=True, color='skyblue')
plt.title('Distribution of Book Prices')
plt.xlabel('Price ($)')
plt.ylabel('Frequency')

# Plot 2: Book Count by Rating
plt.subplot(1, 2, 2)
sns.countplot(x='Rating', data=df, order=['One', 'Two', 'Three', 'Four', 'Five'], palette='viridis')
plt.title('Count of Books by Rating')
plt.xlabel('Rating')
plt.ylabel('Number of Books')

plt.tight_layout()

# Save Visualizations as Image
plt.savefig('eda_plots.png')
print("\nVisualization plots saved successfully as 'eda_plots.png'.")

# Display Plots
plt.show()