import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

class Plots:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def save_and_display_plot(self, plot_func, output_path):
        """Display and save a plot to a file."""
        plt.figure(figsize=(10, 6))
        plot_func()  # Execute the plotting function
        plt.savefig(output_path)  # Save the figure
        plt.show()  # Display the figure
        plt.close()  # Close the figure
        print(f"Plot saved to {output_path}.")

    def histogram(self, column: str, output_path: str):
        """Histogram for a column."""
        self.save_and_display_plot(
            lambda: sns.histplot(self.data[column], kde=True, color="blue"),
            output_path
        )

    def bar_chart(self, x_col: str, y_col: str, output_path: str):
        """Bar chart for two columns."""
        self.save_and_display_plot(
            lambda: sns.barplot(data=self.data, x=x_col, y=y_col, palette="viridis"),
            output_path
        )

    def pie_chart(self, column: str, output_path: str):
        """Pie chart for a column."""
        data_counts = self.data[column].value_counts()
        self.save_and_display_plot(
            lambda: plt.pie(data_counts, labels=data_counts.index, autopct="%1.1f%%"),
            output_path
        )

    def scatter_plot(self, x_col: str, y_col: str, output_path: str):
        """Scatter plot for two numeric columns."""
        self.save_and_display_plot(
            lambda: sns.scatterplot(data=self.data, x=x_col, y=y_col, color="green"),
            output_path
        )

    def correlation_heatmap(self, output_path: str):
        """Correlation heatmap for numeric columns."""
        self.save_and_display_plot(
            lambda: sns.heatmap(self.data.corr(), annot=True, fmt=".2f", cmap="coolwarm"),
            output_path
        )
