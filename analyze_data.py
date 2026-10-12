
import pandas as pd

# stap-1: Load cleaned dataset.
df = pd.read_csv("cleaned_indian_books.csv")

# stap-2: Clean column names .
df.columns = df.columns.str.strip()

print("=" * 40)
print("INDIAN BOOKS DATA ANALYSIS")
print("=" * 40)

# stap-3: Total books .
print("\nTotal Books:", len(df))

# stap-4: Unique authors.
if "Authors" in df.columns:
    authors = df["Authors"].dropna().str.strip()
    print("Unique Authors:", authors.nunique())

# stap-5: Language analysis.

if "Language" in df.columns:
    print("\nBooks by Language:")
    print(
        df["Language"]
        .dropna()
        .str.split(", ")
        .explode()
        .value_counts()
        .head(10)
    )
else:
    print("\nLanguage column not found.")

# stap-6: Publication year analysis .
if "First Publish Year" in df.columns:
    years = pd.to_numeric(
        df["First Publish Year"],
        errors="coerce"
    ).dropna()

    print("\nEarliest Publication Year:",
          int(years.min()) if not years.empty else "Not available")

    print("Latest Publication Year:",
          int(years.max()) if not years.empty else "Not available")

    if not years.empty:
        print("\nPublication Year Summary:")
        print(years.describe())

# stap-7: Preview.
print("\nCleaned Data Preview:")
print(df.head(10).to_string(index=False))

print("\nData Analysis Completed!")
