import pytest
from tms_wtr.data_generation.synthetic_data import generate_synthetic_data

# Define Constants 
START_DATE = '2020-01-01'
END_DATE = '2023-12-31'
PRODUCTS = ['Aqua Pure', 'Crystal Clear', 'Fresh Flow', 'Pure Drop', 'Aqua Bliss']
COUNTRIES = ['USA', 'Canada', 'Mexico', 'UK', 'Germany']
CHANNELS = ['Online', 'Retail', 'Wholesale']
BRANDS = ['Brand X', 'Brand Y', 'Brand Z']

# Function to generate syntetic data

def generate_data():
    return generate_synthetic_data(start_date=START_DATE, end_date=END_DATE, products = PRODUCTS, countries = COUNTRIES, channels=CHANNELS, brands=BRANDS)

# Test function for pytest

def test_generate_synthetic_data():
    df = generate_data()
    assert df is not None, 'Dataframe should not be None'
    assert not df.empty, 'Dataframe should not be empty'
    # Asdd more assertions based on expected structure of df

# Main block for standalone execution
if __name__ == '__main__':
    df = generate_data()
    print(df)