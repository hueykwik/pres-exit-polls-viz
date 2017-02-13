
import requests
import os
import settings

def download():
    years = settings.YEARS
    states = settings.STATES

    base_url = "http://data.cnn.com/ELECTION/%s/%s/xpoll/Pfull.json"
    base_output = "data/%s/%s.json"

    for year in years:
        for state in states:
            url = base_url % (year, state)
            file = requests.get(url)

            output_path = base_output % (year, state)

            dir = os.path.dirname(output_path)

            if not os.path.exists(dir):
                os.makedirs(dir)

            with open(output_path, "w") as output:
                output.write(file.text)

if __name__ == "__main__":
    download()
