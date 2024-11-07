import streamlit as st 
from langchain_community.llms import OpenAI

st.title('🍎🍐🍊 나의 AI Chat 🥝🍅🍆')

openai_api_key = st.sidebar.text_input('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')

def generate_response(input_text):
    llm = OpenAI(temperatur=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))
    
with st.form('my_form'):
    text = st.text_area('Enter text:', '무엇을 도와드릴까요?')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.starswith('sk-'):
        st.warning('OpenAI API 인증키를 입력해 주세요!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)