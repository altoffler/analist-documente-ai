import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

st.set_page_config(page_title="Index Oficial - Asistent AI", page_icon="⚖️", layout="centered")

# Minimalist & Official Design
st.title("⚖️ Analist AI Documente Oficiale")
st.markdown("---")

# Configuration Sidebar
with st.sidebar:
    st.write("### Configurare")
    api_key = st.text_input("Cheie API Google (Gemini)", type="password", help="Obține cheia de pe ://google.com")
    st.info("Datele tale sunt procesate securizat prin Google AI Studio.")

# The 4 Categories
tip_doc = st.selectbox(
    "Alege categoria documentului pentru o analiză precisă:",
    [
        "Legislație & Taxe (ANAF, Impozite, Notificări)",
        "Subvenții & Fonduri (APIA, AFIR, Start-up Nation)",
        "Administrativ (Poliție, Primărie, Ministere)",
        "Validare Formulare & Modele (Verificare completare)"
    ]
)

uploaded_file = st.file_uploader("Încarcă documentul (Imagine PNG/JPG)", type=['png', 'jpg', 'jpeg'])

if uploaded_file:
    if not api_key:
        st.error("Te rugăm să introduci cheia API Gemini în meniul din stânga.")
    else:
        if st.button("Descifrează Documentul"):
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-1.5-flash-latest')
                
                # Image Preparation
                img = Image.open(uploaded_file)
                
                with st.spinner("Analizăm documentul conform legislației române..."):
                    prompts = {
                        "Legislație & Taxe (ANAF, Impozite, Notificări)": "Ești expert fiscal în România. Analizează această imagine și identifică: Sume de plată, Scadențe, Conturi IBAN și Baza Legală.",
                        "Subvenții & Fonduri (APIA, AFIR, Start-up Nation)": "Ești consultant fonduri europene. Analizează imaginea și extrage: Condiții de eligibilitate, Termene de depunere și Documente necesare.",
                        "Administrativ (Poliție, Primărie, Ministere)": "Ești expert în drept administrativ. Analizează imaginea și identifică: Termenul de contestație, Instituția unde se depune și eventuale vicii de formă.",
                        "Validare Formulare & Modele (Verificare completare)": "Ești un asistent administrativ riguros. Verifică dacă toate câmpurile din formular sunt completate și dacă există greșeli vizibile."
                    }
                    
                    response = model.generate_content([prompts[tip_doc], img])
                    
                    st.success("Analiză Finalizată!")
                    st.subheader("📋 Raport de Analiză Senior")
                    st.markdown(response.text)
                    
            except Exception as e:
                st.error(f"A apărut o eroare: {e}")

st.markdown("---")
st.caption("© IndexOficial.ro - Tehnologie AI pentru cetățeni.")
