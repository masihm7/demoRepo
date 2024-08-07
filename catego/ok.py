import pandas as pd

# Data to be saved
data = {
    "Sentence": [
        "The team celebrated their championship win with a grand parade through the city.",
        "Serena Williams broke another record at the Australian Open with her powerful serve.",
        "The coach implemented a new strategy to improve the team's defensive line.",
        "The marathon runner finished in under two hours, setting a new world record.",
        "The soccer match was postponed due to heavy rain and unsafe playing conditions.",
        "The company reported a 15% increase in quarterly profits due to higher sales.",
        "The board of directors met to discuss the upcoming merger with a major competitor.",
        "The startup received venture capital funding to accelerate its product development.",
        "The CEO announced a new initiative to enhance employee work-life balance.",
        "The market research indicated a growing demand for eco-friendly consumer products.",
        "Scientists discovered a new exoplanet in the habitable zone of its star system.",
        "The research team published their findings on the effects of climate change on coral reefs.",
        "A breakthrough in quantum computing could revolutionize data processing speeds.",
        "The experiment aimed to understand the genetic basis of inherited diseases.",
        "Astronomers observed unusual activity in a distant galaxy, leading to new theories about dark matter."
    ],
    "Category": [
        "Sports",
        "Sports",
        "Sports",
        "Sports",
        "Sports",
        "Business",
        "Business",
        "Business",
        "Business",
        "Business",
        "Science",
        "Science",
        "Science",
        "Science",
        "Science"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('categorized_sentences.csv', index=False)
