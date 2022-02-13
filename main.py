# Get text from a notebook photo and save processed results as a json file
# in GCS- Cloud Function edition.

import pandas as pd
import os

from google.cloud import storage
from google.cloud import vision
from datetime import datetime as dt

from word_retriever import NbPage


# Manage credentials based on execution location.
if os.environ.get('GCP_PROJECT') is not None:
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/clairethomison/creds/djcr.json"

# Cloud Function Entry Point
def img_to_text(event, context):
    """Cloud function triggered on new file in GCS that converts a photo of a 
    notebook page to text.
    """

    print(f'File {event.nane} to be processed.')

    # Initialize NbPage class and get text.
    page = NbPage(event.selfLink)
    text = NbPage.get_text()
    page.load_result(text)

    print(f'File {event.name} converted to text and loaded to GCS.')



