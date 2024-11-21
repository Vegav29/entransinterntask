import matplotlib.pyplot as plt
import pandas as pd

class CategoryAnalysisChart:
    def __init__(self, data: pd.DataFrame, category_column: str, numerical_column: str):
        self.data = data
        self.category_column = category_column
        self.numerical_column = numerical_column
    
    def plot_total_by_category(self):
        total_by_category = self.data.groupby(self.category_column)[self.numerical_column].sum().sort_values(ascending=False)
        
        plt.figure(figsize=(10, 6))
        total_by_category.plot(kind='barh', color='skyblue')
        plt.xlabel(f'Total {self.numerical_column}')
        plt.ylabel(f'{self.category_column}')
        plt.title(f'Total {self.numerical_column} by {self.category_column}')
        plt.show()
        
        return total_by_category
    
    def get_max_min_category(self):
        total_by_category = self.data.groupby(self.category_column)[self.numerical_column].sum().sort_values(ascending=False)
        
        max_category = total_by_category.idxmax()
        min_category = total_by_category.idxmin()
        max_value = total_by_category.max()
        min_value = total_by_category.min()
        
        return (max_category, max_value), (min_category, min_value)