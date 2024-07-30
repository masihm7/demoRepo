# main.py
import download_and_load
import categorize_sentences
import save_results

def main():
    # Specify file paths
    input_file = 'sentences.csv'  # Update with your file path
    output_file = 'categorized_sentences.csv'
    
    # Load the dataset
    df = download_and_load.load_dataset(input_file)
    
    # Categorize sentences
    df = categorize_sentences.categorize_sentences(df)
    
    # Save the results
    save_results.save_categorized_data(df, output_file)
    
    print("Categorization complete. Results saved to:", output_file)

if __name__ == "__main__":
    main()
