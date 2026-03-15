# Superstore Sales Performance Dashboard

## Description

The Superstore Sales Performance Dashboard is an Exploratory Data Analysis (EDA) application that is developed using the Streamlit library. It is an interactive application where users can explore the data of a retail business. The application uses the Superstore Sales data that can be found on the Kaggle platform, where there are 9,994 orders received by the retail business. It has relevant information regarding sales, profit, discount, categories of products sold, segments of customers, and regions. The business problem that the application of this data aims to solve is the need for understanding the factors that negatively affect or increase profitability in the context of the region, product sold, or segment of customers. The application allows users to interactively explore two types of visualizations: a heatmap to identify patterns of performance across various geographic or categorical dimensions and a scatter plot to explore the relationship between any two numeric fields. In addition to this, the dashboard includes a stable KPI summary panel, which includes the following: total sales, total profit, average profit, and total orders over the entire dataset. There is a section on the dashboard dedicated to summary statistics, which allows users to explore the statistical distribution of a specific metric of their choice. All the controls in the sidebars are well described, letting users understand what each input does and which output it affects. The application is intended to be simple, beginner-friendly, and immediately useful for data-driven decisions in the retail business.

---

## Tool Used
- **Python** - This is the programming language that the entire application has been built upon.
- **Streamlit** - This is the web application framework that has been utilized for the development and execution of the interactive dashboard in the browser.
- **Pandas** - This has been utilized for data loading, transformation, grouping, and aggregation in the application.
- **Matplotlib** - This has been utilized as the rendering engine for the visualization of the entire application.
- **Seaborn** - This has been utilized in combination with Matplotlib for the generation of highly styled heat maps and scatter plots with minimal code required.

---

## How to Run the Project

1. **Download the provided 'superstore.csv' file** and place it in the same folder as `app.py`
2. **Ensure Python is installed** on your device.
3. **Open a terminal** and navigate to the folder where you saved the project files.
4. **Install the required dependencies** by running the pip install command with the 'requirements.txt' file
5. **Launch the Streamlit app** by running: `streamlit run app.py`
6. **Open the dashboard** in your browser - Streamlit will automatically open it.
7. **Use the sidebar controls** on the left to explore the dataset interactively.

---

## Business Analysis and Insights

The Superstore Sales Performance Dashboard provides several key insights about profitability in the retail sector, and these are directly applicable to managerial decisions. The heatmap data consistently indicates that the Technology category has the highest profit value in almost all regions, while the Furniture category is problematic, especially in the Central region, where it makes a loss of about $2,871. This indicates that perhaps the price or cost structure for the Furniture category in underperforming regions needs to be reviewed before further investment in inventory is made. The West region is seen to have performed the best, making the highest total profit among all product categories. The Central region has performed the worst in terms of profitability, which is a point that needs to be addressed by management. The relationship between the variables on the scatter plot of Discount vs. Profit is one of the most important business insights to be derived from the data. The fact that as the discount values go up, the profit values tend to concentrate in negative territory is a relationship that has negative implications for the business. The relationship is seen across all segments of the business, indicating it is a systematic problem rather than a localized one. As seen from the summary statistics section, the Profit has a very high variance, with a standard deviation of $234 against a mere average of $29, clearly indicating that a few profitable orders for Technology are compensating for the low-margin or loss-making orders elsewhere. The overall picture that the dashboard presents for the management team is that Technology's profit margins should be kept protected, Furniture needs restructuring in terms of pricing, and there needs to be a discount ceiling in place while taking care of the long tail of unprofitable "Consumer Orders."