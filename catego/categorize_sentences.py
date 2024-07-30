# categorize_sentences.py
from gemini_sdk import GeminiClient

# Initialize the Gemini client
client = GeminiClient(api_key='AIzaSyA1sleMnKKmGE9JwiCGGklPKVQgHj7yc7Y')

def categorize_sentence_with_gemini(sentence):
    """Categorize a single sentence using Gemini."""
    response = client.classify_text(
        text=sentence,
        categories=['Weather', 'Sentiment', 'Education']  # Define your categories
    )
    return response['category']  # Adjust according to Gemini's response format

def categorize_sentences(df):
    """Categorize sentences in the DataFrame using Gemini."""
    df['Category'] = df['Sentences'].apply(categorize_sentence_with_gemini)
    return df
