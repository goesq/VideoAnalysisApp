import os
from yt_dlp import YoutubeDL
from pydub import AudioSegment
import whisper
from transformers import pipeline

modelo_whisper = whisper.load_model("base")
resumidor = pipeline("summarization", model="facebook/bart-large-cnn")

def baixar_audio(url):
    output_path = 'audio/temp.%(ext)s'
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return 'audio/temp.mp3'

def transcrever_audio(caminho_audio):
    result = modelo_whisper.transcribe(caminho_audio)
    return result['text']

def resumir_texto(texto):
    if len(texto) > 1024:
        partes = [texto[i:i+1024] for i in range(0, len(texto), 1024)]
        resumos = [resumidor(p, max_length=130, min_length=30, do_sample=False)[0]['summary_text'] for p in partes]
        return " ".join(resumos)
    else:
        return resumidor(texto, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
