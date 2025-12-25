import tkinter as tk
import os
from tkinter import messagebox, ttk
import threading
from config import salvar_config, carregar_config
from bot import PokemonBot
from screen import selecionar_area_por_clique, capturar_area

# ===============================
# BOT
# ===============================
bot = PokemonBot()
area = None
img_base = None
config = carregar_config()

# ===============================
# FUNÇÕES
# ===============================

def selecionar_area_ui():
    global area, img_base
    messagebox.showinfo(
        "Selecionar área",
        "Selecione UMA área SEM Pokémon\n"
        "Clique no canto superior esquerdo\n"
        "Depois no inferior direito"
    )
    area = selecionar_area_por_clique()
    global img_base
    img_base = capturar_area(area)
    messagebox.showinfo("OK", "Área e imagem base capturadas")

def iniciar_bot():
    if area is None:
        messagebox.showwarning("Aviso", "Selecione a área primeiro")
        return

    img_base = capturar_area(area)

    hotkeys = {
        "target": entry_target.get().strip().lower(),
        "buff":   entry_buff.get().strip().lower(),
        "attack": entry_attack.get().strip().lower(),
        "heal":   entry_heal.get().strip().lower()
    }
    salvar_config({
        "hotkeys": hotkeys,
        "area": {
            "x": area[0],
            "y": area[1],
            "w": area[2],
            "h": area[3]
        }
    })

    if not all(hotkeys.values()):
        messagebox.showwarning("Aviso", "Preencha todas as hotkeys")
        return

    root.iconify()  # tira foco da interface

    threading.Thread(
        target=bot.iniciar,
        args=(area, img_base, hotkeys),
        daemon=True
    ).start()

    status_var.set("Bot rodando...")

def parar_bot():
    bot.parar()
    status_var.set("Bot parado")
    root.deiconify()

# ===============================
# INTERFACE
# ===============================
root = tk.Tk()
root.title("Sirigaita Bot")
root.geometry("380x500")
root.resizable(False, False)

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# ===============================
# ÍCONE DO APP (JANELA + BARRA)
# ===============================
try:
    icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")
    root.iconbitmap(icon_path)
except Exception as e:
    print("Não foi possível carregar o ícone:", e)

# ===============================
# ABA BOT
# ===============================
aba_bot = tk.Frame(notebook)
notebook.add(aba_bot, text="Bot")

tk.Label(aba_bot, text="Hotkeys", font=("Arial", 13, "bold")).pack(pady=8)

def campo(parent, label):
    tk.Label(parent, text=label).pack()
    e = tk.Entry(parent, justify="center")
    e.pack(pady=2)
    return e

entry_target = campo(aba_bot, "Target")
entry_buff   = campo(aba_bot, "Buff")
entry_attack = campo(aba_bot, "Attack")
entry_heal   = campo(aba_bot, "Heal")

if config and "hotkeys" in config:
    entry_target.insert(0, config["hotkeys"].get("target", ""))
    entry_buff.insert(0, config["hotkeys"].get("buff", ""))
    entry_attack.insert(0, config["hotkeys"].get("attack", ""))
    entry_heal.insert(0, config["hotkeys"].get("heal", ""))


tk.Button(aba_bot, text="Selecionar Área", width=30,
          command=selecionar_area_ui).pack(pady=10)

tk.Button(aba_bot, text="Iniciar Bot", width=30,
          bg="green", fg="white",
          command=iniciar_bot).pack(pady=6)

tk.Button(aba_bot, text="Parar Bot", width=30,
          bg="red", fg="white",
          command=parar_bot).pack(pady=6)

status_var = tk.StringVar(value="Aguardando...")
tk.Label(aba_bot, textvariable=status_var, fg="blue").pack(pady=12)

if config and "area" in config:
    a = config["area"]
    area = (a["x"], a["y"], a["w"], a["h"])
    status_var.set("Área carregada do config")

# ===============================
# ABA TUTORIAL
# ===============================
aba_tutorial = tk.Frame(notebook)
notebook.add(aba_tutorial, text="Tutorial")

tutorial_texto = (
    "🧠 COMO USAR O BOT\n\n"
    "1️⃣ Abra o jogo no MONITOR PRINCIPAL.\n"
    "2️⃣ Garanta que NÃO há Pokémon na tela.\n"
    "3️⃣ Vá até a aba 'Bot'.\n"
    "4️⃣ Preencha todas as hotkeys exatamente como no jogo.\n"
    "   (ex: 5, v, 6, f)\n\n"
    "5️⃣ Clique em 'Selecionar Área'.\n"
    "   • Selecione a área do painel de batalha\n"
    "   • Essa área deve estar SEM Pokémon.\n\n"
    "6️⃣ Clique em 'Iniciar Bot'.\n"
    "7️⃣ Clique dentro do jogo para dar foco.\n\n"
    "⚔️ QUANDO UM POKÉMON APARECER:\n"
    "• O painel muda\n"
    "• O bot detecta a diferença\n"
    "• Executa: Target → Buff → Attack → Heal\n\n"
    "🛑 Para parar o bot:\n"
    "• Vá até a aba Bot\n"
    "• Clique em 'Parar Bot'\n\n"
    "⚠️ DICAS IMPORTANTES:\n"
    "• Use teclas simples (números/letras)\n"
    "• Não use Ctrl, Shift ou Alt\n"
    "• Não mova a janela do jogo após selecionar a área\n"
)

txt = tk.Text(aba_tutorial, wrap="word", padx=10, pady=10)
txt.insert("1.0", tutorial_texto)
txt.config(state="disabled")
txt.pack(fill="both", expand=True)

# ===============================
# START
# ===============================
if __name__ == "__main__":
    root.mainloop()
