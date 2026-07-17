# Netflix Data Analysis & Visualization Dashboard

### Project Description

A comprehensive data analysis project that explores Netflix's content catalog using Python, uncovering trends in content distribution, ratings, genres, countries, and release patterns through statistical analysis and visualizations.

An interactive Streamlit dashboard was developed to enable real-time exploration of Netflix data, providing actionable insights through dynamic charts, filters, and key performance indicators.

---

# Netflix Data Analysis & Visualization Dashboard

## Overview

This project performs an end-to-end Exploratory Data Analysis (EDA) on the Netflix Titles Dataset to discover meaningful insights about Netflix's content library. The analysis includes data cleaning, statistical exploration, feature engineering, visualization, and an interactive Streamlit dashboard.

The project demonstrates practical data analysis skills using Python and modern data visualization techniques to understand content trends, ratings, genres, release patterns, and geographical distribution.

---

## Objectives

* Load and explore the Netflix dataset.
* Clean and preprocess raw data.
* Handle missing values and duplicates.
* Perform statistical analysis.
* Create insightful visualizations.
* Identify content trends and patterns.
* Build an interactive Streamlit dashboard.

---

## Dataset Information

**Dataset:** Netflix Titles Dataset

**Records:** 8,807

**Features:** 12

### Dataset Columns

* show_id
* type
* title
* director
* cast
* country
* date_added
* release_year
* rating
* duration
* listed_in
* description

---

## Project Workflow

### 1. Data Loading

* Imported required libraries.
* Loaded dataset using Pandas.
* Displayed dataset information and structure.

### 2. Data Cleaning

* Checked missing values.
* Filled missing categorical data.
* Removed duplicate records.
* Converted date fields.
* Created engineered features such as:

  * year_added
  * month_added
  * duration_num

### 3. Exploratory Data Analysis

* Statistical summary
* Mean
* Median
* Mode
* Standard Deviation
* Correlation Matrix

### 4. Data Visualization

Created 15 professional visualizations including:

* Movies vs TV Shows
* Release Year Distribution
* Content Added by Year
* Content Distribution Pie Chart
* Top Countries
* Rating Distribution
* Top Genres
* Movie Duration Distribution
* TV Show Seasons Distribution
* Top Directors
* Top Actors
* Scatter Plot
* Correlation Heatmap
* Box Plot
* Violin Plot

### 5. Streamlit Dashboard

Built an interactive dashboard featuring:

* Dataset Preview
* KPI Metrics
* Content Type Analysis
* Rating Analysis
* Country Analysis
* Genre Analysis
* Interactive Filters
* Dynamic Charts

---

## Technologies Used

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn
* Plotly

### Dashboard Development

* Streamlit

### Development Environment

* Visual Studio Code

---

## Key Insights

* Movies significantly outnumber TV Shows on Netflix.
* Most Netflix content was released after 2010.
* The United States contributes the highest number of titles.
* India is among the leading content-producing countries.
* TV-MA is one of the most common ratings.
* Drama-related genres dominate the platform.
* Netflix content additions increased rapidly after 2015.
* The platform experienced significant growth between 2016 and 2020.
* International content represents a substantial portion of the catalog.
* Content diversity has increased considerably over time.

---

## Project Structure

```text
Netflix-EDA-Dashboard/
│
├── netflix_analysis.py
├── app.py
├── netflix_titles.csv
├── requirements.txt
├── plots/
│   ├── 01_movies_vs_tvshows.png
│   ├── 02_release_year_distribution.png
│   ├── ...
│
└── README.md
```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Run Analysis

```bash
python netflix_analysis.py
```

---

## Run Dashboard

```bash
streamlit run app.py
```

---

## Dashboard Features

* Interactive filtering
* Real-time visualizations
* KPI cards
* Genre analysis
* Country analysis
* Rating distribution
* Release trend monitoring

---

## Learning Outcomes

This project strengthened practical skills in:

* Data Cleaning
* Exploratory Data Analysis
* Feature Engineering
* Statistical Analysis
* Data Visualization
* Dashboard Development
* Python Programming
* Business Intelligence

---

## Future Improvements

* Recommendation System Integration
* Predictive Analytics
* Genre Trend Forecasting
* Advanced Dashboard Features
* Real-Time Data Integration

---

## Author

**Tooba Fatima**

AI/ML Engineer | Data Science Enthusiast | Generative AI | NLP | Computer Vision | Streamlit | Python

---

### If you found this project useful, consider giving it a ⭐ on GitHub.
