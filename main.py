import requests
import csv

url = "https://openlibrary.org/search.json"

params = {
    "q": "Indian authors ",
    "limit": 20,
    "fields": "title,author_name,first_publish_year,language"
}

response = requests.get(

   url,
   params=params,
   headers={"User-Agent": "SmartProductScraper/1.0"},
   timeout = 20
)
response.raise_for_status()

data = response.json()
books = data.get("docs", [])

with open(
    "indian_books.csv",
    "w",
    newline="",
    encoding="utf-8-sig"
) as file:
    writer = csv.writer(file)

    writer.writerow([
        "Title",
        "Authors",
        "First Publish Year",
        "Language"  
    ])

    for book in books:
        writer.writerow([
            book.get("title", ""),
            ", ".join(book.get("author_name", [])),
            book.get("first_publish_year", ""),
            ", ".join(book.get("language", []))
        ])

print("Books data collection completed!")
print("Recordssaved:", len(books))
print("File: indian_books.csv")

