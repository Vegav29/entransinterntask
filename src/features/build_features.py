import pandas as pd
import os

class Features:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def preprocess(self):
        self.data.fillna(0, inplace=True)

        self.remove_unwanted_columns()

        if 'Date' in self.data.columns:
            self.data['Date'] = pd.to_datetime(self.data['Date'], errors='coerce')
        if 'Customer_Age' in self.data.columns:
            self.data['Customer_Age'] = pd.to_numeric(self.data['Customer_Age'], errors='coerce')


        if 'Profit Margin' not in self.data.columns and 'Revenue' in self.data.columns and 'Profit' in self.data.columns:
            self.data['Profit Margin'] = (self.data['Profit'] / self.data['Revenue']) * 100

        print("Preprocessing complete.")
        
        self.print_shape()

        return self.data

    def remove_unwanted_columns(self):
        
        columns_to_drop = ['Day', 'State']  
        self.data.drop(columns=[col for col in columns_to_drop if col in self.data.columns], errors='ignore', inplace=True)

    def save(self, filename: str):
        
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        self.data.to_pickle(filename)
        print(f"Data saved as {filename}")

    def generate_summary_statistics(self):
        
        return self.data.describe()

    def check_missing_values(self):

        return self.data.isnull().sum()

    def print_shape(self):
       
        print(f"Data Shape: {self.data.shape}")

    def get_data_types(self):
        
        return self.data.dtypes
    def save(self, filename: str):
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        self.data.to_pickle(filename)
        print(f"Data saved as pickle file: {filename}")
