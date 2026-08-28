# Task 2: Exploratory Data Analysis (EDA) — CodeAlpha

This repository contains my submission for **Task 2 (EDA)** as part of the Data Analytics Internship at **CodeAlpha**.

The goal of this project is to explore, clean, and analyze the web-scraped dataset (`books_dataset.csv`) to identify key statistical insights, price distributions, and rating patterns.



##  Tech Stack & Tools
- **Python 3.x**
- **Libraries:**
  - `pandas` (for data manipulation and summary statistics)
  - `matplotlib` & `seaborn` (for data visualization)



##  Analytical Steps & Insights
1. **Data Preprocessing:** Cleaned the price column by stripping symbols and mapping word ratings to numerical values for statistical calculations.
2. **Missing Values Check:** Confirmed zero missing or null values in the dataset.
3. **Statistical Summary:** Calculated key statistics such as average book price (~$35.00), minimum price ($12.84), and maximum price ($57.31).
4. **Visual Explorations:**
   - Plotted a **Histogram** to show the distribution of book prices.
   - Built a **Count Plot** to inspect the frequency of books across star ratings.



##  Repository Structure
├── eda_analysis.py # Python script for data analysis & plotting
├── books_dataset.csv # Source dataset used for analysis
├── eda_plots.png # Saved visualization dashboard image
└── README.md # Project documentation




##  Execution Steps
1. Install required dependencies:
   ```bash
   pip install pandas matplotlib seaborn
2. Run the analysis script: python eda_analysis.py
3. The script will print summary stats in the terminal and save the visualization plots as eda_plots.png.



**Intern:** Rohit Mondal
**Domain:** Data Analytics
**Organization:** CodeAlpha
