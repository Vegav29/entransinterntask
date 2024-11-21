
# =======================
# 1. Load and Preprocess Data
# =======================
import sys
import os

# Set project root and import necessary modules
project_root = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(project_root)

from src.data.make_dataset import DataLoader
from src.features.build_features import Features
from src.config import DATA_PATH_RAW, DATA_PATH_INTERIM

# Load Data
dataset = DataLoader(filepath=f"{DATA_PATH_RAW}/sales_data.xlsx")
data = dataset.load_excel()

# Preprocess data
features = Features(data)
processed_data = features.preprocess()

# Generate and print summary statistics
print(features.generate_summary_statistics())

# Check for missing values
print(features.check_missing_values())

# Print data types of the columns
print(features.get_data_types())

# Save processed data as a pickle object
output_path = os.path.join(DATA_PATH_INTERIM, "data.pkl")
features.save(output_path)

# =======================
# 2. Visualizations and Analysis
# =======================
from src.visualization.visualize import Plots
from src.config import FIGURES_PATH

# Initialize Plots
plots = Plots(data)

# Generate and save visualizations
plots.sales_trends(f"{FIGURES_PATH}/sales_trends.png")
plots.revenue_profit_by_product_category(f"{FIGURES_PATH}/revenue_profit_by_category.png")
plots.price_vs_profit(f"{FIGURES_PATH}/price_vs_profit.png")

# =======================
# 3. Summary Statistics and Insights
# =======================
from src.visualization.summary import summary

stats_calculator = summary(data)

# Calculate and display summary statistics for numeric columns
numeric_columns = ['Customer_Age', 'Order_Quantity', 'Unit_Cost', 'Unit_Price', 'Profit', 'Revenue']
summary_stats = stats_calculator.summary_statistics(numeric_columns)

for column, stats in summary_stats.items():
    print(f"\nSummary Statistics for {column}:")
    for stat, value in stats.items():
        print(f"{stat}: {value:.2f}")

# Additional insights: Grouping data
grouped_by_country = stats_calculator.group_by_column('Country', 'Revenue')
grouped_by_product_category = stats_calculator.group_by_column('Product_Category', 'Profit')

print("\nTotal Revenue by Country:")
print(grouped_by_country)

print("\nTotal Profit by Product Category:")
print(grouped_by_product_category)

# Count unique values for specific columns
columns_to_check = ['Product_Category', 'Sub_Category', 'Product']
unique_counts = stats_calculator.count_unique_values(columns_to_check)

for column, count in unique_counts.items():
    print(f"Total number of unique values in {column}: {count}")

# =======================
# 4. Histogram and Box Plots
# =======================
from src.visualization.questioins import Histogram

histogram_plotter = Histogram(data)

# Create histogram for Customer_Age
histogram_plotter.plot_histogram(
    column='Customer_Age', 
    bins=10, 
    title='Customer Age Distribution', 
    xlabel='Age'
)

# Create box plots for Revenue distribution across age groups by year
unique_years = data['Date'].dt.year.unique().tolist()
print("Unique Years in Data:", unique_years)

histogram_plotter.plot_revenue_boxplots(revenue_col='Revenue', age_col='Age_Group', year_col='Year', years=unique_years)

# =======================
# 5. Pie and Bar Charts
# =======================
# Pie chart for gender distribution
histogram_plotter.piechart(column='Customer_Gender', title="Gender Distribution")

# Bar chart for Age_Group vs Revenue and Product_Category vs Profit
from src.visualization.agerevenue import CategoryAnalysisChart

# Age group analysis
age_profit_chart = CategoryAnalysisChart(data, category_column='Age_Group', numerical_column='Profit')
age_profit_chart.plot_total_by_category()
(max_age_group, max_age_profit), (min_age_group, min_age_profit) = age_profit_chart.get_max_min_category()

print(f"Most profitable age group: {max_age_group} with profit {max_age_profit}")
print(f"Least profitable age group: {min_age_group} with profit {min_age_profit}")

# Product category analysis
product_revenue_chart = CategoryAnalysisChart(data, category_column='Product_Category', numerical_column='Revenue')
product_revenue_chart.plot_total_by_category()
(max_product, max_product_revenue), (min_product, min_product_revenue) = product_revenue_chart.get_max_min_category()

print(f"Most profitable product category: {max_product} with revenue {max_product_revenue}")
print(f"Least profitable product category: {min_product} with revenue {min_product_revenue}")

# =======================
# 6. Line Plot for Trends
# =======================
from src.visualization.profittrends import RevenueProfitTrend

start_month = input("Enter the start month (YYYY-MM): ")
end_month = input("Enter the end month (YYYY-MM): ")

trend_analyzer = RevenueProfitTrend(data)
trends = trend_analyzer.plot_trends(start_date=start_month, end_date=end_month)

print("\nMonthly Revenue and Profit Trends:")
print(trends)

# =======================
# 7. Scatter Plots for Profit Margin Analysis
# =======================
from src.visualization.profitmargin import AverageProfitMarginAnalysis

margin = AverageProfitMarginAnalysis(data)

# Average profit margin scatter plot
avg_profit_margin_df = margin.plot_average_profit_margin()
margin.plot_advanced_profit_margin()

print(avg_profit_margin_df.head())

# =======================
# 8. Stacked Bar Chart for Sub-Category Analysis
# =======================
from src.visualization.stackedbarchart import CategoryAnalysisChart

category_analysis = CategoryAnalysisChart(data, category_column='Product_Category', numerical_column='Revenue')
category_analysis.plot_stacked_bar_chart()
