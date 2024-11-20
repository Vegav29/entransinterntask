
import pandas as pd

class DataLoader:
    """Handles loading and saving of data."""
    
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.data = None

    def load_excel(self) -> pd.DataFrame:
        """Load Excel file into a DataFrame."""
        try:
            self.data = pd.read_excel(self.filepath)
            print("Data loaded successfully.")

        except Exception as e:
            print(f"Error loading data: {e}")
        return self.data

    def save_as_pickle(self, output_path: str):
        """Save DataFrame as a pickle file."""
        if self.data is not None:
            self.data.to_pickle(output_path)
            print(f"Data saved as pickle at {output_path}")
        else:
            print("No data to save!")
