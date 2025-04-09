import streamlit as st
import os
from utils.processamento import baixar_audio, transcrever_audio, resumir_texto

st.set_page_config(page_title="Análise de Vídeo", layout="centered")
st.title("📺 Análise e Resumo de Vídeos do YouTube")
url = st.text_input("Cole o link do vídeo:")

if st.button("Analisar"):
    if url:
        with st.spinner("🎧 Baixando e processando..."):
            if not os.path.exists("audio"):
                os.makedirs("audio")
            caminho_audio = baixar_audio(url)
            texto = transcrever_audio(caminho_audio)
            resumo = resumir_texto(texto)

        st.success("✅ Pronto!")
        st.subheader("📝 Transcrição")
        st.text_area("Texto transcrito", texto, height=300)

        st.subheader("🔍 Resumo")
        st.text_area("Resumo", resumo, height=150)
    else:
        st.warning("Insira uma URL primeiro.")
