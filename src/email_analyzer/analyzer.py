import re

from textblob import TextBlob

from src.common.csv_reader import CSVReader
from .summarizer import Summarizer


class EmailAnalyzer():
    """Analyzes emails."""

    def __init__(self, input_file, summary_length):
        """Initializes analyzer inputs."""
        self.input_file = input_file
        self.summary_length = summary_length

        self.emails = CSVReader(self.input_file).csv_to_dict()

    def process_emails(self):
        """Process the emails one by one."""
        # Step 1: Get email history
        email_history = self.get_email_history()

        # Step 2: Get language, summary, sender info
        processed_emails = []
        for row in email_history:
            history_details = {}
            history_details['original'] = row['original']
            history_details['history_details'] = []
            for reply in row['history']:
                history_row = {}
                history_row['reply'] = reply[0]
                history_row['language'] = self.get_language(reply[0])
                history_row['summary'] = self.get_summary(reply[0])

                # print('\n\nhistory row')
                # print(history_row)
                history_details['history_details'].append(history_row)

            processed_emails.append(history_details)

        print('\n\n')
        print(processed_emails)
        return processed_emails

    def get_language(self, message):
        """Detect message language.

        :param message string Email body
        :returns: msg_language Language of the message
        :rtype: string
        """
        message_blob = TextBlob(message)
        return message_blob.detect_language()

    def get_summary(self, message):
        """Return message summary."""
        summary = Summarizer(message, 1).main()

        return summary

    def get_email_history(self):
        """Extract the email text relevant for analysis.

        :param email_body string Email content
        :param subject string Email subject
        :returns: email_history List of email history
        :rtype: List
        """
        email_history = []

        for row in self.emails:
            email_row = {}
            email_row['original'] = row['body']
            email_text_list = self.extract_replies(row['body'],
                                                   row['sender_name'],
                                                   row['subject'])
            email_row['history'] = email_text_list
            email_history.append(email_row)

        # List of lists per row
        return email_history

    def extract_replies(self, email_body, sender_name, subject):
        """Extract the email text relevant for analysis.

        :param email_body string Email content
        :param subject string Email subject
        :returns: email_history List of email history
        :rtype: List
        """
        # Clean subject - Remove [RE:, FW:]
        clean_subject = subject if ':' not in subject else subject.rsplit(':', 1)[1]
        pattern = r"From.*Subject.*" + clean_subject
        email_history = re.split(pattern, email_body)

        # Generate list of list of email history
        hislist = [x.split(',') for x in email_history]

        # Remove the signature
        updated_list = self.remove_signature(hislist, sender_name)
        return updated_list

    def remove_signature(self, email_history, sender_name):
        """Remove the signature from each email reply.

        :param email_history list List of email replies
        :param sender_name string Sender's name
        :returns: Email history without signature
        :rtype: list
        """
        # TODO
        return email_history
