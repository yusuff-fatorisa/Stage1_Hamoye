import pandas as pd
def describe_na(df) :
    na_sum = dict(df.isnull().sum())
    not_na_sum = dict(df.notnull().sum())
    total = len(df)
    na_expand = [ na for na in na_sum.values() if na > 0 ]
    na_list = [ (na_s / total) * 100 for na_s in na_sum.values() if na_s > 0 ]
    not_na_expand = [ not_na for not_na in not_na_sum.values() if not_na < total ]
    not_na_list = [ (not_na_s / total) * 100 for not_na_s in not_na_sum.values() if not_na_s < total ]
    na_notna_df = pd.DataFrame( { 'null_counts' : na_expand, 'null_percent(%)' : na_list, 'not_null_counts' : not_na_expand, 
                               'not_null_percent(%)' : not_na_list}, index = [indices for indices, value in na_sum.items() if value > 0] )
    na_notna_df.index.name = 'column_name'
    
    shape_display = f"{na_notna_df.shape[0]} Rows X {na_notna_df.shape[-1]} Columns"
    # I inserted  this line of code, 14 above to display the rows and columns shape 
    # Of the returned DataFrame as it is in the default behaviour
    # Of a Pandas DataFrame. Although the shape format works correctly, I haven't figured out how to return it correctly
    # Without distorting the DataFrame display graphics output. Maybe I'll figure it out later.
    return na_notna_df


    """This function compiles the missing values of a given DataFrame ."""
    """And displays the output in a nicely formatted DataFrame."""
    """First, it calculates the Series output of the sum of missing values in each column of the given DataFrame.""" 
    """Then it converts the column_name and the corresponding sum of missing values into a key : value pair of a dictionary"""
    """Secondly, it calculates the Series output of the sum of non-missing values in each column of the given DataFrame.""" 
    """Then it converts the column_name and the corresponding sum of non-missing values into a key : value pair of a dictionary"""
    """Next, it calculates the total length of the given DataFrame"""
    """Next, it gets the missing values from the missing values dictionary if the value is greater than Zero"""
    """And it calculates what percentage of the total column is the missing value"""
    """Next, it gets the non-missing values from the non-missing values dictionary if the value is greater than length of the column"""
    """And it calculates what percentage of the total column is the non-missing value"""
    """Finally, it creates a new DataFrame from all the data collated above"""
    """And it gives the index_column a name"""