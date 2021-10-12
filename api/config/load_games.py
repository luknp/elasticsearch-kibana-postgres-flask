import pandas as pd
import os, urllib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URL

    

def main():
    df = pd.read_csv("thegamesdb.csv")
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine, autoflush=True)
    with Session() as session:
        df.to_sql('games', con=engine, if_exists='replace',index=True)
        
        
        
if __name__ == "__main__":
    main()
