import pandas as pd
import matplotlib.pyplot as plt

# (Load cleaned data)

df = pd.read_csv("cleaned_indian_books.csv")
df.columns = df.columns.str.strip()

# (Check language column)

if "Language" not in df.columns:
    print("Language column not found!")
else:
    # (Count books by language)
    
    languages = (
        df["Language"]
        .dropna()
        .str.split(", ")
        .explode()
        .str.strip()
        .value_counts()
        .head(10)
    )

    if languages.empty:
        print("No language data available.")
    else:
        languages.plot(kind="bar")

        plt.title("Books by Language")
        plt.xlabel("Language Code")
        plt.ylabel("Number of Books")
        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.savefig("language_chart.png")
        plt.show()

        print("Chart saved as language_chart.png")
