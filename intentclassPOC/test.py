import pandas as pd
df = pd.read_csv('batch_records_latest.csv')
df= df['Description']
dataframe_length = len(df)
dataframe_list = []
for i,chunk in enumerate(pd.read_csv('batch_records_latest.csv',\
                                     chunksize=5)):
    chunk = chunk['Description']
    dataframe_list.append(chunk)

test = "test"
