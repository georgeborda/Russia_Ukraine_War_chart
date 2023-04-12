import read_csv
import utils
import charts

def main():
    data = read_csv.reader_csv('./russia_losses_personnel.csv')
    column = 'date'
    labels, values = utils.get_column_data(data, column)
    charts.generate_line_chart(labels, values)

    
if __name__ == '__main__':
    main()