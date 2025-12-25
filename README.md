# Sirigaita Bot 🐍🎮

Bot em Python para automação de batalhas em jogos (ex: Pokémon),
utilizando reconhecimento de imagem e hotkeys configuráveis.

---

## ✨ Funcionalidades

- 📸 Detecção visual de mudança na tela
- 🎯 Execução automática de hotkeys (Target, Buff, Attack, Heal)
- 💾 Salva configurações automaticamente (hotkeys + área)
- 🖥️ Interface gráfica em Tkinter
- 📦 Executável `.exe` (não precisa Python instalado)

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- Tkinter
- OpenCV
- PyAutoGUI
- pynput
- PyInstaller

---

## ▶️ Como Usar (Python)

1. Clone o repositório:
   ```bash
   git clone https://github.com/DavidDev0x/sirigaita-bot.git
Crie e ative um ambiente virtual

Instale as dependências:

pip install -r requirements.txt


Execute:

python main.py

▶️ Como Usar (Executável)

Baixe o arquivo SirigaitaBot.exe

Execute normalmente

Configure as hotkeys

Selecione a área de batalha

Inicie o bot

As configurações são salvas automaticamente no arquivo config.json.

⚠️ Observações Importantes

O jogo deve estar em modo janela

Recomenda-se usar o monitor principal

Caso a resolução mude, selecione a área novamente

📦 Gerar o Executável
Instale o PyInstaller (se ainda não tiver):

pip install pyinstaller

Gere o executável:

python -m PyInstaller --onefile --windowed --name SirigaitaBot --icon=icon.ico main.py
O executável será gerado na pasta dist/.