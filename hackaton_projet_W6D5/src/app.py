# src/app.py
import streamlit as st
import PyPDF2
import io
import re
from transformers import pipeline
import torch

class LuxuryBrandAnalyzer:
    def __init__(self):
        st.info("Initialisation du système d'analyse Solweig & Izar...")
        try:
            # Configuration spécifique pour M1
            device = "mps" if torch.backends.mps.is_available() else "cpu"
            self.classifier = pipeline(
                "zero-shot-classification",
                model="facebook/bart-large-mnli",
                device=device
            )
            st.success("✅ Système initialisé avec succès")
        except Exception as e:
            st.error(f"⚠️ Erreur d'initialisation: {str(e)}")
            self.classifier = None

    def _extract_finishes(self, text):
        """Extraction des finitions selon notre méthodologie S&I"""
        finishes = {
            "métallique": ["palladium", "ruthénium", "or", "doré", "argenté"],
            "cuir": ["grainé", "lisse", "embossé", "patiné", "glacé"],
            "textile": ["brodé", "matelassé", "plissé", "surpiqué"],
            "technique": ["thermocollé", "soudé", "assemblé main"]
        }
        
        found_finishes = {}
        for category, terms in finishes.items():
            found = [term for term in terms if term.lower() in text.lower()]
            if found:
                found_finishes[category] = found
                
        return found_finishes if found_finishes else {"status": "Non détectées"}

    def _extract_distinctive(self, text):
        """Extraction des éléments distinctifs"""
        distinctive = {
            "fermoirs": ["twist", "tournisis", "cadenas", "serrure"],
            "logos": ["monogramme", "sigle", "emblème", "signature"],
            "motifs": ["damier", "chevron", "cannage", "matelassé"]
        }
        
        found_elements = {}
        for category, elements in distinctive.items():
            found = [elem for elem in elements if elem.lower() in text.lower()]
            if found:
                found_elements[category] = found
                
        return found_elements if found_elements else {"status": "Non détectés"}

    # ... [Reste du code inchangé] ...

def main():
    st.set_page_config(
        page_title="S&I Analyzer",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    st.title("🎨 Solweig & Izar - Analyseur d'ADN de Marque")
    st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stTitle {
        color: #1e3d59;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Sidebar avec informations sur le système
    with st.sidebar:
        st.header("📊 Informations Système")
        st.write("Device:", "Apple Silicon (M1)" if torch.backends.mps.is_available() else "CPU")
        st.write("Mode:", "Haute précision")
        
    uploaded_file = st.file_uploader(
        "📄 Déposez votre document PDF",
        type=['pdf']
    )
    
    if uploaded_file:
        analyzer = LuxuryBrandAnalyzer()
        
        with st.spinner("🔍 Analyse en cours..."):
            text = analyzer.extract_text_from_pdf(uploaded_file)
            
            if text:
                results = analyzer.analyze_dna(text)
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.subheader("🔹 Identifiants Fondamentaux")
                    st.json(results["identifiants_fondamentaux"])
                
                with col2:
                    st.subheader("🔸 Attributs Techniques")
                    st.json(results["attributs_techniques"])
                
                with col3:
                    st.subheader("✨ Signatures Visuelles")
                    st.json(results["signatures_visuelles"])

if __name__ == "__main__":
    main()
