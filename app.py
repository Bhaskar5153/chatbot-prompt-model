# app.py

import streamlit as st
import requests

FASTAPI_URL = "http://localhost:8080/ask"  # Update if deployed

st.set_page_config(page_title="Khazipur TaxBot", layout="centered")

st.title("📊 Khazipur TaxBot")
st.write("Ask questions about the Khazipur DCB tax dataset.")

# Input box
user_question = st.text_input("Enter your question:")

if st.button("Ask"):
    if not user_question.strip():
        st.warning("Please enter a valid question.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    FASTAPI_URL,
                    json={"question": user_question}
                )
                if response.status_code == 200:
                    answer = response.json().get("answer", "")
                    st.success("✅ Answer:")
                    st.write(answer)
                else:
                    st.error(f"API Error: {response.text}")
            except Exception as e:
                st.error(f"Connection error: {e}")
