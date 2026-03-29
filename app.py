import streamlit as st
from agent.ai_agent import AIAgent

agent = AIAgent()

st.set_page_config(page_title="AI Assistant", layout="centered")

st.title("🤖 Agentic AI Research Assistant")

query = st.text_input("Ask your question:")

if st.button("Submit"):
    if query:
        response = agent.process_query(query)
        st.write(response)
