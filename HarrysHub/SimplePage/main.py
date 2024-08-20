import streamlit as st
from PIL import Image

st.header("Harry's Hub", divider="rainbow" )
st.subheader("All of my current tools.")
st.markdown("All tools up-to-date")

st.link_button("Percentage Calculator", "https://percentagecalculator.streamlit.app/")
st.link_button("Binary Convertor", "https://binaryconvertor.streamlit.app")
st.link_button("ASCII Convertor", "https://asciiconvertor.streamlit.app")

st.subheader("All of my current games.")
st.markdown("All games up-to-date.")

st.link_button("Number Guesser", "https://numberguesser.streamlit.app")
