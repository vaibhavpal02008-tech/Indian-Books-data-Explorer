import pandas as pd

# 1: Load original Dataset
df = pd.read_csv("indian_books.csv")

print("Original rows:", len(df))

# 2: Remove extra spaces from text
for colum in df.select_dtypes(include=["object"]).columns:
    df[colum] = df[colum].str.strip()

# 3: Replace empty text with missing values
df = df.replace(r"^s*$", pd.NA, regex=True)

# 4: Remove rows without a book title
df = df.dropna(subset=["Title"])

# 5: Remove duplicate records 
df = df.drop_duplicates(
subset=["Title", "Authors"],
keep="first" 
)

# 6: Save cleaned dataset 
df.to_csv(
    "cleaned_indian_books.csv",
    index=False,
    encoding="utf-8-sig"    
)

print("Cleaned rows:", len(df))
print("Removed rows:", len(pd.read_csv("indian_books.csv")) - len(df))
print("Saved: cleaned_indian_books.csv")
print("\nCleaned data preview:")
print(df.head(10).to_string(index=False))

