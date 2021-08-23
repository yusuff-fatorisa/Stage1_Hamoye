import pandas as pd
def display_dup( df ) :
    object_index = df[df.duplicated()].index
    
    def increase( item ) :
        return item - 1, item, item + 1
    
    object_expand = increase(object_index)
    
    object_collect =sorted([])
    
    for exp in object_expand :
        object_collect.extend(exp)
    #print(f"the_index : {object_collect}")
    
    try :
        new_df = df.loc[object_collect]

    except KeyError :
        df_index = df.index
        new_object_collect = [shunt_index for shunt_index in object_collect if shunt_index in df_index]
        new_df = df.loc[new_object_collect]
    
    return new_df