import csv
from datetime import datetime

def format_blood_pressure_csv(input_file, output_file):
    """
    Formats a CSV file containing blood pressure data.
    This function reads an input CSV file where the first column contains timestamps in ISO 8601 format,
    and the remaining columns contain blood pressure data. It writes a new CSV file with separate columns
    for the date, time, and timezone extracted from the timestamp, along with the original blood pressure data.
    Args:
        input_file (str): The path to the input CSV file.
        output_file (str): The path to the output CSV file.
    Raises:
        ValueError: If the timestamp in the input file does not match the expected format.
    """
    with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        in_headers = next(reader)[0].split(';')
        out_headers = ['Date', 'Time', 'Timezone'] + in_headers[1:] # Skip the first column (Date)
        
        writer = csv.DictWriter(outfile, out_headers)
        
        writer.writeheader()
        for row in reader:
            row_dict = dict(zip(in_headers, row))
            timestamp = row_dict['Date']
            try:
                try:
                    dt = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%f%z')
                except ValueError:
                    dt = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S%z')
            except ValueError:
                dt = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S')
            row_dict['Date'] = dt.strftime('%Y-%m-%d')
            row_dict['Time'] = dt.strftime('%H:%M:%S')
            row_dict['Timezone'] = dt.strftime('%z') # TODO: Convert timezone to a more readable format (e.g., 'UTC+01:00') for better clarity in the output CSV
            writer.writerow(row_dict)

if __name__ == "__main__":
    input_file = 'bloodPressure.csv'
    output_file = 'bloodPressure_formatted.csv'
    format_blood_pressure_csv(input_file, output_file)