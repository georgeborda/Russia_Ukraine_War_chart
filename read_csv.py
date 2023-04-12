import csv

def reader_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter= ',')
        header = next(reader)
        data = []

        for row in reader:
            iterable = zip(header, row)
            dict_row = {key:value for key,value in iterable}
            data.append(dict_row)
        
        return data