import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="Official Index - AI Assistant", page_icon="⚖️")

st.title("⚖️ AI Analyst Official Documents")
st.markdown("---")

with st.sidebar:
    st.write("### Configuration")
    api_key = st.text_input("Google API Key", type="password")

document_type = st.selectbox(
    "Document Category:",
    ["Legislation & Taxes", "Grants & Funds", "Administrative", "Form Validation"]
)

uploaded_file = st.file_uploader("Upload document image", type=['png', 'jpg', 'jpeg'])

if uploaded_file and api_key:
    if st.button("Decipher Document"):
        try:
            # CRITICAL CONFIGURATION: Force v1 (stable) version to avoid 404 error
            genai.configure(api_key=api_key, transport='rest')
            
            # Use FLASH - it is the most stable for free APIs
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            img = Image.open(uploaded_file)
            
            with st.spinner("Analyzing the document according to Romanian legislation..."):
                prompt = f"You are a legal expert in Romania. Analyze this image (type: {document_type}) and extract as a list: 1. What is the document, 2. Payment or contestation deadlines, 3. Amounts to be paid/collected, 4. Immediate legal steps."
                
                response = model.generate_content([prompt, img])
                
                st.success("Analysis Completed!")
                st.markdown(response.text)
                
        except Exception as e:
            st.error(f"Error: {e}")
            st.info("Check if you have created the API key in 'Google AI Studio'. If you are in the EU, sometimes you need an extra activation step in the console.")

st.markdown("---")
st.caption("© IndexOficial.ro")
