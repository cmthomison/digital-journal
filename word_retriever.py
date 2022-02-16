# Get text from a notebook photo and save processed results as a json file
# in GCS.

from cgi import print_environ
import pandas as pd
import os

from google.cloud import storage
from google.cloud import vision
from datetime import datetime as dt
import json


class NbPage:
    """Class to manage notebook scan data, convert contents to text, and load
    the resulting content to GCS.
    """

    def __init__(self, uri):
        self.uri = uri
    
    def get_text(self):
        """Detects and returns text from images in GCS using Cloud
        Vision API.

        Args:
            uri (string): location of image file
        """
        
        client = vision.ImageAnnotatorClient()
        image = vision.Image()
        image.source.image_uri = self.uri

        response = client.text_detection(image=image)
        texts = response.text_annotations

        # Format response.
        summary = {
            "file": self.uri,
            "content": texts[0].description,
            "processing_date": dt.today()
        }

        return summary
    
    def load_result(self, summary):
        """Load summary file to GCS.
        """

        # Set up the client and bucket reference.
        client = storage.Client(project='digital-journal-340001')
        bucket_name = 'notebook-text'
        BUCKET = client.get_bucket(bucket_name)

        # Derive json file name from image name.
        filename = self.uri.split('/')[-1:][0].split('.')[0]

        # Create and upload the blob.
        blob = BUCKET.blob(filename)

        blob.upload_from_string(
            data=json.dumps(summary),
            content_type='application/json'
        )

        print(f'{filename} upload copmlete to {bucket_name}.')