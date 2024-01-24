# AI Invoice Extractor

AI-Invoice-Extractor is a Streamlit web application that utilizes Gemini Pro and Mixtral LLMs to extract information from invoices based on user prompts.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- Pip package manager installed
- Tesseract installed (OCR tool)
- Poppler installed (PDF processing tool)

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/AI-Invoice-Extractor.git
    cd AI-Invoice-Extractor
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Configuration:**

    Update the `config.yaml` file with your Gemini Pro and Mixtral API keys, file paths, and other configurations.

## Running the Application

1. **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

    This command will launch the web application. Open your browser and navigate to [http://localhost:8501](http://localhost:8501) to interact with the app.

2. **Upload your invoice:**

    On the web interface, upload your invoice file.

3. **Provide a prompt:**

    Enter a prompt related to the information you want to extract from the uploaded invoice.

4. **Get Extracted Information:**

    Click the extraction button, and the application will utilize Gemini Pro and Mixtral LLMs to extract information based on your prompt.

## Additional Notes

- If you encounter issues with dependencies, double-check that your Python environment is properly set up, and the necessary tools like Tesseract and Poppler are installed.

- Make sure to replace placeholder values in the `config.yaml` file with your actual API keys, paths, and other configurations.


