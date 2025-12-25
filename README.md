Aqui vai uma **versão melhorada, mais profissional e organizada do README**, mantendo o tom simples, mas com cara de projeto sólido de GitHub 🚀

Você pode **copiar e colar direto** no `README.md`.

---

# 🐍🎮 Sirigaita Bot

**Sirigaita Bot** é um bot em **Python** para automação de batalhas em jogos (ex: Pokémon), utilizando **reconhecimento de imagem** e **hotkeys configuráveis**.
Ideal para quem deseja automatizar ações repetitivas de forma simples e eficiente.

---

## 🚀 Principais Recursos

* 📸 **Detecção visual inteligente** de mudanças na tela
* 🎯 **Execução automática de hotkeys** (Target, Buff, Attack, Heal)
* 💾 **Salvamento automático de configurações** (hotkeys e área da tela)
* 🖥️ **Interface gráfica intuitiva** desenvolvida em Tkinter
* 📦 **Executável (.exe)** — não requer Python instalado
* ⚡ Baixo consumo de recursos e execução estável

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Tkinter** — Interface gráfica
* **OpenCV** — Reconhecimento de imagem
* **PyAutoGUI** — Automação de teclado e mouse
* **pynput** — Captura de hotkeys
* **PyInstaller** — Geração do executável

---

## ▶️ Como Usar (Modo Python)

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/DavidDev0x/sirigaita-bot.git
cd sirigaita-bot
```

### 2️⃣ Crie e ative um ambiente virtual (opcional, recomendado)

```bash
python -m venv venv
```

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Execute o bot

```bash
python main.py
```

---

## ▶️ Como Usar (Executável `.exe`)

1. Baixe o arquivo **`SirigaitaBot.exe`**
2. Execute normalmente (duplo clique)
3. Configure as **hotkeys**
4. Selecione a **área da batalha**
5. Inicie o bot 🎮

📁 Todas as configurações são salvas automaticamente no arquivo:

```text
config.json
```

---

## ⚠️ Observações Importantes

* O jogo deve estar em **modo janela**
* Utilize preferencialmente o **monitor principal**
* Caso a **resolução da tela mude**, será necessário selecionar a área novamente
* Execute como **Administrador** caso o bot não detecte hotkeys corretamente

---

## 📦 Gerar o Executável (.exe)

### 1️⃣ Instale o PyInstaller

```bash
pip install pyinstaller
```

### 2️⃣ Gere o executável

```bash
python -m PyInstaller --onefile --windowed --name SirigaitaBot --icon=icon.ico main.py
```

📂 O arquivo final será gerado na pasta:

```text
/dist/SirigaitaBot.exe
```

---

## 🧠 Estrutura do Projeto

```text
sirigaita-bot/
│
├── main.py
├── config.json
├── requirements.txt
├── icon.ico
├── /src
├── /dist
└── README.md
```

---

## 📜 Aviso Legal

Este projeto é destinado **exclusivamente para fins educacionais**.
O uso em jogos online pode violar os termos de serviço do jogo.
Use por sua conta e risco.

---

## ⭐ Contribuições

Pull requests são bem-vindos!
Se tiver ideias, melhorias ou correções, fique à vontade para contribuir.

---


