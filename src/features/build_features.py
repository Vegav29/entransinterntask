import pandas as pd
import os

class Features:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def preprocess(self):
        """
        Preprocess the data:
        - Handle missing values.
        - Drop unnecessary columns.
        - Convert data types.
        - Derive new features.
        """
        # Handle missing values
        self.data.fillna(0, inplace=True)

        # Drop unnecessary columns based on predefined list or other conditions
        self.remove_unwanted_columns()

        # Convert data types
        if 'Date' in self.data.columns:
            self.data['Date'] = pd.to_datetime(self.data['Date'], errors='coerce')
        if 'Customer_Age' in self.data.columns:
            self.data['Customer_Age'] = pd.to_numeric(self.data['Customer_Age'], errors='coerce')

        # Derive new features 
        if 'Profit Margin' not in self.data.columns and 'Revenue' in self.data.columns and 'Profit' in self.data.columns:
            self.data['Profit Margin'] = (self.data['Profit'] / self.data['Revenue']) * 100

        print("Preprocessing complete.")
        
        # Print shape of the DataFrame
        self.print_shape()

        return self.data

    def remove_unwanted_columns(self):
        """
        Remove unwanted columns that are not useful for analysis or computation.
        """
        # List of columns to drop
        columns_to_drop = ['Day', 'State', 'Country']  # Modify this list as required
        self.data.drop(columns=[col for col in columns_to_drop if col in self.data.columns], errors='ignore', inplace=True)

    def save(self, filename: str):
        """Save the preprocessed data as a pickle object."""
        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        # Save the data as pickle
        self.data.to_pickle(filename)
        print(f"Data saved as {filename}")

    def generate_summary_statistics(self):
        """Generate summary statistics for numeric columns."""
        return self.data.describe()

    def check_missing_values(self):
        """Check for missing values in the dataset."""
        return self.data.isnull().sum()

    def print_shape(self):
        """Print the shape of the DataFrame."""
        print(f"Data Shape: {self.data.shape}")

    def get_data_types(self):
        """Return the data types of all columns."""
        return self.data.dtypes
    def save(self, filename: str):
    
    # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Save the data as pickle
        self.data.to_pickle(filename)
        print(f"Data saved as pickle file: {filename}")
