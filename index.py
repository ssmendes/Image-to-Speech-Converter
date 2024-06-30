import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
import pytesseract
from gtts import gTTS
import os
from PIL import Image, ImageTk
import pygame

# Função para selecionar a imagem
def select_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")]
    )
    if file_path:
        path_label.config(text=file_path)
        display_image(file_path)
    else:
        messagebox.showwarning("No file selected", "No image was selected.")

# Função para exibir a imagem selecionada
def display_image(file_path):
    img = Image.open(file_path)
    img.thumbnail((300, 300))
    img = ImageTk.PhotoImage(img)
    image_label.config(image=img)
    image_label.image = img

# Função para extrair texto e converter para áudio
def process_image():
    file_path = path_label.cget("text")
    if not file_path:
        messagebox.showwarning("No file selected", "Please select an image first.")
        return
    
    try:
        # Lê a imagem usando OpenCV
        image = cv2.imread(file_path)
        
        # Caminho para o Tesseract OCR
        path = r"C:\Program Files\Tesseract-OCR"
        pytesseract.pytesseract.tesseract_cmd = os.path.join(path, "tesseract.exe")
        
        # Extrai o texto da imagem
        text = pytesseract.image_to_string(image)
        messagebox.showinfo("Extracted Text", text)
        
        # Converte o texto para fala
        language = "en"
        tts = gTTS(text, lang=language)
        audio_path = "audio.mp3"
        tts.save(audio_path)
        
        # Reproduz o áudio
        play_audio(audio_path)
        
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Função para reproduzir o áudio
def play_audio(audio_path):
    pygame.mixer.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

# Criação da janela principal
root = tk.Tk()
root.title("Image to Speech Converter")
root.geometry("600x600")

# Botão para selecionar a imagem
upload_button = tk.Button(root, text="Select Image", command=select_image)
upload_button.pack(pady=10)

# Rótulo para exibir o caminho da imagem
path_label = tk.Label(root, text="")
path_label.pack(pady=5)

# Rótulo para exibir a imagem selecionada
image_label = tk.Label(root)
image_label.pack(pady=10)

# Botão para processar a imagem
process_button = tk.Button(root, text="Process Image", command=process_image)
process_button.pack(pady=10)

# Execução da janela principal
root.mainloop()
