import matplotlib.pyplot as plt
import pandas as pd

class AverageProfitMarginAnalysis:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def plot_average_profit_margin(self):
        
        required_columns = ['Product', 'Profit Margin']

        avg_profit_margin = self.data.groupby('Product')['Profit Margin'].mean().reset_index()
        avg_profit_margin = avg_profit_margin.sort_values(by='Profit Margin', ascending=False)

        plt.figure(figsize=(12, 6))
        plt.scatter(avg_profit_margin['Product'], avg_profit_margin['Profit Margin'], color='blue', alpha=0.6)
        plt.xlabel('Product', fontsize=12)
        plt.ylabel('Average Profit Margin', fontsize=12)
        plt.title('Average Profit Margin per Product', fontsize=14)
        plt.xticks(rotation=90, fontsize=8)
        plt.tight_layout()
        plt.show()

        return avg_profit_margin
    def plot_advanced_profit_margin(self):

        product_analysis = self.data.groupby('Product').agg({
            'Profit Margin': 'mean',  
            'Profit': 'sum'          
        }).reset_index()

        plt.figure(figsize=(12, 8))
        scatter = plt.scatter(
            product_analysis['Profit Margin'], 
            product_analysis['Profit'], 
            s=product_analysis['Profit'] / 300,  
            alpha=0.7,
            color='dodgerblue',
            edgecolor='black'
        )
        
        plt.xlabel('Average Profit Margin (%)', fontsize=12)
        plt.ylabel('Total Profit', fontsize=12)
        plt.title('Advanced Profit Margin vs. Profit Analysis', fontsize=14)
        plt.grid(True, linestyle='--', alpha=0.4)
        plt.tight_layout()

        plt.show()

        return product_analysis