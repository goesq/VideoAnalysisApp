# 🎧 Analisador de Vídeo do YouTube

Este é um app em Python que permite você colar a URL de um vídeo do YouTube, extrair o áudio, transcrevê-lo com Whisper e gerar um resumo com um modelo da 
Hugging Face — tudo isso com uma interface web usando **Streamlit**. 🚀

---

## 📦 Tecnologias Usadas

- [Python 3.8+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [Whisper](https://github.com/openai/whisper)
- [Transformers - Hugging Face](https://huggingface.co/)
- [Pydub](https://github.com/jiaaro/pydub)
- [ffmpeg](https://ffmpeg.org/)

---

## ⚙️ Instalação

```bash
git clone 'https://github.com/goesq/VideoAnalysisApp/'
cd video-analyzer-app
python -m venv venv
venv\Scripts\activate   # no Windows
pip install -r requirements.txt
```

> ⚠️ Certifique-se de ter o `ffmpeg` instalado e adicionado ao PATH do sistema.

---

## 🧠 Executando o App

```bash
python -m streamlit run streamlit_app.py
```

Abra o navegador em: [http://localhost:8501](http://localhost:8501)

---

## ✅ O que o app faz?

1. Você cola a URL de um vídeo do YouTube 🎥  
2. Ele baixa o áudio do vídeo 🎧  
3. Transcreve o áudio usando o Whisper da OpenAI ✍️  
4. Resume o conteúdo com o modelo BART da Hugging Face 📌  
5. Mostra a transcrição completa e o resumo direto na tela 💬

---

## 📁 Estrutura do Projeto

```
VideoAnalysisApp/
│
├── audio/                  # Arquivos de áudio temporários
├── streamlit_app.py        # Código principal da aplicação
├── requirements.txt        # Lista de dependências
└── README.md               # Este arquivo
```

---

## 📌 Exemplo de Uso

Cole um link público do YouTube, como:

```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

E veja o resumo gerado automaticamente!

---

![image](https://github.com/user-attachments/assets/d81f8879-7f30-492f-81e9-a963fc4f0ec0)

