import yaml
import pytesseract
import os
from PIL import Image
import json
import requests
from pypdf import PdfReader
from pdf2image import convert_from_path
import numpy as np

#Load Config
def load_config(file_path="config.yaml"):
    with open(file_path, "r") as file:
        config = yaml.safe_load(file)
    return config

config = load_config()

# Function to extract text with OCR
def ocr_image_to_text(image_path):
    # Specify the path to tesseract executable from the config file
    pytesseract.pytesseract.tesseract_cmd = config["tesseract"]["tesseract_cmd"]
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text


def image_pdf_to_text(pdf_file):
    # Get the path to Poppler executable from the config file
    path_to_poppler_exe = config["poppler"]["path"]
    pdf_pages = convert_from_path(pdf_file, 500, poppler_path=path_to_poppler_exe)
    text = ""
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
    # Use Mistral configurations from the config file
    api_endpoint = config["mistral"]["api_endpoint"]
    token = config["mistral"]["token"]

    # Headers and payload for the POST request
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    payload = {
        "model": config["mistral"]["model"],
        "messages": [{"role": "user", "content": prompt}]
    }

    # Making the POST request
    response = requests.post(api_endpoint, json=payload, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}"
    
print(config["mistral"]["token"])


