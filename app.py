import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Sales Intelligence & Profit Prediction",
    page_icon="",
    layout="wide"
)

@st.cache_resource
def load_model_and_preprocessor():

    model = joblib.load("gradient_boosting_profit_model.pkl")
    preprocessor = joblib.load("profit_preprocessor.pkl")

    return model, preprocessor


model, preprocessor = load_model_and_preprocessor()

st.title("Sales Intelligence & Profit Prediction System")

st.write(
    "Predict the expected profit of a sales transaction "
    "using a trained Gradient Boosting Regression model."
)

st.divider()

st.subheader(" Enter Transaction Details")

col1, col2, col3 = st.columns(3)


with col1:

    sales = st.number_input(
        "Sales ($)",
        min_value=0.0,
        value=100.0,
        step=10.0
    )

    quantity = st.number_input(
        "Quantity",
        min_value=1,
        value=1,
        step=1
    )


with col2:

    discount = st.number_input(
        "Discount",
        min_value=0.0,
        max_value=1.0,
        value=0.0,
        step=0.05,
        help="Enter discount as a decimal. Example: 20% = 0.20"
    )

    category = st.selectbox(
        "Category",
        [
            "Furniture",
            "Office Supplies",
            "Technology"
        ]
    )


with col3:

    segment = st.selectbox(
        "Segment",
        [
            "Consumer",
            "Corporate",
            "Home Office"
        ]
    )

    region = st.selectbox(
        "Region",
        [
            "Central",
            "East",
            "South",
            "West"
        ]
    )

st.subheader("Product & Shipping Information")


col4, col5, col6 = st.columns(3)


with col4:

    sub_category = st.selectbox(
        "Sub-Category",
        [
            "Accessories",
            "Appliances",
            "Art",
            "Binders",
            "Bookcases",
            "Chairs",
            "Copiers",
            "Envelopes",
            "Fasteners",
            "Furnishings",
            "Labels",
            "Machines",
            "Paper",
            "Phones",
            "Storage",
            "Supplies",
            "Tables"
        ]
    )


with col5:

    ship_mode = st.selectbox(
        "Ship Mode",
        [
            "First Class",
            "Same Day",
            "Second Class",
            "Standard Class"
        ]
    )


with col6:

    order_date = st.date_input(
        "Order Date"
    )

    ship_date = st.date_input(
        "Ship Date"
    )

shipping_days = (ship_date - order_date).days

year = order_date.year
month = order_date.month
quarter = ((month - 1) // 3) + 1
day_of_week = order_date.strftime("%A")

st.subheader("Automatically Derived Features")


d1, d2, d3, d4 = st.columns(4)


with d1:
    st.metric(
        "Shipping Days",
        shipping_days
    )


with d2:
    st.metric(
        "Year",
        year
    )


with d3:
    st.metric(
        "Quarter",
        f"Q{quarter}"
    )


with d4:
    st.metric(
        "Day",
        day_of_week
    )


st.divider()

if st.button(
    " Predict Profit",
    use_container_width=True
):

    if shipping_days < 0:

        st.error(
            " Ship Date cannot be earlier than Order Date."
        )

    else:

        input_data = pd.DataFrame([{

            "Sales": sales,
            "Quantity": quantity,
            "Discount": discount,
            "Category": category,
            "Sub-Category": sub_category,
            "Segment": segment,
            "Region": region,
            "Ship Mode": ship_mode,
            "Shipping_Days": shipping_days,
            "Year": year,
            "Month": month,
            "Quarter": quarter,
            "Day_of_Week": day_of_week

        }])

        processed_input = preprocessor.transform(
            input_data
        )

        prediction = model.predict(
            processed_input
        )[0]

        st.subheader(" Prediction Result")


        result_col1, result_col2 = st.columns(2)


        with result_col1:

            st.metric(
                "Predicted Profit",
                f"${prediction:,.2f}"
            )


        with result_col2:

            if prediction >= 0:

                st.success(
                    " Predicted outcome: Positive Profit"
                )

            else:

                st.warning(
                    " Predicted outcome: Negative Profit"
                )

        with st.expander(" View Input Data"):

            st.dataframe(
                input_data,
                use_container_width=True
            )

st.divider()

st.caption(
    "Machine Learning Model: Gradient Boosting Regressor | "
    "Target: Profit"
)