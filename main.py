# Get text from a notebook photo and save processed results as a json file
# in GCS- Cloud Function edition.

import pandas as pd
import os

from google.cloud import storage
from google.cloud import vision
from datetime import datetime as dt


# Manage credentials based on execution location.
if os.envrion.get('GCP_PROJECT') is not None:
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/clairethomison/creds/djcr.json"

