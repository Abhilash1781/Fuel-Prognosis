# Fuel-Prognosis
Fuel consumption prediction project aims to tackle the challenge of providing accurate and reliable fuel consumption estimates for the latest car models released in 2022. 

## Introduction
With the increasing emphasis on environmental sustainability and rising fuel costs, consumers are seeking vehicles that offer optimal fuel efficiency while aligning with their preferences and needs.


 By leveraging machine learning techniques, this project seeks to bridge the gap between consumers and data-driven insights, enabling them to choose vehicles that align with their economic and environmental goals.

## Dataset
The dataset comprises technical details of car models released in 2022, with 945 entries and 15 columns, providing insights into various features and attributes.

### List of columns
1) **Model Year** : The year in which the vehicle model was released.
2) **Make**  : The brand or manufacturer of the vehicle.
3) **Model** : The specific model name of the vehicle.
4) **Vehicle Class** : The category or type of the vehicle, such as SUV, minivan, etc.
5) **Engine Size**  : The size of the vehicle's engine.
6) **Cylinders** : The number of cylinders in the engine.
7) **Transmission** : The type of transmission, such as automatic or manual.
8) **Fuel Type** : The type of fuel used by the vehicle.
9) **Fuel Consumption (City (L/100 km)** : The estimated fuel consumption in city driving conditions.
10) **Fuel Consumption(Hwy (L/100 km))** : The estimated fuel consumption in highway driving conditions.
11) **Fuel Consumption(Comb (L/100 km))** : The estimated fuel consumption in combined city & highway driving conditions.
12) **Fuel Consumption(Comb (mpg))** : The estimated miles per gallon in combined city and highway driving conditions.
13) **CO2 Emissions(g/km)**  :
14) **CO2 Rating** : The carbon dioxide emissions rating.
15) **Smog Rating** : The smog (Smoke + fog) rating of the vehicle.


## Results
Following models were used to predict fuel consumption:

1) Linear Regression
2) Decision Tree Regression
3) Random Forest Regression
4) XG Boost
5) LightGBM

Models were then compared using various performance metrics, such as:
1) R2 Score
2) MAE - Mean Absolute Error
3) MSE - Mean Squared Error
4) RMSE - Root Mean Squared Error


![Performance metrics](https://github.com/Abhilash1781/Fuel-Prognosis/assets/72621930/f7bf6bda-a778-41c9-bb61-c60ccd6ace0d)


Among the models considered, the XGBoost model exhibited the best performance, achieving an R2 Score of around 0.96. Additionally, XGBoost achieved the lowest values for both MAE and RMSE, with 0.43 and 0.27 respectively.


The Random Forest model also demonstrated good performance, with an R2 Score of 0.952. It achived slightly higher values for both MAE and RMSE with 0.44 and 0.29 respectively.

## Deployment
In addition to model development and evaluation, we also focused on creating an interactive and user-friendly interface for our fuel consumption prediction model. To achieve this, we leveraged Streamlit, a powerful Python library for building web applications with minimal effort. Streamlit allowed us to transform our machine learning model into an intuitive and accessible web application.










