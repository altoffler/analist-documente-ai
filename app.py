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
            # CONFIGURARE CRITICĂ: Forțăm utilizarea versiunii stabile v1
            # Acest lucru elimină eroarea 404 v1beta
            genai.configure(api_key=api_key, transport='rest')
            
            # Folosim modelul Flash care este cel mai rapid și stabil pentru conturile free
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            img = Image.open(uploaded_file)
            
            with st.spinner("Analizăm documentul conform legislației din România..."):
                prompt = f"Ești un expert juridic în România. Analizează această imagine (tip: {tip_doc}) și extrage sub formă de listă: 1. Ce este documentul, 2. Termene de plată sau contestație, 3. Sume de plată/încasat, 4. Pașii legali imediați."
                
                response = model.generate_content([prompt, img])
                
                st.success("Analiză Finalizată!")
                st.markdown(response.text)
                
        except Exception as e:
            st.error(f"Eroare: {e}")
            st.info("Verifică dacă ai creat cheia API în 'Google AI Studio'.")

st.markdown("---")
st.caption("© IndexOficial.ro")
