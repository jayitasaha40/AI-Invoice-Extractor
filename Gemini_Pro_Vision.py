"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import yaml
from pathlib import Path
import google.generativeai as genai

def load_config(file_path="config.yaml"):
    with open(file_path, "r") as file:
        config = yaml.safe_load(file)
    return config

def setup_generative_ai_model(config):
    genai.configure(api_key=config["google_generativeai"]["api_key"])
    
    generation_config = config["google_generativeai"]["generation_config"]
    safety_settings = config["google_generativeai"]["safety_settings"]
    
    model_name = config["google_generativeai"]["model_name"]
    
    return genai.GenerativeModel(model_name=model_name,
                                 generation_config=generation_config,
                                 safety_settings=safety_settings)

# Load configuration
config = load_config()

model = setup_generative_ai_model(config)



def get_response(Image_Path,Prompt):
  image_parts = [
    {
      "mime_type": "image/jpeg",
      "data": Path(Image_Path).read_bytes()
    },
  ]

  prompt_parts = [
    image_parts[0],
    Prompt,
    #"\nExtract Invoice Number, Date, Purchaser, Transport, Billed to, Shipped to, GSTIN, All lines of table item, CGST and SGST, and total amount. Give me in proper JSON format. ",
  ]
  response = model.generate_content(prompt_parts)
  return response.text