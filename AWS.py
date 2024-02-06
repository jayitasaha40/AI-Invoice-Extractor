import boto3
import fitz
import os
 
def load_config(file_path="config.yaml"):
    with open(file_path, "r") as file:
        config = yaml.safe_load(file)
    return config


def is_pdf_file(filename):
    return filename.lower().endswith('.pdf')
 
def extract(input_file):
    config = load_config()
 
    text = ""
 
    client = boto3.client('textract',region_name='ca-central-1', aws_access_key_id=config["AWS"]["aws_access_key_id"], aws_secret_access_key= config["AWS"]["aws_secret_access_key"], aws_session_token= config["AWS"]["aws_session_token"]) 
 
    if is_pdf_file(input_file):
 
        pdf_document = fitz.open(input_file)
        file_name = input_file.split('.')[0]
 
 
        for page_number in range(pdf_document.page_count):
            page = pdf_document.load_page(page_number)
            image = page.get_pixmap()
            image.save(f'{file_name}{page_number}.jpg', 'JPEG')
 
        no_of_pages = pdf_document.page_count
        pdf_document.close()
    else:
 
        no_of_pages = 1
        file_name = input_file.split('.')[0]
 
    # Process each page/image
    for i in range(no_of_pages):
        if is_pdf_file(input_file):
            with open(f'{file_name}{i}.jpg', 'rb') as image:
                img = bytearray(image.read())
        else:
            with open(input_file, 'rb') as image:
                img = bytearray(image.read())
 
        response = client.detect_document_text(Document={'Bytes': img})
 
        text += f"\nPage {i + 1}\n"
        for item in response["Blocks"]:
            if item["BlockType"] == "LINE":
                text += item["Text"] + "\n "
 
    return text
    with open('RawText.txt', 'w') as file:
        file.write(text)
    # with open(input_file, 'rb') as file:
    #     img = bytearray(file.read())
 
    # response = client.detect_document_text(Document={'Bytes': img})
 
    # for item in response["Blocks"]:
    #     if item["BlockType"] == "LINE":
    #         text += item["Text"] + "\n"
    # print(text)
    # return text
 
# Example usage:
 
 
 