import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Index Oficial - Generator Acte", page_icon="📝")

st.title("📝 Generator de Cereri și Contestații")
st.markdown("Completează câmpurile de mai jos pentru a genera un document oficial.")

# Sidebar pentru API Key
with st.sidebar:
    api_key = st.text_input("Introdu Cheia API Gemini", type="password")

# Formular de date
nume = st.text_input("Numele tău complet")
institutie = st.text_input("Către ce instituție (ex: Primăria Sector 3, ANAF, etc.)")
problema = st.text_area("Descrie pe scurt problema (ex: am primit o amendă de parcare, vreau o adeverință, etc.)")

tip_act = st.selectbox("Ce fel de act vrei să generezi?", 
    ["Cerere Tip", "Contestație Amendă", "Plângere Prealabilă", "Solicitare Informații Publice"])

if st.button("Generează Documentul"):
    if not api_key or not nume or not problema:
        st.error("Te rugăm să completezi toate câmpurile și să introduci cheia API.")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = f"""
            Ești un expert juridic în România. Redactează un document de tip {tip_act} oficial, sobru și corect gramatical.
            Expeditor: {nume}
            Destinatar: {institutie}
            Subiect: {problema}
            Te rog să incluzi formulele de adresare oficiale, baza legală generală și un spațiu pentru semnătură.
            """
            
            response = model.generate_content(prompt)
            
            st.success("Documentul a fost generat cu succes!")
            st.text_area("Copiați textul de mai jos în Word:", value=response.text, height=400)
            st.info("Sfat: Verifică documentul și adaugă datele tale specifice (CNP, adresă) înainte de a-l depune.")
            
        except Exception as e:
            st.error(f"Eroare: {e}")

st.markdown("---")
st.caption("© IndexOficial.ro")
