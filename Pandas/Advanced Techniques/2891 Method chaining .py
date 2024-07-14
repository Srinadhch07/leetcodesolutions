import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    #print(animals[animals['weight'] > 100][['name']])
    return animals.sort_values(['weight'],ascending=False)[animals['weight'] > 100][['name']]
    
    
