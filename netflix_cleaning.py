import pandas as pd

# Load the raw dataset
df = pd.read_csv("netflix_titles.csv")

# Display initial dataset shape and structure
print("Initial Shape:", df.shape)
print("\nInitial Data Info:\n", df.info())

# 1. Remove duplicate rows
df = df.drop_duplicates()
print("\nShape after removing duplicates:", df.shape)

# 2. Handle missing values
print("\nMissing values before handling:\n", df.isnull().sum())

# Fill missing 'rating' values using forward fill method
df['rating'] = df['rating'].fillna(method='ffill')

# Replace missing values in 'country' and 'director' with "Unknown"
df['country'] = df['country'].fillna('Unknown')
df['director'] = df['director'].fillna('Unknown')

# Drop rows with missing 'date_added' (optional)
df = df.dropna(subset=['date_added'])

# 3. Convert 'date_added' to datetime format
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# 4. Standardize text values (trim spaces, fix case)
df['type'] = df['type'].str.strip().str.lower()
df['rating'] = df['rating'].str.strip().str.upper()
df['country'] = df['country'].str.strip()

# 5. Rename column headers to lowercase and snake_case
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# 6. Reset index after cleaning
df = df.reset_index(drop=True)

# 7. Verify final data types
print("\nFinal Data Types:\n", df.dtypes)

# 8. Show cleaned dataset sample
print("\nSample of Cleaned Data:\n", df.head())

# 9. Save cleaned dataset to CSV
df.to_csv("netflix_titles_cleaned.csv", index=False)
print("\n✅ Cleaned data saved to 'netflix_titles_cleaned.csv'")
