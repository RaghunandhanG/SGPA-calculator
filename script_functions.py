import streamlit as st
import os


def upload_file():

    uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
    if uploaded_file is not None:
        return uploaded_file 
    else:
        st.write('Waiting for the file....')


def rename_file(file):
    if file is not None:
        os.rename(file.name, "sem_result")
        
        
def upload_file_in_db(uploaded_file,file_path):

    if uploaded_file is not None:
        upload_dir = "uploads"
        os.makedirs(upload_dir, exist_ok=True)  

        # Create the directory if it doesn't exist
        
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        

        # Can be used wherever a "file-like" object is accepted:
        st.success('File uploaded', icon="✅")
        
        
        
        
def extract(text):
  res = []
  start = text.find('[')
  end = text.find(']') +  1
  
  return text[start:end]
