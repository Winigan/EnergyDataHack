import pandas as pd

csvname = 'Vague1Lot2' + '.csv'
df1 = pd.read_csv(csvname)
print(df1.info())
