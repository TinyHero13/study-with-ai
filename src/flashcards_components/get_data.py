import pandas as pd

def get_cards():
    df = pd.read_csv('files/cards.csv')
    return df
