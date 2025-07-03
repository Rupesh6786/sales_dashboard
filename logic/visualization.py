import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_trends(df):
    if 'Date' in df.columns and 'Sales' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
        monthly_sales = df.groupby(df['Date'].dt.to_period('M')).sum(numeric_only=True)
        monthly_sales.index = monthly_sales.index.to_timestamp()

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(monthly_sales.index, monthly_sales['Sales'], marker='o')
        ax.set_title("Monthly Sales Trend")
        ax.set_xlabel("Date")
        ax.set_ylabel("Sales")
        ax.grid(True)
        plt.tight_layout()
        return fig
    else:
        print("Dataset must contain 'Date' and 'Sales' columns")
        return None

def plot_graphs(df):
    if 'Category' in df.columns and 'Sales' in df.columns:
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Category', y='Sales', data=df, ci=None)
        plt.title("Sales by Category")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print("Dataset must contain 'Category' and 'Sales' columns")
