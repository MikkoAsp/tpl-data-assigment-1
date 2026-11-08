import pandas as pd

# Show all columns and don't wrap the table
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)


def analyze_data(df):
    rows, columns = df.shape

    print("\nData analysis")
    print(f"Shape: {rows} rows, {columns} columns")

    print("\n--- First two records ---")
    print(df.head(2).to_string(index=False))

    print("\n--- Last two records ---")
    print(df.tail(2).to_string(index=False))
    print("\n")