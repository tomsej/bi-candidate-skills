import json

import requests

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

            print(result)

        except Exception as e:
            raise Exception(e)

def main():
    api = HolidaysAPI("2021").process()

if __name__ == "__main__":
    main()