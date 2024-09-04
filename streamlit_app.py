import streamlit as st

from transformers import pipeline

### Create a GPT2 generator pipeline
generator = pipeline('text-generation', model='gpt2')

prompt = st.text_input("What is your prompt today?", "Damascus is")

### Generate the answer to the question "Damascus is a" 
output = generator(prompt, max_length=20, num_return_sequences=10, truncation=True)[0]

st.title("🎈 My new app")
st.write(
    output["generated_text"]
)
