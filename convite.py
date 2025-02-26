from PIL import Image, ImageDraw, ImageFont
from IPython.display import Image as imgx

nomes = ['Jeferson','Vitor', 'Mariana']
evento = 'Formatura do Python'
data = '27 de fevereiro de 2025'
local = 'Avenida Paulista, na Clarify'

for nome in nomes:
    # criando uma imagem em rgb com fundo branco (600 por 400px)
    img = Image.new("RGB", (600,400), (255,255,255)) # é criada a imagem em fundo branco
    draw = ImageDraw.Draw(img) # preparando a ferramenta para desenhar a imagem

    # fontes que serão usadas no texto
    font_title = ImageFont.truetype("arial.ttf",36)   
    font_text = ImageFont.truetype("arial.ttf",24)

    draw.text((50,50), f'Convite para {nome}',(0,0,0), font=font_title)

    draw.text((50,100), evento, (0,0,0), font=font_text)

    draw.text((50,150), data, (0,0,0), font=font_text)

    draw.text((50,200), local, (0,0,0), font=font_text)

    draw.rectangle([(45,45),(555,355)], outline=(62,229,229), width=5)

    img.save(f"{nome}.jpg")

    




