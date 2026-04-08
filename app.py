import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="Index Oficial - Asistent AI", page_icon="⚖️")

st.title("⚖️ Analist AI Documente Oficiale")
st.markdown("---")

with st.sidebar:
    st.write("### Configurare")
    api_key = st.text_input("Cheie API Google", type="password")

tip_doc = st.selectbox(
    "Categoria documentului:",
    ["Legislație & Taxe", "Subvenții & Fonduri", "Administrativ", "Validare Formulare"]
)

uploaded_file = st.file_uploader("Încarcă imaginea documentului", type=['png', 'jpg', 'jpeg'])

if uploaded_file and api_key:
    if st.button("Descifrează Documentul"):
        try:
            genai.configure(api_key=api_key)
            
            # Schimbăm pe modelul PRO care are rute de acces mai stabile
            model = genai.GenerativeModel('gemini-1.5-pro')
            
            img = Image.open(uploaded_file)
            
            with st.spinner("Analizăm..."):
                prompt = f"Ești expert juridic în România. Analizează această imagine (tip: {tip_doc}) și extrage: 1. Ce este documentul, 2. Termene limită, 3. Sume, 4. Pașii de urmat."
                
                # Forțăm cererea fără a specifica versiunea, lăsăm biblioteca să decidă
                response = model.generate_content([prompt, img])
                
                st.success("Analiză Finalizată!")
                st.markdown(response.text)
                
        except Exception as e:
            st.error(f"Eroare: {e}")
            st.info("Dacă eroarea persistă, verifică dacă ai creat cheia API în 'Google AI Studio' și nu în 'Google Cloud Console'.")

st.markdown("---")
st.caption("© IndexOficial.ro")

