
import requests
import os

def download():
    years = ["2012", "2016"]
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

    base_url = "http://data.cnn.com/jsonp/ELECTION/%s/%s/xpoll/Pfull.json"
    base_output = "data/%s/%s.json"

    for year in years:
        for state in states:
            url = base_url % (year, state)
            file = requests.get(url)
            print(file.text)
            output_path = base_output % (year, state)

            dir = os.path.dirname(output_path)

            if not os.path.exists(dir):
                os.makedirs(dir)

            with open(output_path, "w") as output:
                output.write(file.text)

if __name__ == "__main__":
    download()
