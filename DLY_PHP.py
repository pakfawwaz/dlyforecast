import yfinance as yf
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")  # Suppress warnings for cleaner output

# Download PHP/USD data from Yahoo Finance (extended historical data)
data = yf.download('PHPUSD=X', start='2020-01-01', end='2024-09-01', interval='1mo')
data = data['Close'].dropna()  # Use only the 'Close' column and drop any NaN values

# Define the range of parameters for p, d, q
p_values = range(0, 3)
d_values = range(0, 2)
q_values = range(0, 3)

# Variables to store the best parameters and lowest RMSE
best_rmse = float("inf")
best_order = None

# Grid search over the (p, d, q) parameters
for p in p_values:
    for d in d_values:
        for q in q_values:
            try:
                model = ARIMA(data, order=(p, d, q))
                model_fit = model.fit()
                
                # Generate predictions for training set
                predictions = model_fit.predict(start=1, end=len(data)-1)
                
                # Calculate RMSE
                rmse = np.sqrt(mean_squared_error(data[1:], predictions))
                
                # Check if we found a new best model
                if rmse < best_rmse:
                    best_rmse = rmse
                    best_order = (p, d, q)
                    
            except:
                continue

print(f"Best ARIMA order: {best_order} with RMSE: {best_rmse}")

# Fit the model with the best parameters found
best_model = ARIMA(data, order=best_order)
fitted_best_model = best_model.fit()

# Forecast 12 months ahead
forecast = fitted_best_model.forecast(steps=12)

print(forecast)
