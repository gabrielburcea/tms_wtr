import pandas as pd
import random
from datetime import datetime

def generate_synthetic_data(start_date, end_date, products, countries, channels, brands):
    """
    Generate synthetic sales data with seasonality. 

    Parameters:
        start_date (str): Start date in 'YYYY-MM-DD' format
        end_date (str): End date in 'YYYY-MM-DD' format
        products (list): List of product names
        countries (list): List of product countries
        channels (list): List of product channels
        brands (list): List of brands

    Returns:
        pd.DataFrame: List of brands.
    """
    date_range = pd.date_range(start = start_date, end = end_date)
    
    def generate_sale(date):
        month = date.month
        
        if month in [6,7,8]:
            value = random.uniform(50000, 250000)
            volume = random.uniform(100000, 500000)
        elif month in [12, 1, 2]:
            value = random.uniform(20000, 50000)
            volume = random.uniform(20000, 100000)
        else:
            value = random.uniform(20000, 150000)
            volume = random.uniform(50000, 300000)
        return round(value, 2), round(volume, 2)
    data = []
    for date in date_range:
        product = random.choice(products)
        country = random.choice(countries)
        channel = random.choice(channels)
        brand = random.choice(brands)
        total_invoiced_value, total_invoiced_volume = generate_sale(date)
        data.append([date.strftime('%Y-%m-%d'), product, country, channel, brand, total_invoiced_value, total_invoiced_volume])
        df_synthetic = pd.DataFrame(data, columns=['date', 'product', 'country', 'channel', 'brand', 'total_invoiced_value', 'total_invoiced_volume'])
        return df_synthetic 
    

