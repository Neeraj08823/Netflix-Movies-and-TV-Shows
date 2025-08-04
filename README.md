# 📺 Netflix Dataset Cleaning – Internship Task

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Cleaning-green)
![VS Code](https://img.shields.io/badge/Editor-VS%20Code-blue?logo=visualstudiocode&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📑 Table of Contents:

- [Overview](#-overview)
- [Dataset](#-dataset)
- [Objectives](#-objectives)
- [Tools Used](#-tools-used)
- [Tasks Performed](#-tasks-Performed)
- [Output](#-output)

---

## 🧾 Overview:

This project involves cleaning and preprocessing the **Netflix Movies and TV Shows** dataset as part of a Data Analyst internship assignment. The goal is to make the dataset ready for analysis or visualization by handling common issues like missing values, duplicate rows, inconsistent formats, and more.

---

## 📊 Dataset:

**Source:** [Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)  
**Rows:** 8,797 after cleaning  
**Columns:** 12 including `show_id`, `type`, `title`, `date_added`, `rating`, etc.

---

## 🎯 Objectives:

- Handle missing and duplicate values
- Clean text fields for consistency
- Convert dates to datetime format
- Standardize column names
- Export a cleaned dataset ready for analysis

---

## 🛠 Tools Used:

- Python 3.8+
- Pandas
- VS Code
- Git & GitHub

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
