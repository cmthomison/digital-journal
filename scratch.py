# Digital journal + Cloud Vision Scratch
# 1/31/2022

import pandas as pd
import pydata_google_auth
from google.cloud import storage
from google.cloud import vision
from google.cloud import bigquery

# Temporarily manage credentials.
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/clairethomison/creds/djcr.json"

# Modified function to detect text from GCP examples.
# https://cloud.google.com/vision/docs/ocr#vision_text_detection-python
def detect_text_uri(uri):
    """
    Detects text in the file located in Google Cloud Storage or on the Web.
    """

    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    
    return texts

def get_text(uri):
    """Detects and returns text from images in GCS using Cloud
    Vision API.

    Args:
        uri (string): location of image file
    """
    
    client = vision.ImageAnnotationClient()
    image = vision.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations

    vertices = (['({},{})'.format(vertex.x, vertex.y)
            for vertex in text.bounding_poly.vertices])

    {'description': text.description,}

    note = {'uri': uri,
            'content': [
                {}
            ]}


# Set up GCP cred authentication.
creds = pydata_google_auth.get_user_credentials(
    ['https://www.googleapis.com/auth/cloud-platform']
)

# Get list of images in GCS bucket.







# BQ Scratch
client = bigquery.Client(project='digital-journal-340001',credentials=creds)
q = """
SELECT * FROM `digital-journal-340001.test.test`
"""

df = (
    client.query(q)
    .result()
    .to_dataframe()
)
