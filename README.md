Dsproject
==============================


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------
# Sales Data Analysis and Visualization

This project involves analyzing and visualizing sales data using Python. The goal is to preprocess the data, perform analysis, and create visualizations for insights.

---

## Tasks and Screenshots

### 1. Import Data from Excel and Load it as a DataFrame Using Pandas
The first step is to import the sales data from an Excel file and load it into a Pandas DataFrame for processing.

**Screenshot:**
![Import Data Screenshot](![image](https://github.com/user-attachments/assets/0bf1714b-a889-410f-a8a1-1821ab81c168)


---

### 2. Perform Preprocessing Operations
This step involves checking the data types, handling null values, and ensuring the dataset is clean for analysis.

**Screenshot:**
![Preprocessing Screenshot](![image](https://github.com/user-attachments/assets/a519505c-541c-4027-ac9e-c39fa36aa19a)
)

---

### 3. Save Data as a Pickle Object
Once the data is processed, it is saved as a pickle object for future use and storage.

**Screenshot:**
![Save Data Screenshot](![image](https://github.com/user-attachments/assets/593a51b5-9039-4c93-b92a-a3ac2c031af8)
)

---

### 4. Perform Data Analysis and Visualize Using Seaborn/Matplotlib
We perform data analysis and create various visualizations to extract insights from the data.

**Screenshot:**
![Data Analysis Screenshot](![image](https://github.com/user-attachments/assets/04bd7676-7c42-422f-b670-5b1ede688fe5),![image](https://github.com/user-attachments/assets/e686aea8-9c12-42ff-8857-0b71f1d5982c),![image](https://github.com/user-attachments/assets/dd83bb78-c6ac-4765-a542-5753b3a09fa0)


)

---

### 5. Display Data Using Visualizations/Data Analysis and Save as JPG/PNG
Visualizations are generated to provide a better understanding of the data, and the images are saved for future reference.

**Screenshot:**
![Visualization Screenshot](./screenshots/visualization.png)

---

### 6. Calculate Summary Statistics (Mean, Median, etc.) for Numeric Columns
Summary statistics for numeric columns, including mean, median, and other key metrics, are calculated to provide insights into the dataset.

**Screenshot:**
![Summary Statistics Screenshot](./screenshots/summary_statistics.png)

---

### 7. Find the Total Number of Product_Category, Sub_Category, Product
This step counts the unique values for columns such as Product_Category, Sub_Category, and Product.

**Screenshot:**
![Unique Counts Screenshot](![image](https://github.com/user-attachments/assets/bee722be-200d-410d-ab82-729682fd9e2f)
)

---

### 8. Create a Histogram of Customer_Age to Observe the Age Distribution
A histogram is created to visualize the distribution of customer ages.

**Screenshot:**
![Customer Age Histogram Screenshot](./screenshots/![image](https://github.com/user-attachments/assets/643ccfaf-85cc-4e39-9c37-b928c35b592f)
)

---

### 9. [Advanced] Create 5 Subplots with Box Plots of Revenue Distribution Across Each Age Group for a Year
This advanced visualization shows the revenue distribution for each age group across different years using box plots.

**Screenshot:**
![Revenue Distribution Box Plot Screenshot](./screenshots/revenue_distribution_boxplot.png)

---

### 10. Create a Pie Chart or Bar Chart to Visualize Gender Distribution
A pie chart or bar chart is generated to visualize the gender distribution of the customers.

**Screenshot:**
![Gender Distribution Pie Chart Screenshot](![image](https://github.com/user-attachments/assets/bd21c54c-7071-41f5-83c3-c2e7893d8956)


---

### 11. Use a Bar Chart to Show the Relationship Between Age_Group and Revenue
This bar chart shows the relationship between different age groups and their corresponding revenue.

**Screenshot:**
![Age Group vs Revenue Bar Chart Screenshot](![image](https://github.com/user-attachments/assets/d85df4cd-ccfb-4bec-b2f1-b86fad383d2f)
)

---

### 12. Identify the Most and Least Profitable Product_Category
We analyze which product category is the most and least profitable by summing the profits for each category and creating a horizontal bar chart.

**Screenshot:**
![Product Category Profit Screenshot](![image](https://github.com/user-attachments/assets/456a7fca-c2c8-4cb6-a9ab-7256392382d2),![image](https://github.com/user-attachments/assets/2aa2b8f5-6964-4d95-8295-dc0e337a032e)

)

---

### 13. Take User Input for Start and End Month/Year and Create a Line Plot Showing Revenue and Profit Trends
A line plot is created to show the trends in revenue and profit based on user input for a specific period.

**Screenshot:**
![Revenue and Profit Trends Line Plot Screenshot](![image](https://github.com/user-attachments/assets/51c42d8e-ca86-4122-b7de-bd86cefddc70)


---

### 14. Calculate the Average Profit Margin per Product and Plot Using a Scatter Plot
A scatter plot is generated to visualize the average profit margin for each product.

**Screenshot:**
![Profit Margin Scatter Plot Screenshot](![image](https://github.com/user-attachments/assets/9a3babc8-8fe3-4c00-8001-0c9bf370bd4f)
)

---

### 15. [Advanced] Plot Profit Margin per Product with Profit Amount Using Scatter Plot (Marker Size as Profit Indicator)
An advanced scatter plot visualizes the relationship between profit margin and profit amount, with marker size representing profit.

**Screenshot:**
![Profit Margin with Profit Scatter Plot Screenshot](![image](https://github.com/user-attachments/assets/7d1a33fa-3b36-4668-a0c8-c983da22b5b0)
)

---

### 16. Examine Which Sub_Category within a Product_Category Performs Best in Terms of Profit or Revenue
A stacked bar chart is created to visualize revenue or profit by sub-category within each product category.

**Screenshot:**
![Sub-Category Performance Stacked Bar Chart Screenshot](![image](https://github.com/user-attachments/assets/7da203cd-9ab1-44fe-98bc-c29804b7f574)


---

## Conclusion
The project provides a comprehensive analysis of sales data, offering various insights into product performance, customer demographics, and trends over time. The visualizations and statistical analyses can be used for decision-making and strategic planning.

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
