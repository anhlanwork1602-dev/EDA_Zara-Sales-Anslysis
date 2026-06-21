import streamlit as st
import pandas as pd
import plotly.express as px


# ======================
# Page Config
# ======================

st.set_page_config(
    page_title="Zara Sales Dashboard",
    page_icon="👗",
    layout="wide"
)


# ======================
# Load Data
# ======================

@st.cache_data
def load_data():
    df = pd.read_csv("Zara_sales_EDA.csv", sep=";")

    # clean price
    df["price"] = (
        df["price"]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .astype(float)
    )

    return df


df = load_data()


# ======================
# Title
# ======================

st.title("👗 Zara Fashion Sales Dashboard")

st.markdown(
"""
Exploratory dashboard analyzing Zara product attributes,
pricing, promotions and sales performance.
"""
)


# ======================
# Sidebar Filter
# ======================

st.sidebar.header("Filter")


category = st.sidebar.multiselect(
    "Product Category",
    options=df["Product Category"].unique(),
    default=df["Product Category"].unique()
)


season = st.sidebar.multiselect(
    "Seasonal",
    options=df["Seasonal"].unique(),
    default=df["Seasonal"].unique()
)


filtered_df = df[
    (df["Product Category"].isin(category)) &
    (df["Seasonal"].isin(season))
]


# ======================
# KPI Cards
# ======================

col1, col2, col3, col4 = st.columns(4)


col1.metric(
    "Total Products",
    filtered_df.shape[0]
)


col2.metric(
    "Average Price",
    f"${filtered_df['price'].mean():.2f}"
)


col3.metric(
    "Average Sales",
    f"{filtered_df['Sales Volume'].mean():.0f}"
)


promo_rate = (
    filtered_df["Promotion"]
    .value_counts(normalize=True)
    .get("Yes",0)
    *100
)


col4.metric(
    "Promotion Rate",
    f"{promo_rate:.1f}%"
)


st.divider()


# ======================
# Charts Row 1
# ======================


col1, col2 = st.columns(2)


with col1:

    category_sales = (
        filtered_df
        .groupby("Product Category")["Sales Volume"]
        .mean()
        .reset_index()
        .sort_values(
            "Sales Volume",
            ascending=False
        )
    )


    fig = px.bar(
        category_sales,
        x="Product Category",
        y="Sales Volume",
        title="Average Sales by Category"
    )

    st.plotly_chart(fig, use_container_width=True)



with col2:

    fig = px.histogram(
        filtered_df,
        x="price",
        nbins=40,
        title="Price Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )



# ======================
# Charts Row 2
# ======================


col1, col2 = st.columns(2)


with col1:

    promo = (
        filtered_df
        .groupby("Promotion")["Sales Volume"]
        .mean()
        .reset_index()
    )


    fig = px.bar(
        promo,
        x="Promotion",
        y="Sales Volume",
        title="Promotion vs Sales"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )



with col2:

    position = (
        filtered_df
        .groupby("Product Position")["Sales Volume"]
        .mean()
        .reset_index()
    )


    fig = px.bar(
        position,
        x="Product Position",
        y="Sales Volume",
        title="Product Position vs Sales"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ======================
# Scatter
# ======================


fig = px.scatter(
    filtered_df,
    x="price",
    y="Sales Volume",
    color="Promotion",
    hover_data=[
        "Product Category",
        "Product Position"
    ],
    title="Price vs Sales Volume"
)


st.plotly_chart(
    fig,
    use_container_width=True
)


st.caption(
"Created using Python, Pandas, Streamlit and Plotly"
)
