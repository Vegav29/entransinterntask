import unittest
import pandas as pd
import os
from src.visualization.summary import summary
from src.config import DATA_PATH_INTERIM
class TestSummaryWithPickle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the test data from a pickle file."""
        pickle_file_path = os.path.join(DATA_PATH_INTERIM, "data.pkl")
        try:
            cls.data = pd.read_pickle(pickle_file_path)
            print("Test data loaded from pickle file.")
        except Exception as e:
            raise ValueError(f"Failed to load pickle file: {e}")

        if cls.data is None or cls.data.empty:
            raise ValueError("Loaded test data is empty or invalid.")

    def setUp(self):
        """Initialize the summary object with the loaded data."""
        self.summary_obj = summary(self.data)

    def test_column_data_types(self):
        """Test that columns have correct data types."""
        self.assertTrue(pd.api.types.is_string_dtype(self.data['Product_Category']), "Product_Category should be string")
        self.assertTrue(pd.api.types.is_string_dtype(self.data['Sub_Category']), "Sub_Category should be string")
        self.assertTrue(pd.api.types.is_numeric_dtype(self.data['Revenue']), "Revenue should be numeric")
        self.assertTrue(pd.api.types.is_numeric_dtype(self.data['Profit']), "Profit should be numeric")

    def test_column_names(self):
        """Test that all expected columns are present."""
        expected_columns = ['Product_Category', 'Sub_Category', 'Product', 'Revenue', 'Profit']
        actual_columns = list(self.data.columns)
        self.assertListEqual(expected_columns, actual_columns, "Column names do not match the expected structure.")


if __name__ == '__main__':
    unittest.main()
