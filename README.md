# Hourly Energy Consumption Dashboard

![Dashboard Preview](https://github.com/ceduard0/hourly-energy-consumption-app/blob/main/hourly-energy-consumption-app.png?raw=true)
[demo]: https://www.kaggle.com/datasets/robikscube/hourly-energy-consumption



## Overview

This Streamlit dashboard allows you to explore over 10 years of hourly energy consumption data from PJM in Megawatts. The dataset is sourced from PJM Interconnection LLC (PJM), a regional transmission organization (RTO) in the United States, operating in the Eastern Interconnection grid. The electric transmission system serves various states and regions, including Delaware, Illinois, Indiana, Kentucky, Maryland, Michigan, New Jersey, North Carolina, Ohio, Pennsylvania, Tennessee, Virginia, West Virginia, and the District of Columbia.

## Key Features

### 1. Daily Trends

Explore the daily energy consumption trends over the selected period. Use interactive charts to identify patterns and fluctuations in energy usage on a daily basis.

### 2. Monthly Trends

Analyze the monthly energy consumption trends to uncover insights into seasonal variations and long-term patterns. The dashboard provides tools to visualize and compare energy usage on a monthly scale.

### 3. Annual Comparison

Compare annual energy consumption data to identify yearly trends and changes. The dashboard facilitates a side-by-side comparison, enabling users to spot variations and make informed observations.

## About the Dataset

### PJM Hourly Energy Consumption Data

The dataset consists of hourly power consumption data obtained from PJM's official website. The values are reported in megawatts (MW). As the regions served by PJM have changed over the years, the data may only appear for specific dates per region.

: [kaggle]: https://www.kaggle.com/datasets/robikscube/hourly-energy-consumption

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/ceduard0/hourly-energy-consumption-app.git
cd hourly-energy-consumption-app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:
```bash
streamlit run app.py
```
