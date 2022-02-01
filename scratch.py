# Digital journal + Cloud Vision Scratch
# 1/31/2022

import pandas as pd
import pydata_google_auth
from google.cloud import storage
from google.cloud import vision
from google.cloud import bigquery


# Set up GCP cred authentication.
creds = pydata_google_auth.get_user_credentials(
    ['https://www.googleapis.com/auth/cloud-platform']
)

client = bigquery.Client(project='digital-journal-340001',credentials=creds)
q = """
SELECT * FROM `digital-journal-340001.test.test`
"""

df = (
    client.query(q)
    .result()
    .to_dataframe()
)
