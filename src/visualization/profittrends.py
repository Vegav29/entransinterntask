import matplotlib.pyplot as plt
import pandas as pd


class RevenueProfitTrend:
    def __init__(self, data: pd.DataFrame):
        """Initialize the class with a DataFrame."""
        self.data = data
        # Ensure 'Date' column is in datetime format and add 'YearMonth' for filtering
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        self.data['YearMonth'] = self.data['Date'].dt.to_period('M')

    def plot_trends(self, start_date: str, end_date: str):
        """
        Plot revenue and profit trends for a specified period.

        :param start_date: Start date in 'YYYY-MM' format
        :param end_date: End date in 'YYYY-MM' format
        :return: DataFrame containing aggregated revenue and profit trends
        """
        try:
            # Parse user inputs to Period objects
            start_period = pd.Period(start_date, freq='M')
            end_period = pd.Period(end_date, freq='M')

            # Check if the date range is valid
            if start_period > pd.Timestamp.today().to_period('M') or end_period > pd.Timestamp.today().to_period('M'):
                raise ValueError("Date range cannot be in the future.")

            # Filter data for the given period
            filtered_data = self.data[(self.data['YearMonth'] >= start_period) & (self.data['YearMonth'] <= end_period)]

            if filtered_data.empty:
                raise ValueError("No data available for the specified period.")

            # Group by 'YearMonth' and calculate sums for Revenue and Profit
            monthly_trends = filtered_data.groupby('YearMonth')[['Revenue', 'Profit']].sum()

            # Plot trends
            plt.figure(figsize=(12, 6))
            plt.plot(monthly_trends.index.astype(str), monthly_trends['Revenue'], label='Revenue', marker='o', color='skyblue')
            plt.plot(monthly_trends.index.astype(str), monthly_trends['Profit'], label='Profit', marker='o', color='orange')
            plt.xlabel('Month')
            plt.ylabel('Amount')
            plt.title('Revenue and Profit Trends')
            plt.xticks(rotation=45)
            plt.legend()
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()

            return monthly_trends
        except Exception as e:
            raise ValueError(f"An error occurred while processing trends: {e}")
