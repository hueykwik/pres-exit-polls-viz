import settings
import json
from pprint import pprint
import csv

def extract_file(year, state, csv_writer):
    json_path = "data/%s/%s.json" % (year, state)
    print(json_path)

    with open(json_path) as data_file:
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

                csv_writer.writerow([year, state, pollname, question, answer_name, dem_pct, rep_pct])

def extract():
    # Output: CSV year pollname answer state democrat_pct republican_pct
    years = settings.YEARS
    states = settings.STATES

    base_output = "data/%s/%s.json"

    with open('data/exit_polls.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(['year', 'state', 'pollname', 'question', 'answer', 'democrat', 'republican'])

        states = ['CA'] # remove later
        for year in years:
            for state in states:
                extract_file(year, state, csv_writer)

if __name__ == "__main__":
    extract()
