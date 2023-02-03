import streamlit as st
import openai

# Authenticate to OpenAI API
openai.api_key = "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"

def summarize_text(text, model, max_length=50):
    completions = openai.Completion.create(
        engine=model,
        prompt=f"Summarize this text for a second standard kid: {text}",
        max_tokens=max_length,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

# Streamlit app
st.title("GPT-3 Text Summarizer for Kids")

text = st.text_area("Enter your text:")

model = "text-ada-001"
summary = ""

if text:
    max_length = len(text.split(" "))
    summary = summarize_text(text, model, max_length=max_length)
    st.write(f"Summary: {summary}")