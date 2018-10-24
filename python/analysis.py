#### THIS IS JUST PSEUDO CODE!!! ####

# Find out cardinality on all columns and then one-hot encoding
cardinality = [[col, len(df[col].unique())] for col in df.columns]
cardinality = pd.DataFrame(cardinality)
cardinality.columns = 'column card'.split()

column_list_ohe = cardinality[cardinality['card'] <= max_level_to_OHE]
column_list_ohe = column_list_ohe['column'].values.tolist()

# 10 minutes to pandas
df.mean()
df.mean(1)

df.apply(np.cumsum)
df.apply(lambda x: x.max() - x.min())

df.col.str.lower()
df.col.str.contains()

df.describe(include = ['O']) # non-numeric columns only
df.describe(include = 'all') # all columns

# map method with dictionary to change value
mapping_dict = {
    'Android': 'Android',
    'Chrome OS': 'Chrome OS',
    'Linux': 'Linux',
    'Mac OS': 'macOS',
    'No OS': 'No OS',
    'Windows': 'Windows',
    'macOS': 'macOS'
}
laptops['os'] = laptops['os'].map(mapping_dict)

# cleaning data with str.split(n=1, expand=True), strip() to get rid of leading and trailing space
for i in ['storage_1','storage_2']:
    s_capacity = i+'_capacity_gb'
    s_type = i+'_type'
    laptops[[s_capacity,s_type]]=laptops[i].str.split(n=1,expand=True)
    laptops[s_capacity]=laptops[s_capacity].astype(float)
    laptops[s_type]=laptops[s_type].str.strip()
laptops.drop(['storage','storage_1','storage_2'],axis=1,inplace=True)

# rename column
laptops.rename({"screen_size": "screen_size_inches"}, axis=1, inplace=True)

# use function and list comprehension to clean column names
def clean_col(s):
    s = s.strip()
    s = s.replace('Operating System','os')
    s = s.replace(' ','_')
    s = s.replace('(','')
    s = s.replace(')','')
    s = s.lower()
    return s    
laptops.columns = [clean_col(i) for i in laptops.columns]