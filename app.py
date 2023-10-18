import os
import openai
from PIL import Image
import streamlit as st
openai.api_key = os.environ.get('OpenAI_API_Key')

st.set_page_config(
    page_title="ChatGPT + DALL-E 2",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="auto",
)

@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def openai_completion(prompt):
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      max_tokens=150,
      temperature=0.5
    )
    return response['choices'][0]['text']

@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def openai_image(prompt):
    response = openai.Image.create(
      prompt=prompt,
      n=1,
      size="256x256"
    )
    return response['data'][0]['url']

top_image = Image.open('static/banner_top.png')
bottom_image = Image.open('static/banner_bottom.png')
main_image = Image.open('static/main_banner.png')

st.sidebar.image(top_image,use_column_width='auto')
format_type = st.sidebar.selectbox('Choose your OpenAI magician 😉',["ChatGPT","DALL-E 2"])
st.sidebar.image(bottom_image,use_column_width='auto')

st.image(main_image,use_column_width='auto')
st.title("📄 ChatGPT + DALL-E 🏜 Streamlit")

if format_type == "ChatGPT":
    input_text = st.text_area("Please enter text here... 🙋",height=50)
    chat_button = st.button("Do the Magic! ✨")

    if chat_button and input_text.strip() != "":
        with st.spinner("Loading...💫"):
            openai_answer = openai_completion(input_text)
            st.success(openai_answer)
    else:
        st.warning("Please enter something! ⚠")

else:
    input_text = st.text_area("Please enter text here... 🙋",height=50)
    image_button = st.button("Generate Image 🚀")

    if image_button and input_text.strip() != "":
        with st.spinner("Loading...💫"):
            image_url = openai_image(input_text)
            st.image(image_url, caption='Generated by OpenAI')
    else:
        st.warning("Please enter something! ⚠")

st.markdown("<br><hr><center>Made with ❤️ by <a href='mailto:ralhanprateek@gmail.com?subject=ChatGPT + DALL-E WebApp!&body=Please specify the issue you are facing with the app.'><strong>Prateek Ralhan</strong></a></center><hr>", unsafe_allow_html=True)
st.markdown("<style> footer {visibility: hidden;} </style>", unsafe_allow_html=True)
