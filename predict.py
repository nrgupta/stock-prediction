# Import Required Libraries
import pandas as pd
import yfinance as yf
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings("ignore")

# Define Stock Symbol
stock_symbol = "Googl"

# Download historical data from Yahoo Finance
data = yf.download(stock_symbol, start='2010-01-01', end='2023-01-01')
data.head(100)