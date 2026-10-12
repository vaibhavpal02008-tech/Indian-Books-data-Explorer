
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Indian Books Explorer",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Indian Books Explorer")
st.write("Explore, search and analyze your book dataset.")

# { Load data }

try:
    df = pd.read_csv("cleaned_indian_books.csv")
except FileNotFoundError:
    st.error("cleaned_indian_books.csv file not found.")
    st.stop()

df.columns = df.columns.str.strip()

# {Search}

search = st.text_input("🔍 Search books or authors")

filtered = df.copy()

if search:
    mask = (
        filtered["Title"].fillna("").str.contains(
            search, case=False, regex=False
        )
        | filtered["Authors"].fillna("").str.contains(
            search, case=False, regex=False
        )
    )
    filtered = filtered[mask]

# {Language filter}

if "Language" in filtered.columns:
    all_languages = (
        filtered["Language"]
        .dropna()
        .str.split(", ")
        .explode()
        .str.strip()
    )
    language_options = sorted(all_languages.unique().tolist())

    selected = st.selectbox(
        "Filter by language",
        ["All languages"] + language_options
    )

    if selected != "All languages":
        filtered = filtered[
            filtered["Language"]
            .fillna("")
            .str.split(", ")
            .apply(lambda values: selected in values)
        ]

# {Metrics}

col1, col2, col3 = st.columns(3)

col1.metric("Books", len(filtered))

if "Authors" in filtered.columns:
    col2.metric("Authors", filtered["Authors"].nunique())
else:
    col2.metric("Authors", "N/A")

if "First Publish Year" in filtered.columns:
    years = pd.to_numeric(
        filtered["First Publish Year"], errors="coerce"
    )
    col3.metric("Publication Years", years.nunique())
else:
    col3.metric("Publication Years", "N/A")

st.subheader("📖 Book Dataset")
st.dataframe(filtered, width="stretch")

# {Download}

csv_data = filtered.to_csv(index=False).encode("utf-8-sig")

st.download_button(
    label="⬇️ Download CSV",
    data=csv_data,
    file_name="filtered_books.csv",
    mime="text/csv"
)

# {Language chart}

if "Language" in filtered.columns:
    st.subheader("📊 Books by Language")

    language_counts = (
        filtered["Language"]
        .dropna()
        .str.split(", ")
        .explode()
        .str.strip()
        .value_counts()
        .head(10)
    )

    if not language_counts.empty:
        st.bar_chart(language_counts)

st.caption("Data source: Open Library API")
