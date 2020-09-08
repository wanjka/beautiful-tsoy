import csv

def csv_writer(header, data, path):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(header)
        for line in data:
            writer.writerow(line)

