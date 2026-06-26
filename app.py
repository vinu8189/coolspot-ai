import streamlit as st
from agent.coolspot_agent import run_agent

st.set_page_config(page_title="CoolSpot AI", page_icon="🌍")

st.title("🌍 CoolSpot AI")
st.subheader("Find cool indoor places during heatwaves")

query = st.text_input("Tell me your situation (city, heat, kids, etc.)")

if st.button("Find places"):
    if query.strip():
        with st.spinner("Thinking..."):
            result = run_agent(query)
        st.write(result)