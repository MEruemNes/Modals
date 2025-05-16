import streamlit as st

st.set_page_config(page_title="Modül Seçimi", layout="centered")

st.title("📚 Modül Seçimi Yapınız")

modul = st.radio(
    "Lütfen bir modül seçin:",
    ("1 - A1", "2 - A2", "3 - B1", "4 - B2")
)

linkler = {
    "1 - A1": "https://example.com/A1",
    "2 - A2": "https://example.com/A2",
    "3 - B1": "https://calculator-jctqjn5zjrrasjtf2jw5wi.streamlit.app/",
    "4 - B2": "https://example.com/B2"
}

if st.button("Devam Et"):
    secilen_link = linkler.get(modul)
    st.success("Yönlendiriliyorsunuz:")
    st.markdown(f"[👉 Buraya tıklayın]({secilen_link})", unsafe_allow_html=True)
