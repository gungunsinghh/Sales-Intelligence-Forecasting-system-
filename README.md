#  Sales Intelligence & Profit Prediction System

An end-to-end Data Analytics and Machine Learning project built using a Superstore-style retail dataset. The project combines exploratory data analysis, customer segmentation, business intelligence, feature engineering, regression modeling, model interpretation, and a Streamlit-based profit prediction application.

The objective is to understand sales and profitability patterns, identify valuable customer and product segments, discover business insights, and predict the expected profit of a sales transaction.

---

##  Project Objectives

- Analyze overall sales and profitability performance.
- Identify profitable and loss-making regions, categories, and products.
- Understand the relationship between discounts and profit.
- Segment customers using RFM analysis.
- Engineer meaningful features for machine learning.
- Compare multiple regression models for profit prediction.
- Tune selected machine learning models using cross-validation.
- Interpret model predictions using feature importance and permutation importance.
- Build an interactive Streamlit application for profit prediction.
- Translate machine learning results into actionable business insights.

---

##  Technologies Used

- **Python** — Core programming language
- **Pandas** — Data manipulation and analysis
- **NumPy** — Numerical computation
- **Matplotlib** — Data visualization
- **Seaborn** — Statistical visualization
- **Plotly** — Interactive visualizations
- **Scikit-learn** — Data preprocessing, regression models and evaluation
- **XGBoost** — Gradient boosting model comparison
- **Joblib** — Model serialization and loading
- **SQLite** — Data storage and querying
- **Jupyter Notebook** — Data analysis and experimentation
- **Streamlit** — Interactive machine learning application
- **Git & GitHub** — Version control and project hosting

---

##  Dataset

The project uses a **Superstore-style retail sales dataset** containing transactional information about customers, products, orders, shipping, sales, discounts and profit.

### Dataset Statistics

- **Rows:** 10,194
- **Original Columns:** 21
- **Target Variable:** `Profit`

### Important Columns

- `Order ID`
- `Order Date`
- `Ship Date`
- `Ship Mode`
- `Customer ID`
- `Customer Name`
- `Segment`
- `Region`
- `Category`
- `Sub-Category`
- `Product Name`
- `Sales`
- `Quantity`
- `Discount`
- `Profit`

The original dataset is not included in the repository. To reproduce the notebook locally, place the dataset in the `data` folder using the expected filename:

`sample_-_superstore.xls`

---

##  Data Cleaning & Preparation

The dataset was inspected and prepared before performing business analysis and machine learning.

The preprocessing workflow included:

- Checking dataset dimensions and data types.
- Inspecting missing values.
- Checking duplicate records.
- Converting order and shipping dates into datetime format.
- Preparing numerical and categorical variables.
- Creating derived features from date information.
- Preparing the dataset separately for business analysis and machine learning.

---

#  Exploratory Data Analysis

Extensive exploratory data analysis was performed to understand the business performance of the retail dataset.

##  Overall Business Performance

The analysis calculated:

- Total Sales
- Total Profit
- Total Quantity
- Number of Orders
- Number of Customers
- Overall Profit Margin

### Overall Results

| Metric | Value |
|---|---:|
| Total Sales | $2,326,534.35 |
| Total Profit | $292,296.81 |
| Total Quantity | 38,654 |
| Total Orders | 5,111 |
| Total Customers | 804 |
| Profit Margin | 12.56% |

---

##  Regional Analysis

Sales, profit, orders, customers and profit margins were analyzed across different regions.

| Region | Sales | Profit | Orders | Profit Margin |
|---|---:|---:|---:|---:|
| West | $739,813.61 | $110,798.82 | 1,635 | 14.98% |
| East | $691,828.17 | $94,883.26 | 1,475 | 13.71% |
| Central | $503,170.67 | $39,865.31 | 1,179 | 7.92% |
| South | $391,721.91 | $46,749.43 | 822 | 11.93% |

The analysis shows differences in sales volume and profitability across regions, allowing regional performance to be evaluated beyond sales alone.

---

##  Discount & Profitability Analysis

Different discount ranges were analyzed to understand their relationship with profitability.

| Discount Band | Sales | Profit | Profit Margin |
|---|---:|---:|---:|
| 0% | $1,105,323.79 | $326,718.59 | 29.56% |
| 1–10% | $54,952.50 | $9,099.97 | 16.56% |
| 11–20% | $801,497.92 | $92,498.94 | 11.54% |
| 21–30% | $104,474.07 | -$10,513.45 | -10.06% |
| 31–50% | $195,394.73 | -$48,477.05 | -24.81% |
| 50%+ | $64,891.35 | -$77,030.19 | -118.71% |

Higher discount ranges showed substantially weaker profitability in this dataset, with the highest discount bands producing negative profit.

---

##  Category & Sub-Category Analysis

Product categories and sub-categories were analyzed using sales and profit metrics.

The analysis identified both high-performing and loss-making product groups.

Examples of profitable sub-categories included:

- Copiers
- Phones
- Accessories
- Paper

Examples of loss-making sub-categories included:

- Tables
- Bookcases
- Supplies

This analysis helps identify areas where pricing, discounting or product-level strategy may require further investigation.

---

#  Customer Segmentation — RFM Analysis

Customer behavior was analyzed using **RFM (Recency, Frequency, Monetary)** analysis.

### RFM Components

- **Recency:** How recently a customer made a purchase.
- **Frequency:** How frequently a customer made purchases.
- **Monetary:** How much a customer spent.

Based on RFM scores, customers were grouped into meaningful segments.

### Customer Segments

| Segment | Customers | Total Sales |
|---|---:|---:|
| Loyal / Active | 262 | ~$1.02M |
| High Value | 122 | ~$646K |
| Potential | 220 | ~$472K |
| Needs Attention | 119 | ~$140K |
| Low Engagement | 81 | ~$48K |

RFM analysis was also used to identify high-spending customers who generated negative profit, providing an additional perspective on customer profitability.

---

#  Product & Profitability Analysis

Product-level analysis was performed to identify products with strong sales and profit as well as products generating significant losses.

### Examples of High-Profit Products

- Canon imageCLASS 2200 Advanced Copier
- Fellowes PB500 Electric Punch Plastic Comb Binder
- Hewlett Packard LaserJet 3310 Copier
- Canon PC1060 Personal Laser Copier
- HP Designjet T520

### Examples of High-Loss Products

- Cubify CubeX 3D Printer Double Head Print
- Lexmark MX611dhe
- Cubify CubeX Triple Head
- Chromcraft Bull-Nose Wood Oval Conference Table
- Bush Advantage Collection Racetrack Conference Table

This analysis provides a product-level view of revenue generation and profitability.

---

#  Feature Engineering

Feature engineering was performed to transform raw transaction information into useful machine learning features.

### Date-Based Features

From `Order Date` and `Ship Date`, the following features were created:

- `Shipping_Days`
- `Year`
- `Month`
- `Quarter`
- `Day_of_Week`

### Machine Learning Features

The final feature set consisted of:

- `Sales`
- `Quantity`
- `Discount`
- `Category`
- `Sub-Category`
- `Segment`
- `Region`
- `Ship Mode`
- `Shipping_Days`
- `Year`
- `Month`
- `Quarter`
- `Day_of_Week`

### Target Variable

`Profit`

### Target Leakage Prevention

`Profit_Margin` was intentionally excluded from the machine learning features because it is directly calculated using `Profit`. Including it would introduce target leakage and provide the model with information derived from the target variable.

---

#  Machine Learning

The machine learning objective was to predict the expected profit of an individual sales transaction.

## Models Evaluated

The following regression algorithms were compared:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor

---

##  Data Preprocessing

### Numerical Features

Numerical variables were processed using:

- Median imputation
- Standard scaling

### Categorical Features

Categorical variables were processed using:

- Most-frequent imputation
- One-hot encoding

A `ColumnTransformer` was used to apply the appropriate preprocessing to each feature type.

---

#  Model Performance

The models were evaluated using:

- **MAE (Mean Absolute Error)**
- **RMSE (Root Mean Squared Error)**
- **R² Score**

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | 61.71 | 214.14 | 0.4889 |
| Decision Tree | 24.96 | 138.78 | 0.7853 |
| Random Forest | 21.39 | 141.61 | 0.7765 |
| **Gradient Boosting** | **27.48** | **133.49** | **0.8014** |
| XGBoost | 28.22 | 187.45 | 0.6084 |

### Final Model

The **Gradient Boosting Regressor** was selected as the final model based on its held-out test performance.

### Final Test Performance

- **MAE:** 27.48
- **RMSE:** 133.49
- **R²:** 0.8014

The model explains approximately **80% of the variance in transaction-level profit on the test set**.

---

#  Hyperparameter Tuning

Hyperparameter optimization was performed using **RandomizedSearchCV** with 5-fold cross-validation.

Tuning was performed for:

- Gradient Boosting Regressor
- XGBoost Regressor

The tuned Gradient Boosting model achieved a higher cross-validation score, but its held-out test performance was lower than the original Gradient Boosting configuration.

Therefore, the original Gradient Boosting model was retained as the final model based on test-set performance.

---

#  Model Interpretation

## Feature Importance

The trained Gradient Boosting model was analyzed to understand which features contributed most to its predictions.

The strongest predictive features included:

- Sales
- Discount
- Sub-Category
- Region
- Quantity
- Temporal and shipping-related features

Sales and Discount were particularly influential in the trained model.

---

##  Permutation Importance

Permutation importance was calculated by randomly shuffling individual original input features and measuring the resulting change in model performance.

The analysis showed that:

1. **Sales** had the strongest predictive contribution.
2. **Discount** had a strong predictive contribution.
3. **Sub-Category** provided additional meaningful predictive information.

Permutation importance measures predictive contribution within the model and should not be interpreted as causal impact.

---

#  Model Diagnostics

Residual analysis was performed to evaluate model behavior and identify prediction errors.

### Training Performance

- MAE: 20.77
- RMSE: 43.80
- R²: 0.9574

### Testing Performance

- MAE: 27.48
- RMSE: 133.49
- R²: 0.8014

The difference between training and testing performance indicates some degree of overfitting.

The substantially larger RMSE compared with MAE is influenced by a relatively small number of observations with large prediction errors, particularly high-profit transactions.

---

#  Model Serialization

The final trained model and preprocessing pipeline were saved using **Joblib**.

Saved artifacts:

- `gradient_boosting_profit_model.pkl`
- `profit_preprocessor.pkl`

The saved model and preprocessing pipeline were reloaded and verified to produce identical predictions to the original trained objects.

---

#  Streamlit Application

A Streamlit application was developed to provide an interactive interface for profit prediction.

Users can enter:

- Sales
- Quantity
- Discount
- Category
- Sub-Category
- Segment
- Region
- Ship Mode
- Order Date
- Ship Date

The application automatically derives:

- Shipping Days
- Year
- Month
- Quarter
- Day of Week

The trained model then predicts the expected profit for the entered transaction.

### Run the Application

```bash
cd notebook
python -m streamlit run app.py
