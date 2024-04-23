import fitz
import pandas as pd

def extract_table_from_pdf(pdf, csv):
    doc = fitz.open(pdf)
    table_rows = []

    # i = 1
    for page in doc:
        tabs = page.find_tables()
        if tabs:
            tab = tabs[0]
            df = tab.to_pandas()
            table_rows += df.values.tolist()
            # print("page done", i)
            # i += 1

    df = pd.DataFrame(table_rows, columns=df.columns)
    df.to_csv(csv, index=False)

if __name__ == "__main__":
    extract_table_from_pdf("FB_Purchase_Details.pdf", "purchase_data.csv")
    extract_table_from_pdf("FB_Redemption_Details.pdf", "redemption_data.csv")