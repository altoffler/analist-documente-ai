import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Index Oficial - Generator Acte", page_icon="📝")

st.title("📝 Generator de Cereri și Contestații")
st.markdown("Completează câmpurile de mai jos pentru a genera un document oficial.")

with st.sidebar:
    st.write("### Configurare")
    api_key = st.text_input("Introdu Cheia API Gemini", type="password")

nume = st.text_input("Numele tău complet")
institutie = st.text_input("Către ce instituție (ex: Primăria Beiuș, ANAF, etc.)")
problema = st.text_area("Descrie pe scurt problema (ex: adeverință sponsorizare, etc.)")

tip_act = st.selectbox("Ce fel de act vrei să generezi?", 
    ["Cerere Tip", "Contestație Amendă", "Plângere Prealabilă", "Solicitare Informații Publice"])

if st.button("Generează Documentul"):
    if not api_key or not nume or not problema:
        st.error("Te rugăm să completezi toate câmpurile și să introduci cheia API.")
    else:
        try:
            # REPARARE CRITICĂ: Forțăm transportul prin REST și folosim identificatorul generic 'gemini-pro'
            # Acest mod este cel mai compatibil cu orice versiune de API (v1 sau v1beta)
            genai.configure(api_key=api_key, transport='rest')
            model = genai.GenerativeModel('gemini-pro')
            
            prompt = f"Redactează o {tip_act} oficială către {institutie}, din partea lui {nume}, referitor la: {problema}. Include formule de adresare oficiale și text juridic adecvat."
            
            with st.spinner("Se generează documentul..."):
                response = model.generate_content(prompt)
                
                st.success("Documentul a fost generat!")
                st.text_area("Rezultat (Copiați în Word):", value=response.text, height=400)
                
        except Exception as e:
            # Plan de rezervă: încercăm cu numele complet al modelului dacă primul eșuează
            try:
                model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
                response = model.generate_content(prompt)
                st.success("Documentul a fost generat (v2)!")
                st.text_area("Rezultat:", value=response.text, height=400)
            except:
                st.error(f"Eroare: {e}. Verifică dacă cheia API este validă.")

st.markdown("---")
st.caption("© IndexOficial.ro")
