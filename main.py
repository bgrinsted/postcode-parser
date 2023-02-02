import re

import pandas as pd


class Postcode:
    # compile the regex pattern for UK postcodes
    pattern = re.compile(r"[A-Z]{1,2}[0-9][A-Z0-9]?\s[0-9][A-Z]{2}")

    # read LondonPostcodes.csv as a set for faster checking
    with open("data/input/LondonPostcodes.csv", "r", encoding="ISO-8859-1") as f:
        london_postcodes = set(f.read().splitlines())

    def __init__(self, value):
        self.value = value
        self.value_clean = value.replace("\s+", " ").strip()
        self.valid = re.fullmatch(Postcode.pattern, self.value_clean)
        self.category = None

    def categorize(self):
        if self.valid:
            if self.value_clean in Postcode.london_postcodes:
                self.category = "valid_london"
            else:
                self.category = "valid_notlondon"
        else:
            self.category = "invalid"
        return self.category


if __name__ == "__main__":
    # read InputFile.csv as a pandas dataframe
    df = pd.read_csv("data/input/InputFile.csv", encoding="ISO-8859-1", header=None)

    # categorize the postcodes and add the category as a new column to the dataframe
    df[1] = df[0].apply(lambda x: Postcode(x).categorize())

    # divide the postcode values by category and write to the output files
    for category, values in df.groupby(1):
        values[0].to_csv(f"data/output/{category}.csv", index=False, header=False)

    # print some relevant stats to console
    print(f"{len(df)} values read from InputFile.csv and categorised as:")
    print(df[1].value_counts().to_string())
