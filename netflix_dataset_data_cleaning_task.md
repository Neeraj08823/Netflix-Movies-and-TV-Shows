# Netflix Dataset – Data Cleaning Task

## 📊 Dataset:

[Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)

## 🧹 Objective:

Clean and preprocess the raw Netflix dataset using Python (Pandas) to make it ready for analysis.

## 🛠️ Tools Used:

- Python 3.x
- Pandas Library
- VS Code

## ✅ Tasks Performed:

- Loaded the dataset using `pandas.read_csv()`
- Removed duplicate records using `.drop_duplicates()`
- Handled missing values:
  - Filled missing `rating` using forward fill
  - Replaced missing `country` and `director` with `"Unknown"`
  - Dropped rows missing `date_added`
- Converted `date_added` to datetime format using `pd.to_datetime()`
- Standardized text in `type`, `rating`, and `country` columns
- Renamed all column headers to lowercase with underscores
- Verified data structure and previewed sample records using `.head()` and `.info()`
- Exported final cleaned dataset as `netflix_titles_cleaned.csv`

## 🗃 Output:

A clean, consistent, and ready-to-use dataset suitable for further analysis or visualization.
