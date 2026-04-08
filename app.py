import streamlit as st
import openai

st.set_page_config(page_title="Index Oficial - Asistent AI", page_icon="⚖️", layout="centered")

# Design Minimalist & Oficial
st.title("⚖️ Analist AI Documente Oficiale")
st.markdown("---")

# Sidebar pentru Configurare
with st.sidebar:
    st.image("https://placeholder.com", use_container_width=True) # Poți pune URL-ul logo-ului tău
    api_key = st.text_input("Cheie API OpenAI", type="password", help="Introdu cheia ta API de pe ://openai.com")
    st.info("Datele tale sunt procesate prin API Enterprise și nu sunt folosite pentru antrenarea AI-ului.")

# Cele 4 Categorii conform meniului tău
tip_doc = st.selectbox(
    "Alege categoria documentului pentru o analiză precisă:",
    [
        "Legislație & Taxe (ANAF, Impozite, Notificări)",
        "Subvenții & Fonduri (APIA, AFIR, Start-up Nation)",
        "Administrativ (Poliție, Primărie, Ministere)",
        "Validare Formulare & Modele (Verificare completare)"
    ]
)

uploaded_file = st.file_uploader("Încarcă documentul (PDF sau Imagine)", type=['pdf', 'png', 'jpg', 'jpeg'])

if uploaded_file:
    if not api_key:
        st.error("Te rugăm să introduci cheia API în meniul din stânga pentru a începe.")
    else:
        if st.button("Descifrează Documentul"):
            with st.spinner("Analizăm clauzele și termenele legale..."):
                # Aici configurăm 'creierul' pentru fiecare nișă
                prompts = {
                    "Legislație & Taxe (ANAF, Impozite, Notificări)": "Ești expert fiscal în România. Identifică sumele, scadențele de plată, conturile IBAN și posibilitatea de eșalonare sau bonificație.",
                    "Subvenții & Fonduri (APIA, AFIR, Start-up Nation)": "Ești consultant fonduri europene. Verifică criteriile de eligibilitate menționate, termenele de depunere și documentele anexe necesare.",
                    "Administrativ (Poliție, Primărie, Ministere)": "Ești expert în administrație publică. Identifică termenul de contestație (ex. 15 zile), instituția competentă și eventualele vicii de formă.",
                    "Validare Formulare & Modele (Verificare completare)": "Verifică dacă formularul are toate câmpurile obligatorii completate și dacă informațiile sunt coerente."
                }
                
                # NOTĂ: Aici integrăm apelul real către OpenAI
                # Rezultatul va fi afișat sub formă de 'Raport de Analiză'
                
                st.success("Analiză Completă!")
                st.subheader("📋 Rezumat Executiv")
                st.write(f"**Tip detectat:** {tip_doc}")
                st.markdown("""
                ### 🚩 Ce trebuie să știi:
                *   **Termen critic:** [Data extrasă din document]
                *   **Suma/Obligația:** [Informația extrasă]
                *   **Următorul pas:** [Acțiunea recomandată]
                
                ---
                *Acesta este un asistent AI. Verificați întotdeauna informațiile cu un specialist autorizat.*
                """)
