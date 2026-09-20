import pandas as pd
from sqlalchemy import create_engine
from getpass import getpass
from urllib.parse import quote_plus

password = getpass("Enter your PostgreSQL password: ")

encoded_password = quote_plus(password)

DATABASE_URL = f"postgresql://postgres:{encoded_password}@localhost:5432/spotify_dw"

engine = create_engine(DATABASE_URL)

tables = [
    "fact_tracks",
    "dim_artist",
    "dim_album",
    "dim_date"
]

for table in tables:
    df = pd.read_sql(f"SELECT * FROM {table}", engine)

    output = f"data/dashboard/{table}.csv"

    df.to_csv(output, index=False)

    print(f"Exported {output}")

print("Done!")
