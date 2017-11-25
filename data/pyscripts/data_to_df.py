import pandas

# Convert raw Fortum data CSV to pandas dataframe and save it

fp = '../day.data'
df = pandas.read_csv(fp, sep=';')
df['datetime'] = df['datetime'].apply(pandas.to_datetime)
df.to_pickle('fortum.pkl')

