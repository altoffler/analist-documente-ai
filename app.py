import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

st.set_page_config(page_title="Index Oficial - Asistent AI", page_icon="⚖️", layout="centered")

st.title("⚖️ Analist AI Documente Oficiale")
st.markdown("---")

with st.sidebar:
    st.write("### Configurare")
    api_key = st.text_input("Cheie API Google (Gemini)", type="password")
    st.info("Obține cheia de pe ://google.com")

tip_doc = st.selectbox(
    "Alege categoria documentului pentru o analiză precisă:",
    [
        "Legislație & Taxe (ANAF, Impozite, Notificări)",
        "Subvenții & Fonduri (APIA, AFIR, Start-up Nation)",
        "Administrativ (Poliție, Primărie, Ministere)",
        "Validare Formulare & Modele (Verificare completare)"
    ]
)

uploaded_file = st.file_uploader("Încărcați documentul (Imagine PNG/JPG)", type=['png', 'jpg', 'jpeg'])

if uploaded_file and api_key:
    if st.button("Descifrează Documentul"):
        try:
            genai.configure(api_key=api_key)
            
            # Folosim versiunea cea mai stabilă care rezolvă eroarea v1beta
            model = genai.GenerativeModel('gemini-1.5-flash-latest')
            
            img = Image.open(uploaded_file)
            
            with st.spinner("Analizăm documentul conform legislației din România..."):
                prompt = f"Ești un expert juridic și administrativ în România. Analizează această imagine de tip '{tip_doc}' și oferă un raport detaliat: ce este documentul, termene limită, sume de plată și pașii legali de urmat."
                
                response = model.generate_content([prompt, img])
                
                st.success("Analiză Finalizată!")
                st.markdown(response.text)
                
        except Exception as e:
            st.error(f"Eroare: {e}. Asigură-te că API Key-ul este corect.")

st.markdown("---")
st.caption("© IndexOficial.ro")
