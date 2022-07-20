"""Report generator."""
import csv
import os

class CSVReportGenerator(object):
    """This class is responsible for creating report in CSV Format."""

    def __init__(self):
        """Initialize."""
        # self.directory = self.get_report_directory()
        # self.create_dir()
        self.file = self.get_file_path()

    def create_dir(self):
        """Create a directory for XML Reports.

        :raises OSError: A system-related error
        """
        try:
            path = os.getcwd()  
            os.makedirs(path)
            print('Creating directory for reports...')
        except OSError as e:
            if e.errno != errno.EEXIST:
                print('Error in creating directory for reports...')
                raise

    def get_report_directory(self):
        """Get full directory where report will be saved."""
        report_directory = os.path.join(os.path.expanduser('~'),
                                        'report')

        print(report_directory)    
        return report_directory

    def get_file_path(self):
        """Generate the filename of the resulting report.

        :param filename: Name or the file
        :type  filename: str
        :return file_path: File path
        """
        # TODO: ask filename as input
        # if filename is None:
        #     filename = ('{options[root]}_{options[source]}_{options[date]}'
        #                 '.{options[type]}'.format(options=self.options))

        file_path = '{dir}/{name}'.format(dir=os.path.expanduser('~'), name='analysis_report')

        return file_path

    def add_report_header(self, header):
        """Add report header."""
        with open(self.file, 'wb') as outcsv:
            writer = csv.DictWriter(outcsv, fieldnames=header)
            writer.writeheader()

    def create_csv_report(self, records):
        """Loop all the records returned by the database query.

        :param list records: Details of the property process.
        """
        # Add headers
        self.add_report_header(records['headers'])

        with open('report.py', 'wb') as outcsv:
            for record in records:
                writer = csv.writer(outcsv)
                writer.writerows(rows)
