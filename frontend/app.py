import streamlit as st
from PIL import Image
import requests
import json

# Frontend
# page setup boilerplate, tab icon
icon = Image.open('icon.png')
st.set_page_config('See Out Loud', page_icon=icon)

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)


# Streamlit UI
st.title('Your image describer 📷')

my_image = st.file_uploader('insert image here')

if my_image and st.button('Generate Caption'):
    with st.spinner('Wait for it...'):
        st.image(my_image)
        url = "http://backend:8080/uploadfile"

        files = {"image_data": my_image.getvalue()}

        res = requests.post(url=url, files=files)
    st.subheader(f"{res.json().get('Caption')}")
else:
    pass
