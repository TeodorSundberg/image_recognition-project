import pandas as pd
import numpy as np

def add_data_columns(df):
    # 1. Customer Type Classification
    df['customer_type'] = df['customer_type'].apply(lambda x: 'B2B' if x in ['company', 'business'] else 'B2C')

    # 2. Rolling Averages & Moving Sums
    df['7_day_sales_avg'] = df['sales'].rolling(window=7).mean()
    df['30_day_sales_avg'] = df['sales'].rolling(window=30).mean()
    df['90_day_sales_avg'] = df['sales'].rolling(window=90).mean()

    df['7_day_revenue_avg'] = df['revenue'].rolling(window=7).mean()
    df['30_day_revenue_avg'] = df['revenue'].rolling(window=30).mean()
    df['90_day_revenue_avg'] = df['revenue'].rolling(window=90).mean()

    # 3. Seasonality Indicators
    df['month'] = df['date'].dt.month
    df['quarter'] = df['date'].dt.quarter
    df['year'] = df['date'].dt.year

    # 4. Holiday/Event Flags (example for Black Friday)
    df['is_black_friday'] = df['date'].apply(lambda x: 1 if x.month == 11 and x.weekday() == 4 else 0)

    # 5. Customer Lifetime Value (CLV) Proxy
    df['customer_revenue'] = df.groupby('customer_id')['revenue'].transform('sum')
    df['avg_order_value'] = df.groupby('customer_id')['order_value'].transform('mean')

    # 6. Purchase Frequency Metrics
    df['orders_per_customer'] = df.groupby('customer_id')['order_id'].transform('count')
    df['avg_time_between_purchases'] = df.groupby('customer_id')['date'].transform(lambda x: x.diff().mean())

    # 7. Sales Growth Rates (Month-over-Month and Year-over-Year)
    df['mom_growth'] = df['sales'].pct_change(periods=30)
    df['yoy_growth'] = df['sales'].pct_change(periods=365)

    # 8. Product Popularity Scores
    product_sales = df.groupby('product_id')['sales'].sum().reset_index()
    df['product_popularity'] = df['product_id'].map(product_sales.set_index('product_id')['sales'])

    # 9. Outlier Detection Features (example for sales spikes)
    sales_median = df['sales'].median()
    sales_std = df['sales'].std()
    df['sales_outlier'] = df['sales'].apply(lambda x: 1 if abs(x - sales_median) > 3 * sales_std else 0)

    # Aggregate by month to create the final output
    monthly_data = df.groupby(['year', 'month']).agg(
        CLV_proxy=('customer_revenue', 'sum'),
        sales_avg_7d=('7_day_sales_avg', 'mean'),
        sales_avg_30d=('30_day_sales_avg', 'mean'),
        sales_avg_90d=('90_day_sales_avg', 'mean'),
        revenue_avg_7d=('7_day_revenue_avg', 'mean'),
        revenue_avg_30d=('30_day_revenue_avg', 'mean'),
        revenue_avg_90d=('90_day_revenue_avg', 'mean'),
        is_black_friday=('is_black_friday', 'sum'),
        avg_order_value=('avg_order_value', 'mean'),
        orders_per_customer=('orders_per_customer', 'mean'),
        avg_time_between_purchases=('avg_time_between_purchases', 'mean'),
        mom_growth=('mom_growth', 'mean'),
        yoy_growth=('yoy_growth', 'mean'),
        product_popularity=('product_popularity', 'mean'),
        sales_outlier=('sales_outlier', 'sum')
    ).reset_index()

    # Reshape data to meet the "category", "month", "value" format
    reshaped_data = pd.melt(monthly_data, id_vars=['year', 'month'], 
                            value_vars=monthly_data.columns[2:], 
                            var_name='category', value_name='value')
    
    # Add a month string (e.g., "2025 Jan")
    reshaped_data['month'] = reshaped_data['month'].apply(lambda x: f'{x} {reshaped_data["year"].iloc[0]}')
    reshaped_data.drop('year', axis=1, inplace=True)
    
    return reshaped_data

# Example usage
df = pd.read_csv("sales_data.csv", parse_dates=['date'])
df_transformed = add_data_columns(df)
