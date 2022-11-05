# OR568 Final Project: Predicting Optimal Bike Demand based on Seoul Bike Sharing Data

<center>
<strong>Predicting Optimal Bike Demand based on Seoul Bike Sharing Data</strong><br><br><br>

Amy Lovas

Hannah Abraham

Kyle Smith

Sagar Goswami<br><br>

OR-568-004: Applied Predictive Analytics

George Mason University

December 13, 2022

<br><br><strong>Under the guidance of:</strong>

Dr. Vadim Sokolov
</center>

---


## Project Goals
- **Train a Predictive Model** to estimate the bike demand for a given time based on various Weather, Season, Holiday, etc. features. This model can be used to optimize and ensure proper quantity of bike availability at any given time basedon the before-mentioned features.


## Seoul Bike Sharing Demand Data Set
The Seoul Bike Sharing Demand Data is sourced from [The Machine Learning Repository, University of California - Irvine](https://archive.ics.uci.edu/ml/datasets/Seoul+Bike+Sharing+Demand). The dataset has 14 Attributes (explaining weather, season, holiday, etc.) and 8760 records. The target variable is the quantity of bikes rented during each hour. Following are the list of attributes:
- Target Variable:
    - Rented Bike Count : Count of bikes rented at each hour
- Time-Series Data
    - Date : Year-Month-Day
    - Hour : Hour of the day
- Weather Data
    - Temperature : Temperature in Celsius
    - Humidity : %
    - Wind Speed : m/s
    - Visibility : 10m
    - Dew Point Temperature : Celsius
    - Solar Radiation : MJ/m2
    - Rainfall : mm
    - Snowfall : cm
- Seasonal Data
    - Seasons : Winter, Spring, Summer, Autumn
    - Holiday : Holiday/No Holiday
    - Functioning Day : NoFunc(Non Functional Hours), Fun(Functional hours)


## Project Methodology
-   Data Exploration, Data Cleaning, and Pre-Processing
-   Predictive Models
    -   Multiple Linear Regression Model
    -   Best Subset Feature Selection Model
    -   Lasso Feature Selection and Regression
