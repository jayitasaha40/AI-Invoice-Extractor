import streamlit as st
import os
import json
from Gemini_Pro_Vision import get_response
from Mixtral_8x7b import ocr_image_to_text,mistral_chat_completion,get_pdf_text,image_pdf_to_text

def save_file(file, save_path):
    full_path = os.path.join(save_path, file.name)
    with open(full_path, "wb") as f:
        f.write(file.getbuffer())
    return full_path



def save_response(response, filename='response.json'):
    with open(filename, 'w') as json_file:
        json.dump(response, json_file)


save_path = "C:\\Users\\JayitaSaha\\Documents\\JAYI\ML\\Rushabh\\Mixtral"
st.set_page_config(page_title="Invoice Extractor")
st.title("Invoice Extractor...💁 ")
st.subheader("I can help you in extracting invoice data")
# Upload the Invoices (pdf files)
file = st.file_uploader("Upload invoices here, only PDF files allowed", type=["pdf","jpg"],accept_multiple_files=False)
user_prompt= st.text_input("Please enter your prompt here")
models = ["Mixtral 8*7b", "Gemini Pro"]
selected_model = st.radio("Select an option:", models)
submit=st.button("Extract Data")
if submit:
    if selected_model == "Gemini Pro":
        with st.spinner('Wait for it...'):
         file_path = save_file(file, save_path)
         response = get_response(file_path,user_prompt)
         st.write("Result:", response)
         
         #df = pd.DataFrame(response)

    else:
       with st.spinner('Wait for it...'):
        file_type = file.type.split('/')[1] if file.type else None
        if file_type == "jpg" or file_type == "jpeg":
           text = ocr_image_to_text(file)
        else:
           try:
            text = get_pdf_text(file)  #text pdf
           except:
              #If image pdf
            text = image_pdf_to_text(file)
           finally:
            prompt = user_prompt + text 
            response = mistral_chat_completion(prompt)
            st.write("Result:", response)
            save_file(file, save_path)
        #df = pd.DataFrame(response)

    

        
st.success("Hope I was able to save your time❤️")