import csv
from datetime import datetime

def format_blood_pressure_csv(input_file, output_file):
    with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        in_headers = next(reader)[0].split(';')
        out_headers = ['Date', 'Time', 'Timezone'] + in_headers[1:] # [1:] To avoid first column, Date
        writer = csv.DictWriter(outfile, out_headers)
        
        writer.writeheader()
        for row in reader:
            row_dict = {in_headers[i]: row[i] for i in range(len(in_headers))}
            timestamp = row_dict['Date']
            dt = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%f%z')
            row_dict['Date'] = dt.strftime('%Y-%m-%d')
            row_dict['Time'] = dt.strftime('%H:%M:%S')
            row_dict['Timezone'] = dt.strftime('%z') # TODO: Improve Timezone output structure
            writer.writerow(row_dict)

if __name__ == "__main__":
    input_file = 'bloodPressure.csv'
    output_file = 'bloodPressure_formatted.csv'
    format_blood_pressure_csv(input_file, output_file)