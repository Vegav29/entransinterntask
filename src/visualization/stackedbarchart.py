# File: src/visualization/stackedbarchart.py
import pandas as pd
import matplotlib.pyplot as plt

class CategoryAnalysisChart:
    def __init__(self, data: pd.DataFrame, category_column: str, numerical_column: str):
        self.data = data
        self.category_column = category_column
        self.numerical_column = numerical_column
    
    def plot_stacked_bar_chart(self):
        
        grouped_data = self.data.groupby([self.category_column, 'Sub_Category'])[self.numerical_column].sum().unstack()
        
        ax = grouped_data.plot(kind='bar', stacked=True, figsize=(12, 8), colormap='tab20')
        plt.title(f"Total {self.numerical_column} by Sub-Category within {self.category_column}")
        plt.xlabel(self.category_column)
        plt.ylabel(f"Total {self.numerical_column}")
        plt.xticks(rotation=45, ha='right')
        plt.legend(title='Sub-Category', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.show()
