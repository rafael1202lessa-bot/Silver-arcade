import streamlit as st

# Configura a página para modo amplo (aproveita melhor a tela dos PCs da escola)
st.set_page_config(page_title="Central de Jogos da Escola", page_icon="🕹️", layout="wide")

st.title("🕹️ Central de Jogos - Hora Livre")
st.markdown("Chega de perder tempo procurando! Escolha um jogo abaixo e divirta-se.")

# Criando as abas de categorias para organizar os jogos
aba_arcade, aba_retro, aba_puzzle = st.tabs(["🎮 Arcade Clássico", "👾 Retrô / Cobrinha", "🧩 Quebra-Cabeça"])

# --- ABA 1: ARCADE CLÁSSICO (Pacman Aberto) ---
with aba_arcade:
    st.subheader("Pacman Clássico")
    st.caption("Comandos: Clique na tela do jogo e use as setas do teclado para mover.")
    
    # Versão open-source hospedada no GitHub Pages que aceita iframe
    st.components.v1.iframe("https://macek.github.io/google_pacman/", height=450, scrolling=False)

# --- ABA 2: RETRÔ (Jogo da Cobrinha Clássico) ---
with aba_retro:
    st.subheader("Snake Game (Jogo da Cobrinha)")
    st.caption("Comandos: Use as setas do teclado para coletar os pontos.")
    
    # Versão aberta e nostálgica da cobrinha
    st.components.v1.iframe("https://thesnakegame.github.io/", height=500, scrolling=False)

# --- ABA 3: QUEBRA-CABEÇA (2048 Open-Source) ---
with aba_puzzle:
    st.subheader("2048")
    st.caption("Comandos: Use as setas para juntar os números iguais.")
    
    # O criador original do 2048 (Gabriele Cirulli) deixa o código aberto no GitHub Pages
    st.components.v1.iframe("https://gabrielecirulli.github.io/2048/", height=650, scrolling=False)

# --- MENU LATERAL ---
st.sidebar.title("🎮 Sobre a Central")
st.sidebar.info(
    "Este site foi criado para salvar a galera na hora livre da sala de informática! "
    "Os jogos rodam direto no navegador, sem precisar instalar nada."
)
st.sidebar.markdown("---")
st.sidebar.markdown("💻 **Desenvolvido por Rafael Lessa**")
