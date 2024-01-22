import pytesseract
import os
from PIL import Image
import json
import requests
from pypdf import PdfReader
from pdf2image import convert_from_path
import numpy as np

# Function to extract text with OCR
def ocr_image_to_text(image_path):
    # Specify the path to tesseract executable if it's not in the PATH
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\RushabhDedhia\AppData\Roaming\Python\Python310\site-packages\pytesseract\tesseract.exe'  # Update the path as necessary
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text


def image_pdf_to_text(pdf_file):
    path_to_poppler_exe = r'C:\path\to\poppler\poppler-21.03.0\bin\poppler.exe'
    pdf_pages = convert_from_path(pdf_file, 500, poppler_path=path_to_poppler_exe)
    # Iterate through all the pages stored above
    for page in pdf_pages:
           
           img1 = np.array(page)
           text += pytesseract.image_to_string(img1)
    return text


def get_pdf_text(pdf_doc):
    text = ""
    pdf_reader = PdfReader(pdf_doc)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

#extacted_text = ocr_image_to_text("C:\\Users\\RushabhDedhia\\AppData\\Roaming\\Python\\Python310\\Scripts\\ABM ENTERPRISES 4.jpg")

def mistral_chat_completion(prompt):
    # API endpoint and token from your provided file
    api_endpoint = "https://api.mistral.ai/v1/chat/completions"
    token = "YOUR_TOKEN"  # Replace with your actual token

    # Headers and payload for the POST request
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    payload = {
        "model": "mistral-tiny",  # Replace with your desired model
        "messages": [{"role": "user", "content": prompt}]
    }

    # Making the POST request
    response = requests.post(api_endpoint, json=payload, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}"


