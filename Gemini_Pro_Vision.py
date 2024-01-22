"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

from pathlib import Path
import google.generativeai as genai

genai.configure(api_key="") #Provide your API Key

# Set up the model
generation_config = {
  "temperature": 0,
  "top_p": 1,
  "top_k": 32,
  "max_output_tokens": 4096,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-pro-vision",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# Validate that an image is present
# if not (img := Path("ABM ENTERPRISES 4.jpg")).exists():
#   raise FileNotFoundError(f"Could not find image: {img}")





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