from pathlib import Path
import pandas as pd

data_path = Path(__file__).parent/"Data"

df = pd.read_csv(data_path/"prog_book.csv")
print(df.head())


df.head().to_csv(data_path/"prog_book_head.csv")

df.head().to_csv(data_path/"prog_book_head.csv")