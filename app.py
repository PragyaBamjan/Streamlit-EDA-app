import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Superstore Sales Performance Dashboard")
st.write(
    "Explore sales, profit, and performance trends across regions, product categories, "
    "and customer segments. Use the sidebar controls to configure the visualizations."
)

@st.cache_data
def load_data():
    return pd.read_csv("superstore.csv", encoding="latin-1")

df = load_data()

# Sidebar controls
st.sidebar.header("Heatmap Controls")

column_axis = st.sidebar.selectbox(
    "Column Axis",
    options=["Category", "Segment", "Ship Mode"],
    help="Select the business dimension to display as heatmap columns. "
         "Rows are always fixed to Region."
)

heatmap_metric = st.sidebar.radio(
    "Metric to Map",
    options=["Sales", "Profit", "Discount", "Quantity"],
    index=1,
    help="Select the metric to display in each heatmap cell. "
         "Values are totals (sum) across all orders in each Region x column combination."
)

st.sidebar.header("Scatter Plot Controls")

numeric_options = ["Sales", "Profit", "Discount", "Quantity"]

x_axis = st.sidebar.selectbox(
    "X Axis",
    options=numeric_options,
    index=2,
    help="Select the numeric variable for the horizontal axis."
)

y_axis = st.sidebar.selectbox(
    "Y Axis",
    options=numeric_options,
    index=1,
    help="Select the numeric variable for the vertical axis."
)

color_grouping = st.sidebar.selectbox(
    "Color Grouping",
    options=["Category", "Segment", "Region", "Ship Mode"],
    index=1,
    help="Select the categorical variable to use for dot colors."
)

st.sidebar.header("Summary Statistics Controls")

summary_metric = st.sidebar.radio(
    "Metric to Summarize",
    options=["Sales", "Profit", "Discount", "Quantity"],
    index=1,
    help="Select the metric to display descriptive statistics for."
)

# Heatmap
st.subheader("Sales Performance Heatmap")

if heatmap_metric == "Discount":
    st.info("Discount values are decimals (0.0 = 0%, 0.8 = 80%).")

heatmap_data = df.pivot_table(
    values=heatmap_metric,
    index="Region",
    columns=column_axis,
    aggfunc="sum"
)

heatmap_fmt = ".2f" if heatmap_metric == "Discount" else ".0f"

fig1, ax1 = plt.subplots(figsize=(10,4))
sns.heatmap(heatmap_data, annot=True, fmt=heatmap_fmt, cmap="RdYlGn",
            linewidths=0.5, linecolor="white", ax=ax1)
ax1.set_title(f"Total {heatmap_metric} by Region x {column_axis}")
ax1.set_xlabel(column_axis)
ax1.set_ylabel("Region")
plt.tight_layout()
st.pyplot(fig1)

# Scatter plot
st.subheader("Variable Relationship Scatter Plot")

if x_axis == y_axis:
    st.warning(
        f"X and Y axes are both set to {x_axis}. "
        "Please select two different variables."
    )
else:
    if x_axis == "Discount" or y_axis == "Discount":
        st.info("Discount values are decimals (0.0 = 0%, 0.8 = 80%).")

    fig2, ax2 = plt.subplots(figsize=(10,5))
    palette = sns.color_palette("Set2", df[color_grouping].nunique())

    for i, cat in enumerate(sorted(df[color_grouping].unique())):
        subset = df[df[color_grouping] == cat]
        ax2.scatter(subset[x_axis], subset[y_axis],
                    label=str(cat), alpha=0.4, s=15, color=palette[i])
        
    if y_axis == "Profit":
        ax2.axhline(y=0, color="red", linestyle="--", linewidth=1,
                    alpha=0.6, label="Break-even ($0)")
        
    ax2.set_title(f"{x_axis} vs. {y_axis} by {color_grouping}")
    ax2.set_xlabel(x_axis)
    ax2.set_ylabel(y_axis)
    ax2.legend(title=color_grouping, bbox_to_anchor=(1.01, 1),
               loc="upper left", fontsize=9)
    plt.tight_layout()
    st.pyplot(fig2)

# KPI cards
st.subheader("Business Overview")

total_sales     = df["Sales"].sum()
total_profit    = df["Profit"].sum()
profit_margin   = (total_profit / total_sales) * 100
total_orders    = len(df)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sales",          f"${total_sales:,.0f}")
col2.metric("Total Profit",         f"${total_profit:,.0f}")
col3.metric("Avg Profit Margin",    f"{profit_margin:.1f}%")
col4.metric("Total Orders",         f"{total_orders:,}")

# Summary Statistics
st.subheader(f"Summary Statistics - {summary_metric}")

if summary_metric == "Discount":
    st.info("Discount values are decimals (0.0 = 0%, 0.8 = 80%).")

st.write(df[summary_metric].describe())
