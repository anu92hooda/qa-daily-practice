import csv
import  json
import pytest

def load_test_data():

    with open("testdata.json") as f:
        return json.load(f)

@pytest.mark.parametrize("data", load_test_data())
def test_read(data):

    print(f"username:{data['username']} , password:{data['password']}")

#

def load_csv_data():

    with open("testdata.csv") as f:
        reader= csv.DictReader(f)
        return list(reader)

@pytest.mark.parametrize("data", load_csv_data())
def test_csv_read(data):
    print(f"username:{data['username']}  , password: {data['password']}")

