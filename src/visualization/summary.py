import pandas as pd

class summary:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def calculate_summary(self, column: str):
        if column in self.data.columns: 
            return {
                "Mean": self.data[column].mean(),
                "Median": self.data[column].median(),
                "Min": self.data[column].min(),
                "Max": self.data[column].max(),
            }
        else:
            raise ValueError(f"Column '{column}' not found in the dataset.")

    def summary_statistics(self, columns: list):
        stats = {}
        for column in columns:
            try:
                stats[column] = self.calculate_summary(column)
            except ValueError as e:
                print(e)
        return stats

    def group_by_column(self, group_by_col: str, calc_col: str, agg_func='sum'):
        if group_by_col in self.data.columns and calc_col in self.data.columns:
            return self.data.groupby(group_by_col)[calc_col].agg(agg_func)
        else:
            raise ValueError(f"One or both columns '{group_by_col}' and '{calc_col}' not found in the dataset.")
    def count_unique_values(self, columns: list):
        unique_counts = {}
        for column in columns:
            if column in self.data.columns:
                unique_counts[column] = self.data[column].nunique()
            else:
                raise ValueError(f"Column '{column}' not found in the dataset.")
        return unique_counts