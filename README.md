# Reconhecer texto da imagem
Projeto que reconhece e extrai texto da imagem


## Instalações
- No terminal do PyCharm, exercutar os comandos:
  - `pip install pytesseract`
  - `pip install opencv-python`

- Se estiver utilizando Windows provavelmente vai dar erro quando rodar o código (antes de rodar qualquer linha de código que usa o tesseract, é necessário passar o local do tesseract),  para isso:
  - é necessário seguir esses passos [stackoverflow](https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i)
     - baixar o Tesseract [baixar](https://github.com/UB-Mannheim/tesseract/wiki)
     - copiar o caminho da pasta onde vai ser salvo:
     - 
        ![tesseract](https://user-images.githubusercontent.com/53915799/158419184-6d3bdad3-17c0-43ee-8625-b3cd554a437d.png)
     - definir o caminho do tesseract no script: `pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'`
 
 ### Observação
 - Se quiser que o texto extraído fique em português (com acentos, cedilha etc), é necessário baixar o arquivo [acesse aqui](https://github.com/tesseract-ocr/tessdata/blob/main/por.traineddata), acessar a pasta do Tesseract-OCR e colar dentro da pasta tessdata
 - No código adicionar `lang="por"` em `texto = pytesseract.image_to_string(imagem, lang="por")`
 - Para ver o projeto funcionando: 
