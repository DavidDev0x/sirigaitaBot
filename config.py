import json
import os

ARQUIVO_CONFIG = "config.json"

def salvar_config(dados):
    with open(ARQUIVO_CONFIG, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2)

def carregar_config():
    if not os.path.exists(ARQUIVO_CONFIG):
        return None

    with open(ARQUIVO_CONFIG, "r", encoding="utf-8") as f:
        return json.load(f)
