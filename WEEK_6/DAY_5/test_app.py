import streamlit as st

def main():
    st.title("Solweig & Izar - Document Analyzer")
    st.write("Test de configuration")
    
    # Upload de fichier
    file = st.file_uploader(
        "Déposez un document ou une image",
        type=['txt', 'pdf', 'png', 'jpg', 'jpeg']
    )
    
    if file:
        st.success(f"Fichier reçu : {file.name}")

if __name__ == "__main__":
    main()
