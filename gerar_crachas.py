import json 
import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

# 1. configurações e pastas
ARQUIVO_JSON = 'data/aluno.json'
PASTA_SALIDA = 'crachas_impressao'

if not os.path.exists(PASTA_SALIDA):
  os.makedirs(PASTA_SALIDA):

def gerar_crachas(): 
  try:
    with open(ARQUVO_JSON,'r',emncoding='utf-8') as f:
      aluno = json.load(f)
