from barcode import EAN13
from barcode.writer import ImageWriter
import qrcode
import os


#BASE SIMPLES
# codigo_barra = EAN13('111111111111', writer=ImageWriter())
# codigo_barra.save('codigo_barra') 
#EAN13 sempre de os 12 primeiros números o 13º vai ser gerado automaticamente de forma randomica.

codigos_produtos = {
    'Coca' : '111111111111',
    'Cocazero' : '111111111112',
    'Fantauva' : '111111111113',
    'Fantalaranja' : '111111111114',
    'Sprite' : '111111111115',
    'Cha-mate' : '111111111116',
    'Sucouva' : '111111111117',
    'Sucolaranja' : '111111111118',
    'Arroz' : '111111111119',
    'Brigadeiro' : '222222222222'}

for produto in codigos_produtos:
    codigo = codigos_produtos[produto]
    codigo_barra = EAN13(codigo, writer=ImageWriter())
    codigo_barra.save(f'codigo_barra_{produto}')
    print(codigos_produtos)

# imagem_qrcode = qrcode.make('link')
# imagem_qrcode.save(qrcode.png)

links_produtos = {
    'Steam' : 'https://steamcommunity.com/id/Nakrou',
    'GamersClub' : 'https://gamersclub.com.br/player/480257',
    'Instagram' : 'https://www.instagram.com/zuzangado/',
    'Twitter' : 'https://twitter.com/ArturZuza',
    'Site' : 'linktr.ee/ArturZuza'}


for produtoqr in links_produtos:
    link = links_produtos[produtoqr]
    imagem_qrcode = qrcode.make(link)
    imagem_qrcode.save(f'qrcode_{produtoqr}.png')

    print(links_produtos)