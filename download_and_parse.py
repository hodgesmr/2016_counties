import csv
import json
import tempfile
import urllib

CLINTON_PERCENT_COLUMN = 4
TRUMP_PERCENT_COLUMN = 5
STATE_COLUMN = 8
COUNTY_COLUMN = 9
ID_COLUMN = 10

output = {}

URL = 'https://raw.githubusercontent.com/tonmcg/County_Level_Election_Results_12-16/master/2016_US_County_Level_Presidential_Results.csv'

with tempfile.NamedTemporaryFile() as tmp:
    urllib.urlretrieve(URL, tmp.name)

    with open(tmp.name, 'rb') as input_file:
        reader = csv.reader(input_file)
        header = next(reader)

        for row in reader:
            output[row[ID_COLUMN]] = {
                'county': row[COUNTY_COLUMN],
                'state': row[STATE_COLUMN],
                'clinton': row[CLINTON_PERCENT_COLUMN],
                'trump': row[TRUMP_PERCENT_COLUMN]
            }

with open('./2016_county_results.json', 'wb') as output_file:
    json.dump(output, output_file)
