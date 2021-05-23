
# IMPORT CSV as DATAFRAMES with PANDAS
import pandas
df_calls2016 = pandas.read_csv ( r'/dw/MyDrive/Colab_Notebooks/TDI_test/Calls_for_Service_2016.csv' )
df_calls2017 = pandas.read_csv ( r'/dw/MyDrive/Colab_Notebooks/TDI_test/Calls_for_Service_2017.csv' )
df_calls2018 = pandas.read_csv ( r'/dw/MyDrive/Colab_Notebooks/TDI_test/Calls_for_Service_2018.csv' )
df_calls2019 = pandas.read_csv ( r'/dw/MyDrive/Colab_Notebooks/TDI_test/Calls_for_Service_2019.csv' )
df_calls2020 = pandas.read_csv ( r'/dw/MyDrive/Colab_Notebooks/TDI_test/Call_for_Service_2020.csv'  )

# display data to grasp it's structure
df_calls2016.head(3)
# with pandas.option_context('display.max_rows', 10, 'display.max_columns', None): display( df_calls2020 )


print( str( df_calls2020 ['Type'].value_counts(dropna=False) ))
print('\n')
display ( df_calls2020 ['Type'].value_counts(dropna=False) )
#df_calls2020 ['TypeText'].value_counts(dropna=False)
print('\n')
print( list(df_calls2020 ['Type'].value_counts(dropna=False)) )

most_frecuent = df_calls2020 ['Type'].value_counts(dropna=False).idxmax()
print ('Most_frecuent type:           ', most_frecuent)
print ('Counts for the Most frecuent: ', df_calls2020 ['Type'].value_counts(dropna=False)[ most_frecuent ])
# Calculate the fraction of the most common within the total
print ('Most frecuent fraction:       ', '{:.5f}'.format((df_calls2020 ['Type'].value_counts(dropna=False)[ most_frecuent ]) / len(df_calls2020) ) )

# S02.P02
df_calls2016_counts = df_calls2016 ['Type_'].value_counts(dropna=False)
df_calls2016_counts.rename('Type_2016', inplace=True)
print ( 'df_calls2016_counts:   ', len( df_calls2016_counts) )


df_calls2020_counts = df_calls2020 ['Type'] .value_counts(dropna=False)   # pD series with 1 column (counts) and index
df_calls2020_counts.rename('Type_2020', inplace=True)
print ( 'df_calls2020_counts:   ', len( df_calls2020_counts) )
print('\n', end='')

# definition of decrease in volume
df_all = pandas.concat([ df_calls2020_counts , df_calls2016_counts], axis = 1)
import numpy
df_all.replace({ numpy.NaN : 0}, inplace=True)
df_all['decrease'] = df_all['Type_2016'] - df_all[ 'Type_2020'] # create difference column
display (df_all)
print('\n', end='')

# find the larget decrease
max_value       = df_all['decrease']. max() 
max_value_index = df_all['decrease'].idxmax()
print('max_value:          ', max_value )
print('max_value_index:    ', max_value_index )
print('\n', end='')
print(r'--- category ','\'', max_value_index ,'\' ---', sep='')
print(df_all.loc[[ max_value_index ]])	# print a specific row
print('\n', end='')

# calcuate fraction of decrease.
print ('The volume of calls in 2016 was: ')
print (df_calls2016_counts.sum())
print ('The fraction occupied by the decrease was:')
print ('{:.5f}'.format( max_value / df_calls2016_counts.sum() ) )

# check colum names
print('df_calls2016:  ', len ( df_calls2016.columns), type ( df_calls2016.columns) )
print('df_calls2016:  ', df_calls2016.columns)

# extract colum names and convert to list
list_calls2016 = df_calls2016.columns.values.tolist()
list_calls2017 = df_calls2017.columns.values.tolist()
list_calls2018 = df_calls2018.columns.values.tolist()
list_calls2019 = df_calls2019.columns.values.tolist()
list_calls2020 = df_calls2020.columns.values.tolist()

# Compare the list to find the common names
list_common = set(list_calls2016) & set(list_calls2017) & set(list_calls2018) & set(list_calls2019) & set(list_calls2020) 
print('identical column names: ', len(list_common))
print(list_common)

# find the different names
list_different   = set(list_calls2016) - set(list_common) 
print(list_different)

# have to rename columns {'TimeArrive', 'Type_'}
df_calls2016.rename(columns={  'Type_'        :'Type'        }, inplace=True)
df_calls2017.rename(columns={  'Type_'        :'Type'        }, inplace=True)
df_calls2018.rename(columns={  'Type_'        :'Type'        }, inplace=True)
df_calls2019.rename(columns={  'TimeArrival'  :'TimeArrive'  }, inplace=True)

# concat all the calls resoluted on new year's day -- all 5 years included
df_newyear = pandas.concat( [ df_calls2016[ df_calls2016['TimeClosed'].str.contains( '01/01/')]  , 
                              df_calls2017[ df_calls2017['TimeClosed'].str.contains( '01/01/')]  ,
                              df_calls2018[ df_calls2018['TimeClosed'].str.contains( '01/01/')]  ,
                              df_calls2019[ df_calls2019['TimeClosed'].str.contains( '01/01/')]  ,
                              df_calls2020[ df_calls2020['TimeClosed'].str.contains( '01/01/')]  ,
                             ], axis=0)	

display (df_newyear.head(3))
print ('df_newyear lenght:    ', len(df_newyear))

#remove ducplicates

df_newyear2 = df_newyear.drop_duplicates(subset=['TimeClosed'])
print ('df_newyear2 lenght:    ', len(df_newyear2))

print ('duplicate rows removed:    ', len(df_newyear) -len(df_newyear2) )
