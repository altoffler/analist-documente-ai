import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

st.set_page_config(page_title="Index Oficial - Asistent AI", page_icon="⚖️", layout="centered")

# Design Minimalist & Oficial
st.title("⚖️ Analist AI Documente Oficiale")
st.markdown("---")

# Sidebar pentru Configurare
with st.sidebar:
    st.write("### Configurare")
    api_key = st.text_input("Cheie API Google (Gemini)", type="password", help="Obține cheia de pe ://google.com")
    st.info("Datele tale sunt procesate securizat prin Google AI Studio.")

# Cele 4 Categorii conform IndexOficial.ro
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

if uploaded_file:
    if not api_key:
        st.error("Te rugăm să introduci cheia API Gemini în meniul din stânga.")
    else:
        if st.button("Descifrează Documentul"):
            try:
                genai.configure(api_key=api_key)
                
                # Încercăm varianta stabilă a modelului
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # Pregătire Imagine
                img = Image.open(uploaded_file)
                
                with st.spinner("Analizăm documentul conform legislației române..."):
                    prompts = {
                        "Legislație & Taxe (ANAF, Impozite, Notificări)": "Ești expert fiscal în România. Analizează această imagine și identifică: Sume de plată, Scadențe, Conturi IBAN și Baza Legală.",
                        "Subvenții & Fonduri (APIA, AFIR, Start-up Nation)": "Ești consultant fonduri europene în România. Analizează imaginea și extrage: Condiții de eligibilitate, Termene de depunere și Documente necesare conform ghidurilor oficiale.",
                        "Administrativ (Poliție, Primărie, Ministere)": "Ești expert în drept administrativ românesc. Analizează imaginea și identifică: Termenul de contestație, Instituția unde se depune contestația și eventuale vicii de formă sau procedură.",
                        "Validare Formulare & Modele (Verificare completare)": "Ești un asistent administrativ riguros. Verifică dacă toate câmpurile din formular sunt completate, dacă datele sunt lizibile și dacă există greșeli vizibile."
                    }
                    
                    # Generare conținut
                    response = model.generate_content([prompts[tip_doc], img])
                    
                    st.success("Analiză Finalizată!")
                    st.subheader("📋 Raport de Analiză Senior")
                    st.markdown(response.text)
                    
            except Exception as e:
                # Dacă dă eroarea 404 din nou, încercăm automat cu prefixul 'models/'
                try:
                    model = genai.GenerativeModel('models/gemini-1.5-flash')
                    response = model.generate_content([prompts[tip_doc], img])
                    st.success("Analiză Finalizată (v2)!")
                    st.markdown(response.text)
                except:
                    st.error(f"Eroare tehnică: {e}. Asigură-te că API Key-ul este corect și activ.")

st.markdown("---")
st.caption("© IndexOficial.ro - Tehnologie AI pentru descifrarea birocrației.")
