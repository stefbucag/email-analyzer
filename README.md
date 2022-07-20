# Email Analyzer Project Details

## Overview:
Extract all historic emails from email body received, conduct early analyses on text, then finish with machine learning model

### Technical requirement:
Please use Python 3.x

### **Step 1: Segment email history into list of texts**
The input is a CSV file containing anonymized emails, with the key column called “Body”. The challenge is that one email will contain all historic emails in its body, in case the original email was replied to or forwarded. Unfortunately, each time an email is replied to / forwarded, this create dummy text (From: To: Re:  as well as legal texts or person signatures). The task is to be able to extract the email text only and discard the other text passages that aren’t relevant for analysis. Given 1 email as input (from the CSV file), the program should break out the emails in the history and reply with an array of strings (list of strings)

**Note:**
  1. The CSV contains other fields, most of which should be self-explanatory (sender, To, CC, etc.). Clean Body contains a version of the body text which has gone through a “stemmer”. “Last email” contains an attempt to single out only the last email. All further fields are categorization fields and can be disregarded
  
  2. To create a valid comma-separated file, all commas in the text have been replaced with underscore (_). To have the original email body, simply replace _ with , and this should provide a close version of the original version

### **Step 2: Conduct some early meta-analysis on the email text**
Using the list of historic emails achieved in step 1, conduct “easy” analyses on the text:
- Identify text language
- Extract n summary sentences (n = 2 in general, but make it configurable)

Finally, also extract meta-information about sender and send date of the email (not necessarily in the text)

**Note:** It is important that all computations be done locally (for data security reasons). E.g. it is not allowed to use Python libraries which use Google Translate services in the back-end to identify the language, as this would mean sharing the data with Google servers

### Step 3: Train machine learning model to measure emotions
Using only the extracted text (and potentially subject if this is the original email), create 1-multiple machine learning models that are able to measure emotions. For example:
  - Contempt vs. esteem
  - Surprise vs. predictability
  - Anger vs. calm


### Installation
1. Clone repository
    ```
    $ git clone
    $ cd email-analyzer
    ```
2. Install virtualenvironment
    ```
    $ virtualenv .virtualenv
    ```
3. Activate virtual environment and install requirements
    ```
    $ pip install -r requirements.txt
    ```
4. Lastly,
    ```
    python setup.py develop
    ```

### To use the Email Analyzer script
- Activate virtual environment and run command:
    ```
    python -m src.email_analyzer.main [location-of-the-csv-input]
    ```
