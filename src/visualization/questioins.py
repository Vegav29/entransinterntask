import pandas as pd
import matplotlib.pyplot as plt

class Histogram:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def plot_histogram(self, column: str, bins: int = 10, title: str = "Histogram", xlabel: str = None, ylabel: str = "Frequency"):
        if column in self.data.columns:
            plt.figure(figsize=(10, 6))
            plt.hist(self.data[column], bins=bins, color='blue', alpha=0.7, edgecolor='black')
            plt.title(title)
            plt.xlabel(xlabel if xlabel else column)
            plt.ylabel(ylabel)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.show()
        else:
            raise ValueError(f"Column '{column}' not found in the dataset.")

    def plot_revenue_boxplots(self, revenue_col: str, age_col: str, year_col: str, years: list):
        
        filtered_data = self.data[self.data[year_col].isin(years)]

        fig, axes = plt.subplots(1, 6, figsize=(20, 6), sharey=True)

        for i in range(6):
            if i < len(years):
                year = years[i]
                year_data = filtered_data[filtered_data[year_col] == year]

                ax = axes[i]
                if year_data.empty:
                    ax.text(0.2, 0.2, 'No Data', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
                    ax.set_title(f"Year: {year}")
                    ax.set_xticks([])  
                    ax.set_yticks([])  
                    continue

                year_data.boxplot(column=revenue_col, by=age_col, ax=ax, grid=False, showfliers=False)
                ax.set_title(f"Year: {year}")
                ax.set_xlabel('Age Group', fontsize=7)
                ax.set_ylabel('Revenue' if i == 0 else '')  
            else:
                ax = axes[i]
                ax.axis('off')  

        fig.suptitle('Revenue Distribution Across Age Groups by Year', fontsize=16)
        plt.tight_layout(rect=[0, 0, 1, 0.95])
        plt.show()

    def piechart(self, column: str, title: str):
        counts = self.data[column].value_counts()
        plt.figure(figsize=(8, 8))
        plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
        plt.title(title)
        plt.show()
