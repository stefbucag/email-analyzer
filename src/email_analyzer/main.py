"""Analyzes emails."""
from argparse import ArgumentParser
import time
import csv

from src.email_analyzer.analyzer import EmailAnalyzer
from src.common.csv_report_generator import CSVReportGenerator as ReportGenerator

def get_arg_parser():
    """Get arguments."""
    description = "Extract email history and process."
    num_desc = 'Number of sentences in the summary'

    parser = ArgumentParser(description=description)
    parser.add_argument('input', type=str, help='Input CSV')
    parser.add_argument('--length', type=int, default=2, help=num_desc)
    parser.add_argument('--filname', type=str, help='Report filename')

    return parser

def __run():
    """Run EmailAnalyzer Application."""
    start_time = time.time()

    arg_parser = get_arg_parser()
    options = arg_parser.parse_args()

    # Analyze emails
    emails = EmailAnalyzer(options.input, options.length)
    email_analysis = emails.process_emails()

    # TODO: needs approval from client
    # Store analysis results to file
    # generator = ReportGenerator()
    # generator.create_csv_report(email_analysis)

    print('Total Run time: %s', time.time() - start_time)


if __name__ == '__main__':
    __run()
