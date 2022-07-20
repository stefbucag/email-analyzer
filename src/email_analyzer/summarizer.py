"""Summarizes the given message or text."""
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize
from heapq import nlargest
from string import punctuation
from collections import defaultdict


class Summarizer(object):
    """Summarizes given message depending on the configured length."""

    def __init__(self, message, summary_length):
        """Initializes needed params

        :params message string Message to be summarized
        :params summary_length int Number of sentences in the summary.
        """
        self.message = message
        self.summary_length = summary_length

    def sanitize_msg(self):
        """Performs clean-up and formatting."""
        # TODO: change formatting
        replace = {
            ord('\f'): ' ',
            ord('\t'): ' ',
            ord('\n'): ' ',
            ord('\r'): None
        }

        self.message.translate(replace)

    def tokenize_msg(self):
        """Split message into words."""
        stop_words = set(stopwords.words('english') + list(punctuation))
        words = word_tokenize(self.message.lower())

        # sent_tokenize
        return [
            sent_tokenize(self.message),
            [word for word in words if word not in stop_words]
        ]

    def score_tokens(self, word_tokens, sentence_tokens):
        """
        Counts the occurence of each word in the messsage
        and score sentences based on word count.
        """
        word_frequency = FreqDist(word_tokens)
        ranking = defaultdict(int)

        for i, sentence in enumerate(sentence_tokens):
            for word in word_tokenize(sentence.lower()):
                if word in word_frequency:
                    ranking[i] += word_frequency[word]

        return ranking

    def summarize(self, sentence_ranks, sentence_tokens):
        """
        Utilizes a ranking map produced by score_token to extract
        the highest ranking sentences in order after converting from
        array to string.  
        """
        # Checks length of sentence to 
        # TODO: how do we deal when length is less than configured summary length
        if self.summary_length > len(sentence_tokens):
            print("ERROR: Requested summary length is greater than sentence length")
            exit()

        indexes = nlargest(self.summary_length, sentence_ranks,
                           key=sentence_ranks.get)
        final_sentences = [sentence_tokens[j] for j in sorted(indexes)]

        return ' '.join(final_sentences) 

    def main(self):
        """Main method for Summarizer class"""
        self.sanitize_msg()

        sentence_tokens, word_tokens = self.tokenize_msg()
        sentence_ranks = self.score_tokens(word_tokens, sentence_tokens)

        summary = self.summarize(sentence_ranks, sentence_tokens)
        return summary
