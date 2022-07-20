"""Reads file."""
import pandas as pd


class CSVReader(object):
    """Reader iterates over lines in the file."""

    def __init__(self, input_file):
        """Initialize."""
        self.file = input_file

    def open_file(self):
        """Open input file."""
        try:
            self.file = open(self.file, "rt")
        except FileNotFoundError:
            print('File not found')
            exit()

    def read(self, skip_header=True):
        """Read CSV and returns a data frame ."""
        self.open_file()

        data_frame = pd.read_csv(self.file)
        return data_frame

    def csv_to_dict(self):
        """Convert each csv row to a dictionary

        :return dict_rows 
        :rtype: list
        """
        data_frame = self.read()

        # Get the header
        header = [colName.lower().replace(' ', '_') for colName in list(data_frame)]

        dict_rows = []
        for index, row in data_frame.iterrows():
            csv_row = dict(zip(header, row))
            dict_rows.append(csv_row)

        return dict_rows

    def close_file(self):
        """Close input file."""
        self.file.close()
