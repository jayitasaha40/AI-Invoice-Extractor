import boto3
import fitz
import os
 
 
def is_pdf_file(filename):
    return filename.lower().endswith('.pdf')
 
def extract(input_file):
    
 
    text = ""
 
    client = boto3.client('textract',region_name='ca-central-1', aws_access_key_id='ASIA37NKDWJ23JMHUKOU', aws_secret_access_key='055XVdaCVvdRy19FTZAfyqwuyfWWgxAi0nao5dTJ', aws_session_token='IQoJb3JpZ2luX2VjEHYaDGNhLWNlbnRyYWwtMSJHMEUCIQDyNvpPNIbZn/AHFHa4WEJ9z+hVYeuRY01TVTYiPu3G2AIgCzf8vdtPI4b2+S8e6fQ1ba8+xBIF6x/Jha4o1gwa30cqiwMIQBADGgw4MjMzNzk4NjYyMjkiDPMSHRlz+L/boL3+LCroAqy0JgrKWA14LW9kYcd3QULGFObiH1cdFdbyQ+xuPn8TRNbpyrNnjaC3EwxiMZqa2qLejpkSoKarlHlzIz7HsIAWYB7zV8fNz8/+DX3YN1z78+0qG8DdP6sFBsNZwJKq/vkCZ3ltmgU5ClklNwa2ugSofPNQFRyYnR3gdmCzKyeQhYzpqxebsGimofqOcvVUEBDj5e3hftA0jC/HpP1JK+Ml44pWhByIulj0x2a3p2I68PKvPQ/alEjIn+2iTJ1hgRWA9i+dkyF98rOJg84IsjvS4UNGYOfFIXRRomKdOceZj3avrbQlrBijOHPySIa9Tc33bZ9U57hnzGwTrBsxm7tI45uV1/dGd54gsj4u5zdWYTkBxcWz8clbgeHmykmWEXWRA+lNZEf0720o7u3Aa6/2f0xZLcpNTADSJL65sZrpog/CUppfNbUHr154EfkpYR656MvonHE8+SMF2DEsB4VqJavSBKOCOzCz9OytBjqmAcIrPgja/fBfJ036kQ+Fjxz0ArRei18tntgguBz/on32h0eGbQX9WhkIvo/qGuWAGRj76JEHQEQjjPholKoK6rmuI4dYdWLbOyf5NUZhK9ja/lBaErwtJbalnrEoK2nzdLJijesCcOISZHiSEmcsHg4hJtSs/UbUGhK7cLUTok+G7tzV9gFqPRchtza+Q+7R1bTtCe6pGmrqR5geaBbrao8OsHd6cyM=')
 
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
 
 
 