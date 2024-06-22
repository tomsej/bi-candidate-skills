import json

import requests
import argparse

class HolidaysAPI:

    def __init__(self, year: str):
        self.url: str = "https://kayaposoft.com/enrico/json/v2.0/?action=getHolidaysForYear&year={year}&country=cze&holidayType=all"
        self.year: str = year

    def process(self):
        """Processing of API call."""

        try:
            api_url = self.url.format(year=self.year)
            r = requests.get(api_url)
            json_list = json.loads(r.text)
            result = ""
            for item in json_list:
                item_tmp = json.dumps(item)
                result += str(item_tmp) + "\n"

            filename = f"{self.year}.json"
            
            with open(filename, 'w') as file:
                json.dump(json_list, file, indent=4)
            
            print(f"Data from '{api_url}' for year {self.year} has been downloaded to filename")

        except Exception as e:
            raise Exception(e)

def main():

    parser = argparse.ArgumentParser()
    
    
    parser.add_argument('-y', '--year', type=str, required=True) # Define the argument from CLI for -y
    args = parser.parse_args()
    api = HolidaysAPI(args.year).process()

if __name__ == "__main__":
    main()