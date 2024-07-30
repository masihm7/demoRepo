# save_results.py
def save_categorized_data(df, output_file):
    """Save the DataFrame with categorized data to a CSV file."""
    df[['Sentences', 'Category']].to_csv(output_file, index=False)
