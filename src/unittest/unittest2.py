import unittest
import pandas as pd
import os
from src.visualization.profittrends import RevenueProfitTrend
from src.config import DATA_PATH_INTERIM


class TestRevenueProfitTrendWithPickle(unittest.TestCase):
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
        """Initialize the RevenueProfitTrend object with the loaded data."""
        self.revenue_profit_trend = RevenueProfitTrend(self.data)

    def test_column_data_types(self):
        """Test that columns have correct data types."""
        self.assertTrue(pd.api.types.is_numeric_dtype(self.data['Revenue']), "Revenue should be numeric")
        self.assertTrue(pd.api.types.is_numeric_dtype(self.data['Profit']), "Profit should be numeric")
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(self.data['Date']), "Date should be datetime")

    def test_column_names(self):
        """Test that all expected columns are present."""
        expected_columns = ['Date', 'Revenue', 'Profit', 'Product_Category', 'Sub_Category', 'Product']
        actual_columns = list(self.data.columns)
        for col in expected_columns:
            self.assertIn(col, actual_columns, f"Missing column: {col}")

    def test_plot_trends_valid_range(self):
        """Test the plot_trends method with a valid date range."""
        result = self.revenue_profit_trend.plot_trends(start_date="2023-01", end_date="2023-12")
        self.assertGreater(len(result), 0, "Filtered data should not be empty for the valid date range.")
        self.assertIn("Revenue", result.columns, "The result should contain 'Revenue' column.")
        self.assertIn("Profit", result.columns, "The result should contain 'Profit' column.")

    def test_plot_trends_invalid_range(self):
        """Test the plot_trends method with an invalid date range."""
        with self.assertRaises(ValueError, msg="Should raise ValueError for invalid date range."):
            self.revenue_profit_trend.plot_trends(start_date="2025-01", end_date="2025-12")

    def test_empty_data_check(self):
        """Test for empty filtered data."""
        with self.assertRaises(ValueError, msg="Should raise ValueError when no data is available for the period."):
            self.revenue_profit_trend.plot_trends(start_date="1900-01", end_date="1900-12")


if __name__ == '__main__':
    unittest.main()

