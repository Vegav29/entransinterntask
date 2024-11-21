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
    ├── figures          
    │         
    │
    ├── notebooks          <- Jupyter notebooks.
    │    └── analysis.ipynb <- Jupyter notebooks for data analysis, exploration, and experimentation.                  
    │                         
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
    │   │── data 
    │   ├── features <- Scripts to turn raw data into features for modeling
    |   |   └── build_features.py
    |   ├── Visulaization    
    │       ├── agerevenue.py        <- Class for visualizing age revenue data.
    │       ├── profitmargin.py      <- Class for visualizing profit margins.
    │       ├── profittrends.py      <- Class for visualizing profit trends over time.
    │       ├── questionm.py         <- Class for visualizing questions and answers.
    │       ├── stackedbarchart.py   <- Class for creating stacked bar charts.
    │       ├── summary.py           <- Class for summarizing visual analysis.
    │       └── visualize.py         <- Main script to tie all visualizations together.
    |
    |   
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------
# Sales Data Analysis and Visualization

This project involves analyzing and visualizing sales data using Python. The goal is to preprocess the data, perform analysis, and create visualizations for insights.
link to dataset:https://docs.google.com/spreadsheets/d/1a2p0Eq3nrwee_0cX4W8s--tinG_sAUndFSUraPsfkqE/edit?gid=1733856421#gid=1733856421
---

## Tasks and Screenshots

### 1. Import Data from Excel and Load it as a DataFrame Using Pandas
The first step is to import the sales data from an Excel file and load it into a Pandas DataFrame for processing.

**Screenshot:**

![Import Data Screenshot](https://github.com/user-attachments/assets/0bf1714b-a889-410f-a8a1-1821ab81c168)

---

### 2. Perform Preprocessing Operations
This step involves checking the data types, handling null values, and ensuring the dataset is clean for analysis.

**Screenshot:**

![Preprocessing Screenshot](https://github.com/user-attachments/assets/a519505c-541c-4027-ac9e-c39fa36aa19a)

---

### 3. Save Data as a Pickle Object
Once the data is processed, it is saved as a pickle object for future use and storage.

**Screenshot:**

![Save Data Screenshot](https://github.com/user-attachments/assets/593a51b5-9039-4c93-b92a-a3ac2c031af8)

---

### 4. Perform Data Analysis and Visualize Using Seaborn/Matplotlib
We perform data analysis and create various visualizations to extract insights from the data.

**Screenshot:**

![Data Analysis Screenshot](https://github.com/user-attachments/assets/04bd7676-7c42-422f-b670-5b1ede688fe5)

---

### 5. Display Data Using Visualizations/Data Analysis and Save as JPG/PNG
Visualizations are generated to provide a better understanding of the data, and the images are saved for future reference.

**Screenshot:**

![Visualization Screenshot](https://github.com/user-attachments/assets/e686aea8-9c12-42ff-8857-0b71f1d5982c)

---

### 5.a. Calculate Summary Statistics (Mean, Median, etc.) for Numeric Columns
Summary statistics for numeric columns, including mean, median, and other key metrics, are calculated to provide insights into the dataset.

**Screenshot:**

![Summary Statistics Screenshot](https://github.com/user-attachments/assets/dd83bb78-c6ac-4765-a542-5753b3a09fa0)

---

### 5.b. Find the Total Number of Product_Category, Sub_Category, Product
This step counts the unique values for columns such as Product_Category, Sub_Category, and Product.

**Screenshot:**

![Unique Counts Screenshot](https://github.com/user-attachments/assets/bee722be-200d-410d-ab82-729682fd9e2f)

---

### 5.c. Create a Histogram of Customer_Age to Observe the Age Distribution
A histogram is created to visualize the distribution of customer ages.

**Screenshot:**

![Customer Age Histogram Screenshot](https://github.com/user-attachments/assets/643ccfaf-85cc-4e39-9c37-b928c35b592f)

---

### 5.d. [Advanced] Create 5 Subplots with Box Plots of Revenue Distribution Across Each Age Group for a Year
This advanced visualization shows the revenue distribution for each age group across different years using box plots.

**Screenshot:**

![Revenue Distribution Box Plot Screenshot](https://github.com/user-attachments/assets/7d1a33fa-3b36-4668-a0c8-c983da22b5b0)

---

### 5.e. Create a Pie Chart or Bar Chart to Visualize Gender Distribution
A pie chart or bar chart is generated to visualize the gender distribution of the customers.

**Screenshot:**

![Gender Distribution Pie Chart Screenshot](https://github.com/user-attachments/assets/bd21c54c-7071-41f5-83c3-c2e7893d8956)

---

### 5.f. Use a Bar Chart to Show the Relationship Between Age_Group and Revenue
This bar chart shows the relationship between different age groups and their corresponding revenue.

**Screenshot:**

![Age Group vs Revenue Bar Chart Screenshot](https://github.com/user-attachments/assets/d85df4cd-ccfb-4bec-b2f1-b86fad383d2f)

---

### 5.g. Identify the Most and Least Profitable Product_Category
We analyze which product category is the most and least profitable by summing the profits for each category and creating a horizontal bar chart.

**Screenshot:**

![Product Category Profit Screenshot](https://github.com/user-attachments/assets/456a7fca-c2c8-4cb6-a9ab-7256392382d2)

---

### 5.h. Take User Input for Start and End Month/Year and Create a Line Plot Showing Revenue and Profit Trends
A line plot is created to show the trends in revenue and profit based on user input for a specific period.

**Screenshot:**

![Revenue and Profit Trends Line Plot Screenshot](https://github.com/user-attachments/assets/51c42d8e-ca86-4122-b7de-bd86cefddc70)

---

### 5.i. Calculate the Average Profit Margin per Product and Plot Using a Scatter Plot
A scatter plot is generated to visualize the average profit margin for each product.

**Screenshot:**

![Profit Margin Scatter Plot Screenshot](https://github.com/user-attachments/assets/9a3babc8-8fe3-4c00-8001-0c9bf370bd4f)

---

### 5. j.[Advanced] Plot Profit Margin per Product with Profit Amount Using Scatter Plot (Marker Size as Profit Indicator)
An advanced scatter plot visualizes the relationship between profit margin and profit amount, with marker size representing profit.

**Screenshot:**

![Profit Margin with Profit Scatter Plot Screenshot](https://github.com/user-attachments/assets/7d1a33fa-3b36-4668-a0c8-c983da22b5b0)

---

### 5.k. Examine Which Sub_Category within a Product_Category Performs Best in Terms of Profit or Revenue
A stacked bar chart is created to visualize revenue or profit by sub-category within each product category.

**Screenshot:**

![Sub-Category Performance Stacked Bar Chart Screenshot](https://github.com/user-attachments/assets/7da203cd-9ab1-44fe-98bc-c29804b7f574)
# Unit Testing

This project includes unit tests to ensure the correctness and reliability of the implemented functionalities. The tests are designed to validate key aspects of the application, such as data integrity, functionality, and error handling.

## Test Files
- All test cases are located in the `src/unittest/` directory.
- Each test file corresponds to specific modules or functionalities within the project.

## Tests Overview
1. **Data Validation**:
   - Ensures the data loaded from pickle files is valid, with correct column names, data types, and non-empty content.
   - Verifies the presence of mandatory columns such as `Product_Category`, `Sub_Category`, `Revenue`, and `Profit`.

2. **Functionality Testing**:
   - Tests core functionalities like filtering data by a date range and plotting revenue and profit trends.
   - Ensures functions handle invalid inputs, empty datasets, and out-of-range dates gracefully.

3. **Error Handling**:
   - Validates that the system raises appropriate exceptions for invalid scenarios, such as:
     - Missing or empty data.
# Unit Testing

This project includes unit tests to ensure the correctness and reliability of the implemented functionalities. The tests are designed to validate key aspects of the application, such as data integrity, functionality, and error handling.

## Test Files
- All test cases are located in the `src/unittest/` directory.
- Each test file corresponds to specific modules or functionalities within the project.

## Tests Overview
1. **Data Validation**:
   - Ensures the data loaded from pickle files is valid, with correct column names, data types, and non-empty content.
   - Verifies the presence of mandatory columns such as `Product_Category`, `Sub_Category`, `Revenue`, and `Profit`.

2. **Functionality Testing**:
   - Tests core functionalities like filtering data by a date range and plotting revenue and profit trends.
   - Ensures functions handle invalid inputs, empty datasets, and out-of-range dates gracefully.

3. **Error Handling**:
   - Validates that the system raises appropriate exceptions for invalid scenarios, such as:
     - Missing or empty data.
## Conclusion
The project provides a comprehensive analysis of sales data, offering various insights into product performance, customer demographics, and trends over time. The visualizations and statistical analyses can be used for decision-making and strategic planning.

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
