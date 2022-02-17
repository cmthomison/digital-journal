# Digital Journal Project
Experimenting with Google's Cloud Vision API for OCR on photos of my notebook pages

February 2022

## Background
I'm currently working through a course series on Coursera to prepare for the Google Machine Learning Engineer certification exam and learned about Cloud Vision API and several other pre-trained machine learning models available within Google Cloud Platform (GCP).

For both work and personal projects, I'm constantly switching between digital notes and handwritten notes in notebooks. I decided to use this as an opportunity to test out Cloud Vision API to convert my handwritten notes to text.

## Tools
I'm not generating hundreds of pages of notes each day, so I don't necessarily need a fully automated solution at this point, but I do want note processing to be simple and not require me to run a script each time.

The flow currently uses two key tools in GCP: <b>Cloud Functions</b> and <b>Cloud Storage</b>. 

<b>Cloud Functions</b> are serverless functions in GCP. I find them particularly handy because they can be written in Python (amongst other languages) and they are simple to deploy and trigger. <b>Google Cloud Storage (GCS)</b> is GCP's web storage service that is a great place to stash files and data in a place that is accessible, yet distinct from compute resources.

To process images, I add them to a Cloud Storage bucket. The creation of an object within the bucket triggers the Cloud Function to run, which generates a Cloud Vision API client, detects text, and returns the text response. This response is then formatted and loaded to a different GCS bucket along with the name of the file and the processing date.

## Next Steps