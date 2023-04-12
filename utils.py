def get_column_data(data, column):
    labels = list(map(lambda item : item[column], data))
    values = list(map(lambda item : item['personnel'], data))
    return labels, values