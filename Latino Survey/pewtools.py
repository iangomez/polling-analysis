import pandas as pd

# easily do weighting for survey data
def weighted_frequency(df,meta,x,y):
    a = pd.Series(df[[x,y]].groupby(x).sum()[y])/df[y].sum()
    b = a.index.map(meta.variable_value_labels[x])
    c = a.values
    df_temp = pd.DataFrame({'Labels': b, 'Frequency': c})
    return df_temp

def quick_crosstab(df,meta,x,y,weights):
    crosstab = pd.crosstab(
                            df[x].map(meta.variable_value_labels[x]), \
                            df[y].map(meta.variable_value_labels[y]),  \
                            weights, aggfunc=sum, dropna=True, normalize='columns'
                            ). \
                        loc[meta.variable_value_labels[x].values()]. \
                        loc[:,meta.variable_value_labels[y].values()] *100
    return(crosstab)  # values in percentages