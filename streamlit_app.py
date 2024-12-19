import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="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")
import time
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

# Set your OpenAI API key

# Function to call the OpenAI ChatCompletion API with retries
def get_chat_completion(user_message):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_message},
    ]
    model = "gpt-3.5-turbo"

    for attempt in range(5):  # Retry up to 5 times
        try:
            logging.info("Attempting to call OpenAI API (Attempt %d)", attempt + 1)
            response = client.chat.completions.create(model=model,
            messages=messages)
            logging.info("API call successful!")
            return response.choices[0].message.content
        except Exception as e:
            if "Rate limit exceeded" in str(e):
                logging.warning("Rate limit exceeded. Retrying in %d seconds...", 2 ** attempt)
                time.sleep(2 ** attempt)  # Exponential backoff
            elif "Invalid API key" in str(e):
                logging.error("Authentication error: Invalid API key.")
                return "Error: Invalid API key."
            else:
                logging.error("An unexpected error occurred: %s", str(e))
                return f"An unexpected error occurred: {str(e)}"
    return "Failed to get a response from the OpenAI API after multiple attempts."

# Streamlit app
def main():
    st.title("Chat with OpenAI")
    st.write("Type a message below to interact with OpenAI's GPT API.")
    

    # Input box for user message
    user_message = st.text_input("Your message:", value="")

    # Submit button
    if st.button("Send"):
        if user_message.strip():
            with st.spinner("Connecting to OpenAI..."):
                response = get_chat_completion(user_message)
            st.text_area("Response from OpenAI:", response, height=200)
        else:
            st.warning("Please enter a message before submitting.")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("Written by Hanif Muhammad Rifqi")
if __name__ == "__main__":
    main()
