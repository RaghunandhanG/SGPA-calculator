#live

import streamlit as st 
from script_functions import *
import os

st.title('SGPA CALCULATOR')


        
        
uploaded_file = upload_file()
file_path = os.path.join("uploads", uploaded_file.name)
upload_file_in_db(uploaded_file , file_path)


#________________________________________________________________________________________________________________________________________________________



import requests

files = [
    ('file', ('file', open(file_path, 'rb'), 'application/octet-stream'))
]
headers = {
    'x-api-key': 'sec_oUkQRqJrDyygEOTTEMmjnCMCWWaJY0Wz'
}

response = requests.post(
    'https://api.chatpdf.com/v1/sources/add-file', headers=headers, files=files)

if response.status_code == 200:
    print('Source ID:', response.json()['sourceId'])
else:
    print('Status:', response.status_code)
    print('Error:', response.text)
sourceID = response.json()['sourceId']




#________________________________________________________________________________________________________________________________________________________



import requests

headers = {
    'x-api-key': 'sec_oUkQRqJrDyygEOTTEMmjnCMCWWaJY0Wz',
    "Content-Type": "application/json",
}

data = {
    'sourceId': sourceID,
    'messages': [
        {
            'role': "user",
            'content': "What are the credits of the subjects. Give them in list closed by square brackets",
        }
    ]
}

response = requests.post(
    'https://api.chatpdf.com/v1/chats/message', headers=headers, json=data)

if response.status_code == 200:
    print('Result:', response.json()['content'])
else:
    print('Status:', response.status_code)
    print('Error:', response.text)
credits_list = response.json()['content']



#________________________________________________________________________________________________________________________________________________________



credit_list = eval(f'{extract(credits_list)}')

#________________________________________________________________________________________________________________________________________________________




import requests

headers = {
    'x-api-key': 'sec_oUkQRqJrDyygEOTTEMmjnCMCWWaJY0Wz',
    "Content-Type": "application/json",
}

data = {
    'sourceId': sourceID,
    'messages': [
        {
            'role': "user",
            'content': "Extract the Grade in the file in a format like python list",
        }
    ]
}

response = requests.post(
    'https://api.chatpdf.com/v1/chats/message', headers=headers, json=data)

if response.status_code == 200:
    print('Result:', response.json()['content'])
else:
    print('Status:', response.status_code)
    print('Error:', response.text)
grade_list = response.json()['content']




#________________________________________________________________________________________________________________________________________________________




grade_list = eval(f'{extract(grade_list)}')


#________________________________________________________________________________________________________________________________________________________




dct = {'B':6, 'O':10, 'A':8, 'A+':9,'B+':7}




#________________________________________________________________________________________________________________________________________________________





grade_list = [dct[i] for i in grade_list if i in dct]



#________________________________________________________________________________________________________________________________________________________




sum = 0
total_credits = 0
for i in range(len(credit_list)):
  sum += credit_list[i] * grade_list[i]
  total_credits += credit_list[i]

st.write(f'The SGPA is {round(sum / total_credits , 2)}')
