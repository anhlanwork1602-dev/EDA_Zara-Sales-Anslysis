# %% [markdown]
# # EDA - ZARA SALES ANALYSIS

# %% [markdown]
# ### PROJECT SUMMARY
# 
# This project performs an exploratory data analysis on Zara’s fashion product dataset to understand the key factors influencing product performance and consumer purchasing behavior in the fast-fashion industry.
# 
# The analysis focuses on how product characteristics such as product category, price level, promotional campaigns, seasonal trends, and store positioning impact sales volume.
# 
# From a business and economic perspective, fashion retailers operate in a highly competitive market where demand is influenced by pricing strategy, product visibility, consumer preferences, and seasonal cycles. Understanding these relationships helps retailers optimize product assortment, inventory allocation, and marketing decisions.
# 

# %% [markdown]
# ### OBJECTIVES
# 
# The objective of this project is to uncover actionable insights that explain:
# 
# - Which product categories generate the highest demand
# - How pricing affects customer purchasing behavior
# - Whether promotional activities significantly increase sales
# - How seasonal products perform compared to regular items
# - Which product placement strategies contribute to higher sales performance

# %% [markdown]
# ### PROBLEM STATEMENT
# 
# In the fast-fashion industry, retailers such as Zara need to continuously adapt their product strategies due to rapidly changing consumer preferences and high inventory turnover.
# 
# However, not all products perform equally. Some products achieve high sales volumes while others underperform despite being offered within the same brand ecosystem.
# 
# The key business challenge is:
# 
# *"How can Zara identify the product attributes and commercial strategies that drive higher sales performance and optimize retail decisions?"*
# 
# This project aims to analyze the relationship between product features and sales outcomes to discover patterns that can support better:
# 
# - product planning
# - pricing decisions
# - promotion strategies
# - inventory management

# %% [markdown]
# ### UNIVARIATE ANALYSIS
# 
# **1. Product Category Distribution**
# 
# This analysis examines the distribution of Zara's products across different fashion categories. Understanding category concentration helps identify Zara's main product focus and reveals which segments dominate the product portfolio.
# 
# Categories with the highest product counts represent Zara's core offerings, which may require stronger inventory planning and demand forecasting strategies.
# 
# **2. Product Position Distribution**
# 
# Analyzing product placement across different positions (Aisle, End-cap, Front of Store) provides insights into Zara's merchandising strategy.
# 
# Products placed in high-visibility locations such as Front of Store or End-cap may receive greater customer attention, helping evaluate whether product positioning aligns with sales performance.
# 
# **3. Sales Volume Distribution**
# 
# The sales volume distribution analysis helps understand overall customer demand patterns across Zara products.
# 
# Products with extremely high sales volumes represent popular items, while low-performing products may indicate opportunities for inventory optimization or product strategy adjustments.
# 
# This analysis helps Zara identify demand concentration and improve stock allocation decisions.
# 
# **4. Price Distribution**
# 
# Analyzing product price distribution provides insights into Zara's pricing strategy and product positioning.
# 
# Most products are expected to fall within Zara's accessible fast-fashion price range, while premium-priced products represent a smaller segment.
# 
# Understanding price concentration helps evaluate whether Zara maintains a balanced product portfolio between affordability and premium offerings.
# 
# **5. Promotion Distribution**
# 
# This analysis explores the proportion of products receiving promotional campaigns.
# 
# Products with promotions represent Zara's marketing strategy to increase customer demand, accelerate inventory turnover, and manage seasonal product cycles.
# 
# Comparing promoted and non-promoted products helps evaluate the effectiveness of promotional activities.
# 
# **6. Seasonal Product Distribution**
# 
# Analyzing seasonal product availability reveals how Zara adapts its assortment according to consumer demand cycles.
# 
# Seasonal items may experience stronger demand during specific periods, making seasonality an important factor in inventory planning and product forecasting.
# 
# **7. Material Distribution**
# 
# This analysis identifies the most frequently used materials in Zara's product catalog.
# 
# Understanding material preference helps reveal consumer trends and supports decisions related to sourcing, production planning, and sustainability strategies.
# 
# **8. Section Distribution**
# 
# Analyzing product distribution across different store sections provides insights into Zara's retail organization.
# 
# Sections with a higher concentration of products may represent strategic areas where Zara focuses assortment and customer engagement.
# 

# %% [markdown]
# ### BI-VARIATE ANALYSIS
# 
# **1. Product Category vs Sales Volume**
# 
# This analysis examines the relationship between product categories and sales performance to identify which fashion segments generate the highest customer demand.
# 
# Categories with higher average sales volumes indicate stronger consumer preferences and may help Zara prioritize inventory allocation, product planning, and future collection strategies.
# 
# **2. Price vs Sales Volume**
# 
# Analyzing the relationship between product price and sales volume helps evaluate the impact of pricing strategy on consumer purchasing behavior.
# 
# Products with different price levels may attract different customer segments. Understanding whether lower-priced or premium products achieve stronger sales performance helps Zara optimize pricing decisions and maintain a competitive fast-fashion strategy.
# 
# **3. Promotion vs Sales Volume**
# 
# This analysis investigates whether promotional campaigns influence product demand and customer purchasing decisions.
# 
# Products under promotion may experience higher sales due to increased customer attention and purchase incentives. This insight helps evaluate whether Zara's promotional strategies effectively improve sales performance and inventory turnover.
# 
# **4. Product Position vs Sales Volume**
# 
# Analyzing product placement and sales performance helps understand the impact of merchandising strategies on customer behavior.
# 
# Products displayed in high-visibility locations such as Front of Store or End-cap may generate stronger demand, providing insights into how store positioning influences purchasing decisions.
# 
# **5. Seasonal Product vs Sales Volume**
# 
# This analysis explores the relationship between seasonal attributes and product sales performance.
# 
# Seasonal products may experience changes in demand depending on consumer trends and fashion cycles. Understanding seasonal sales patterns helps Zara improve demand forecasting and inventory management.
# 
# **6. Section vs Sales Volume**
# 
# Analyzing different retail sections and their sales performance reveals which areas contribute most to customer demand.
# 
# Sections with higher sales performance may represent important product segments where Zara should focus assortment planning and resource allocation.
# 
# **7. Material vs Sales Volume**
# 
# This analysis evaluates whether product materials influence customer demand.
# 
# Certain materials may be preferred by customers due to comfort, quality perception, or fashion trends. Understanding material impact supports product design decisions and sourcing strategies.
# 
# **8. Price Category vs Sales Volume**
# 
# This analysis investigates how different price segments perform in terms of sales volume.
# 
# Comparing low, medium, and premium-priced products helps Zara identify the most profitable customer segments and adjust product pricing strategies accordingly.

# %% [markdown]
# ### MULTI-VARIATE ANALYSIS
# 
# **1. Correlation Analysis Between Numerical Variables**
# 
# This analysis explores relationships among numerical features such as product price and sales volume.
# 
# Understanding correlations between variables helps identify factors that may influence product performance and reveals important patterns within Zara's product dataset.
# 
# **2. Price, Promotion, and Sales Volume Relationship**
# 
# This analysis examines how pricing and promotional activities jointly affect product demand.
# 
# Products with different price levels may respond differently to promotional campaigns. This insight helps Zara understand whether discounts are more effective for certain product segments.
# 
# **3. Product Category, Price, and Sales Performance**
# 
# Analyzing product category together with pricing and sales volume provides a deeper understanding of category-level performance.
# 
# This analysis helps identify which categories achieve strong demand at different price points and supports decisions related to assortment planning and pricing optimization.
# 
# **4. Product Position, Promotion, and Sales Performance**
# 
# This analysis investigates whether promotional effectiveness varies depending on product placement.
# 
# Products located in highly visible areas combined with promotional campaigns may generate stronger customer engagement, helping Zara improve merchandising strategies.
# 
# **5. Seasonal Trend, Category, and Sales Volume Analysis**
# 
# This analysis evaluates how seasonality interacts with product categories to influence customer demand.
# 
# Certain categories may perform better during specific seasons, providing insights for seasonal collection planning and inventory preparation.
# 
# **6. Sales Performance Segmentation Analysis**
# 
# This analysis segments products based on their sales performance to identify high-performing and low-performing products.
# 
# High-performing products can reveal successful combinations of attributes such as category, price, promotion, and seasonality, while low-performing products may indicate areas for improvement.
# 
# **7. Customer Demand Pattern Analysis**
# 
# This analysis combines multiple product attributes to understand overall consumer purchasing behavior.
# 
# Identifying common characteristics among successful products helps Zara make data-driven decisions regarding product development, marketing strategies, and inventory optimization.

# %% [markdown]
# ## ANALYSIS PROCESS

# %% [markdown]
# ### 1. IMPORT LIBRARIES

# %%
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore

import warnings
warnings.filterwarnings("ignore")

pd.set_option("display.max_columns", None)

# %% [markdown]
# ### 2. LOAD DATASET

# %%
df = pd.read_csv(
    "C:/Users/Admin/Desktop/DA projects/EDA Zara/Zara_sales_EDA.csv",
    sep=";"
)

df.head()

# %%
df.shape

# %% [markdown]
# ### 3. DATA OVERVIEW

# %%
df.columns

# %%
df.info()

# %%
df.describe()

# %% [markdown]
# ### 4. DATA CLEANING

# %%
df.isnull().sum()

# %%
plt.figure(figsize=(12,5))

sns.heatmap(
    df.isnull(),
    cbar=False
)

plt.title("Missing Value")
plt.show()


# %%
df.duplicated().sum()

# %%
df.drop_duplicates(inplace=True)

# %%
for col in df.columns:
    print(
        col, 
        df[col].nunique()
    )

# %% [markdown]
# ### 5. CONVERT PRICE COLUMN

# %%
df["price"].head()

# %% [markdown]
# ### 6. CREATE NEW FEATURES

# %%
df["price_category"]= pd.cut(
    df["price"],
    bins=[0,30,70,150,1000],
    labels=[
        "Low",
        "Medium",
        "High",
        "Luxury"
    ]
)

# %%
df["sales_level"] = pd.qcut(
    df["Sales Volume"],
    q=4,
    labels=[
    "Low",
    "Medium",
    "High",
    "Very High"   
    ]
)

# %% [markdown]
# ### 7. UNIVARIATE ANALYSIS

# %% [markdown]
# a. Product category distribution
# Question: Zara sells which categories most?

# %%
plt.Figure(figsize=(12,5))

sns.countplot(
    data=df, 
    y="Product Category",
    order=df["Product Category"].value_counts().index
)

plt.title(
    "Product Category Distribution"
)

plt.show()

# %% [markdown]
# b. Sale distribution

# %%
plt.figure(figsize=(10,5))

sns.histplot(
    df["Sales Volume"],
    bins=50,
    kde=True
)

plt.title(
    "Sales Volume Distribution"
)

plt.show()

# %% [markdown]
# c. Price distribution

# %%
plt.figure(figsize=(10,5))

sns.histplot(
    df["price"],
    bins=50,
    kde=True
)

plt.title(
    "Price Distribution"
)

plt.show()

# %% [markdown]
# ### 8. PRODUCT POSITION ANALYSIS

# %% [markdown]
# Research question: Products places where sell better?

# %%
df["Product Position"].value_counts()

# %% [markdown]
# Sales by position

# %%
position_sales = (
    df.groupby(
        "Product Position"
    )["Sales Volume"]
    .mean()
    .sort_values()  
)

position_sales.plot(
    kind="bar",
    figsize=(10,5)
)

plt.title(
    "Average Sales by Product Position"
)

plt.show()

# %% [markdown]
# ### 9. PROMOTION ANALYSIS

# %% [markdown]
# Business question: Does promotion increase sales?

# %%
sns.countplot(
    data=df,
    x="Promotion"
)

plt.show()

# %% [markdown]
# Sales comparison

# %%
sns.boxplot(
    data=df,
    x="Promotion",
    y="Sales Volume"
)

plt.title(
    "Sales vs Promotion"
)

plt.show()

# %% [markdown]
# Mean difference

# %%
df.groupby(
    "Promotion"
)["Sales Volume"].mean()

# %% [markdown]
# ### 10. SEASONAL ANALYSIS

# %% [markdown]
# Question: Are seasonal products easier to sell?

# %%
sns.boxplot(
    data=df,
    x="Seasonal",
    y="Sales Volume"
)

plt.show()

# %% [markdown]
# ### 11. CATEGORY VS SALES

# %% [markdown]
# Very important. 

# %%
category_sales = (
    df.groupby(
        "Product Category"
)["Sales Volume"]
.mean()
.sort_values(
    ascending=False
)
)

category_sales.plot(
    kind="bar",
    figsize=(12,5)
)

plt.title(
    "Average Sales by Category"
)

plt.show()

# %% [markdown]
# ### 12. PRICE VS SALES

# %%
sns.scatterplot(
    data=df,
    x="price",
    y="Sales Volume",
    alpha=0.4
)

plt.title(
    "Price vs Sales Volume"
)

plt.show()


# %% [markdown]
# ### 13. CORRELATION ANALYSIS

# %%
numeric = df.select_dtypes(
    include="number"
)

numeric.head()

# %%
plt.figure(figsize=(10,6))

sns.heatmap(
    numeric.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title(
    "Correlation Matrix"
)

plt.show()

# %% [markdown]
# ### 14. ADVANCE: TOP PRODUCTS

# %% [markdown]
# Question: Which are best-selling Zara items?

# %%
top_products = (
    df.sort_values(
        "Sales Volume",
        ascending=False
    )
    .head(10)
)

top_products[
    [
        "name",
        "Product Category",
        "Sales Volume",
        "price"
    ]
]

# %% [markdown]
# ### 15. CONCLUSION

# %% [markdown]
# This exploratory data analysis provides an overview of Zara's product characteristics and sales patterns.
# 
# The analysis examined how different factors such as product category, pricing, promotion, seasonality, and product positioning are associated with sales volume.
# 
# Key observations from the dataset include differences in customer demand across product attributes, price segments, and product groups.
# 
# These findings provide a foundation for further analysis such as sales prediction, customer segmentation, or inventory optimization.


