import streamlit as st
import os
from openai import OpenAI
from huggingface_hub import InferenceClient

st.set_page_config(page_title="AI Chat & Question & Answering  App")


hf_client = InferenceClient(api_key=st.secrets.get("HF_TOKEN"))


st.header("Chatbot")
openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

if not openai_api_key:
    st.info("For activate please add your OpenAI API key to the sidebar to use the chatbot.")
else:
    client = OpenAI(api_key=openai_api_key)
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Type Your Question ?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                stream=True,
            )
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})

st.divider()


st.header("AI Question Answering")

context = st.text_area("Enter Context", height=250)
question = st.text_input("Ask a question about the context")

if st.button("Get Answer"):
    if context and question:
        with st.spinner("Asking AI..."):
            try:

                result = hf_client.question_answering(
                    model="timpal0l/mdeberta-v3-base-squad2",
                    question=question,
                    context=context
                )
                st.success(f"Answer: {result.answer}")
                st.metric("Confidence Score", round(result["score"], 3))
            except Exception as e:
                st.error(f"Error: {e}. (Make sure your HF_TOKEN is valid)")
    else:
        st.warning("Please provide both context and a question.")

st.divider()
st.markdown("Powered by C-Clarke Institute students")
