import streamlit as st

st.set_page_config(page_title="Générateur Lettre Motivation", page_icon="💌")

st.title("💌 Générateur de Lettre de Motivation")
st.write("Créez une lettre de motivation pour Campus France en 30 secondes")

universite = st.text_input("Nom de l'université")
filiere = st.text_input("Filière souhaitée")
motivation = st.text_area("Pourquoi cette filière ?")

if st.button("Générer la lettre"):
    if universite and filiere and motivation:
        lettre = f"""
Madame, Monsieur,

Je souhaite intégrer la formation {filiere} à {universite} à la rentrée 2026.

{motivation}

Je suis convaincu que cette formation correspond parfaitement à mon projet professionnel et que je saurai m'investir pleinement.

Je vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations distinguées.
        """
        st.success("Voici votre lettre :")
        st.text_area("Copiez votre lettre", lettre, height=300)
    else:
        st.warning("Veuillez remplir tous les champs")

st.caption("Projet réalisé avec Python et Streamlit par cityfes211-max")
