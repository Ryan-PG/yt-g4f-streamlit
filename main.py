from openai import OpenAI
import streamlit as st


models_list = [
  "gpt-3.5-turbo",
  "gpt-4",
  "gpt-4o",
]
select_box = st.selectbox("Select Model", models_list, index=2)

prompt_input = st.text_input("Prompt")
button = st.button("Send")

if button and prompt_input != "":
  client = OpenAI(
    api_key="NO_NEED_TO_API_KEY",
    base_url="http://localhost:1337/v1",
  )

  response = client.chat.completions.create(
    model=select_box,
    messages=[
      {
        "role": "user",
        "content": prompt_input,
      }
    ]
  )

  st.markdown(response.choices[0].message.content)

