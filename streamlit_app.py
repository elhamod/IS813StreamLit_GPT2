import streamlit as st
from transformers import pipeline

st.title("My Super Awesome GPT!")

generator = pipeline('text-generation', model='gpt2')

prompt = st.text_input("What is your prompt today?", "Damascus is")
max_token = st.text_input("What's max number of tokens?", 20)

output = generator(prompt, max_length=int(max_token), num_return_sequences=1, truncation=True, temperature=0.1)[0]

st.write(
    "Predictable response: " + output["generated_text"]
)

output = generator(prompt, max_length=max_token, num_return_sequences=1, truncation=True, temperature=1.5)[0]

st.write(
    "Creative response: " + output["generated_text"]
)

