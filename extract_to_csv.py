import settings
import json
from pprint import pprint
import csv

def convert_file(csv_writer):
    # Goes through each file and writes a row
    # TODO: for year in years, for state in states

    # Just use 2016/CA.json as an example for now

    with open('data/2016/CA.json') as data_file:
        data = json.load(data_file)

        pprint(data['polls'][0])
        #csvwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        #csv_writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


def convert():
    # Output: CSV year pollname answer state democrat_pct republican_pct
    years = settings.YEARS
    states = settings.STATES

    with open('data/exit_polls.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(['year', 'pollname', 'answer', 'state', 'democrat', 'republican'])

        convert_file(csv_writer)

if __name__ == "__main__":
    convert()
