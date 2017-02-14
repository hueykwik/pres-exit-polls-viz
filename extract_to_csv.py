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

        for poll in data['polls']:
            pollname = poll['pollname']
            question = poll['question']

            for answer in poll['answers']:
                answer_name = answer['answer']

                dem_pct = None
                rep_pct = None
                for cand_answer in answer['candidateanswers']:
                    cand_id = cand_answer['id']
                    pct = cand_answer['pct']
                    if cand_id == 1746 or cand_id == 1918:
                        dem_pct = pct
                    if cand_id == 8639 or cand_id == 893:
                        rep_pct = pct

                csv_writer.writerow(['2016', 'CA', pollname, question, answer_name, dem_pct, rep_pct])

def convert():
    # Output: CSV year pollname answer state democrat_pct republican_pct
    years = settings.YEARS
    states = settings.STATES

    with open('data/exit_polls.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(['year', 'state', 'pollname', 'question', 'answer', 'democrat', 'republican'])

        convert_file(csv_writer)

if __name__ == "__main__":
    convert()
