# YouTube Trending Video Analysis (End-to-End Analytics)

## 📋 Project Overview

This project is an end-to-end data analytics solution that explores YouTube's trending videos (Nov 2017 - June 2018). It demonstrates a complete data pipeline: from initial cleaning and exploration with **Python**, through data management in **SQL Server**, to building a professional 4-page interactive dashboard in **Power BI**.

## Data Architecture: The Star Schema

To ensure high performance and scalability—concepts rooted in my software engineering background—I implemented a **Star Schema** for the data model:

- **Fact Table:** `Video_Stats` (Contains quantitative data like views, likes, and trending dates).
- **Dimension Table:** `Videos` (Contains descriptive attributes like titles, channel names, and publish dates).
- **Relationship:** A **1:Many** relationship was established via `video_id`, optimizing query performance and simplifying DAX calculations.

## Technical Tech Stack

### Python (Data Pre-processing & EDA)

- **Pandas & NumPy:** Used for data wrangling, handling duplicates, and transforming the raw JSON/CSV data into a structured format.
- **Matplotlib & Seaborn:** Conducted initial Exploratory Data Analysis (EDA) to identify outliers and understand feature correlations.

### SQL (Data Management & Integrity)

- **SQL Server (SSMS):** Hosted the dataset to simulate a production-grade environment.
- **Data Validation:** Wrote SQL queries to verify data consistency across the `Videos` and `Stats` tables before importing into Power BI.

### Power BI (Visualization & DAX)

- **Power Query:** Performed advanced ETL tasks, including date/time splitting and conditional column creation.
- **Advanced DAX:** Developed complex measures for business logic, such as:
  - `Engagement Rate`: `(Likes + Comments + Dislikes) / Views`
  - `Trend Velocity`: Calculated the speed of content virality using `DATEDIFF` and `LOOKUPVALUE`.

## Key Insights

- **Optimal Posting Time:** Publishing between 10:00 AM and 5:00 PM (Peak at 4:00 PM) correlates with the highest trending probability.
- **Viral Speed (Velocity):** While **Music** videos have the longest "trending life," **News & Politics** videos trend the fastest.
- **Engagement vs. Reach:** **Nonprofits & Activism** often achieve higher engagement rates per view compared to mainstream entertainment categories.

## Project Structure

- `/Python_Scripts`: Jupyter Notebooks containing the EDA process.
- `/SQL_Queries`: SQL scripts for table creation and data validation.
- `/Report`: The final `.pbix` Power BI file.
- `/Images`: Screenshots of the 4 dashboard pages.

## Dashboard Pages

1. **Executive Summary:** Overall KPIs and category performance.
2. **Audience Engagement:** Deep dive into sentiment and interaction ratios.
3. **Time-Series Analysis:** Growth trends and peak activity hours.
4. **Video Deep Dives:** Identifying top-performing individual creators and videos.

### Dashboard Previews

#### 1. Executive Summary

![Executive Summary](Dashboard%20Images/Executive%20Summary.PNG)

#### 2. Audience Engagement

![Audience Engagement](Dashboard%20Images/Audience%20Engagement.PNG)

#### 3. Time-Series Analysis

![Time-Series](Dashboard%20Images/Time-Series.PNG)

#### 4. Video Deep Dives

![Video Deep Dives](Dashboard%20Images/Video%20Deep%20Dives.PNG)

## Data Source

The dataset used in this analysis can be found on Kaggle: [Trending YouTube Video Statistics](https://www.kaggle.com/datasets/datasnaek/youtube-new)

---

**Developed by Magdy Elsayed** _Software Engineer & Data Enthusiast_
