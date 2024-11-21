import matplotlib.pyplot as plt
import pandas as pd

class RevenueProfitTrend:
    def __init__(self, data: pd.DataFrame):
        self.data = data 
        self.data['YearMonth'] = self.data['Date'].dt.to_period('M')  
    
    def plot_trends(self, start_date: str, end_date: str):
    
        start_period = pd.Period(start_date, freq='M')
        end_period = pd.Period(end_date, freq='M')
        filtered_data = self.data[(self.data['YearMonth'] >= start_period) & (self.data['YearMonth'] <= end_period)]
        
        monthly_trends = filtered_data.groupby('YearMonth')[['Revenue', 'Profit']].sum()
        

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


