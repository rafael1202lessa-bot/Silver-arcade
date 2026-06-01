import streamlit as st

# Configura a página para modo amplo (aproveita melhor a tela dos PCs da escola)
st.set_page_config(page_title="Central de Jogos da Escola", page_icon="🕹️", layout="wide")

st.title("🕹️ Central de Jogos - Hora Livre")
st.markdown("Chega de perder tempo procurando! Escolha um jogo abaixo e divirta-se.")

# Criando as abas de categorias para organizar os jogos
aba_arcade, aba_retro, aba_puzzle = st.tabs(["🎮 Arcade Clássico", "👾 Retrô / Cobrinha", "🧩 Quebra-Cabeça"])

# --- ABA 1: ARCADE CLÁSSICO (Pacman) ---
with aba_arcade:
    st.subheader("Playman / Pacman")
    st.caption("Comandos: Use as setas do teclado para mover o Pacman pelo labirinto.")
    
    # Abre o jogo direto na tela através de um iframe limpo
    st.components.v1.iframe("https://pacman.live/play.html", height=600, scrolling=False)

# --- ABA 2: RETRÔ (Jogo da Cobrinha do Google) ---
with aba_retro:
    st.subheader("Snake Game (Jogo da Cobrinha)")
    st.caption("Comandos: Use as setas do teclado para comer as frutas e crescer.")
    
    st.components.v1.iframe("https://www.google.com/fbx?fbx=snake", height=550, scrolling=False)

# --- ABA 3: QUEBRA-CABEÇA (2048) ---
with aba_puzzle:
    st.subheader("2048 Clássico")
    st.caption("Comandos: Use as setas para somar os blocos iguais até chegar no bloco 2048.")
    
    st.components.v1.iframe("https://play2048.co/", height=650, scrolling=False)

# --- MENU LATERAL ---
st.sidebar.title("🎮 Sobre a Central")
st.sidebar.info(
    "Este site foi criado para salvar a galera na hora livre da sala de informática! "
    "Os jogos rodam direto no navegador, sem precisar instalar nada."
)
st.sidebar.markdown("---")
st.sidebar.markdown("💻 **Desenvolvido por Rafael Lessa**")
