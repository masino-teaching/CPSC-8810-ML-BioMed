def get_vars_of_type(data, meta, var_type_key = 'type', var_name_key = 'name', type_kw = 'Continuous'):
    data_columns = data.columns.tolist()
    continuous_vars = meta[(meta[var_type_key] == type_kw) & (meta[var_name_key].isin(data_columns))][var_name_key].tolist()
    return continuous_vars, data[continuous_vars]

def get_vars_of_type_in_list(data, meta, var_type_key = 'type', var_name_key = 'name', type_list = ['Continuous']):
    data_columns = data.columns.tolist()
    continuous_vars = meta[(meta[var_type_key].isin(type_list)) & (meta[var_name_key].isin(data_columns))][var_name_key].tolist()
    return continuous_vars, data[continuous_vars]