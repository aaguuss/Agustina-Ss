import streamlit as st
import hashlib
import io
import base64
from PIL import Image

# Intenta importar qrcode; si no está, lo avisa en la app
try:
    import qrcode
except ImportError:
    qrcode = None

# ==========================================
# ⚙️ CONFIGURACIÓN DE PÁGINA Y ESTILO HACKER
# ==========================================
st.set_page_config(
    page_title="Agustina: Misión oculta",
    page_icon="💋",
    layout="centered"
)

# Estilo personalizado Animal Print + Negro y Rojo
st.markdown("""
    <style>
    /* Fondo con patrón Animal Print de leopardo en tonos negro y rojo */
    .stApp {
        background-color: #0d0000;
        background-image: url('https://www.transparenttextures.com/patterns/leopard.png'); /* Textura de leopardo */
        color: #ff2a2a; /* Texto rojo neón */
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Cajas principales para legibilidad sobre el fondo */
    .stMarkdown, .stText {
        background-color: rgba(10, 0, 0, 0.88);
        padding: 10px;
        border-radius: 8px;
    }
    
    /* Botones negros con borde y texto rojo */
    .stButton>button {
        background-color: #000000;
        color: #ff2a2a;
        border: 2px solid #ff2a2a;
        border-radius: 8px;
        font-weight: bold;
    }
    
    /* Efecto al pasar el mouse por los botones */
    .stButton>button:hover {
        background-color: #ff2a2a;
        color: #000000;
        box-shadow: 0 0 12px #ff2a2a;
    }
    
    /* Entradas de texto */
    .stTextInput>div>div>input {
        background-color: #050000;
        color: #ff2a2a;
        border: 1px solid #ff2a2a;
    }
    </style>
""", unsafe_allow_html=True)

# Helper para verificar hashes SHA-256 (Protección anti-trampa)
def verificar_hash(texto, hash_esperado):
    return hashlib.sha256(texto.strip().lower().encode()).hexdigest() == hash_esperado

# ==========================================
# 🧠 MEMORIA DEL JUEGO (ESTADO DE NIVELES)
# ==========================================
if 'nivel' not in st.session_state:
    st.session_state.nivel = 1

# ==========================================
# 🖥️ ENCABEZADO Y BARRA DE PROGRESO
# ==========================================
st.title("🖤Desafio")
st.caption("🐆Acceso Restringido - Nivel de Seguridad HOT AF")

progreso = (st.session_state.nivel - 1) / 5.0
st.progress(progreso)
st.write(f"**Progreso de Misión:** Nivel {st.session_state.nivel} / 5")
st.divider()

# ==========================================
# 🔒 NIVEL 1: CIFRADO CÉSAR
# ==========================================
if st.session_state.nivel == 1:
    st.subheader("🍒 Nivel 1: Cifrado César")
    st.info("Agustina te ha dejado un mensaje interceptado. Aplica el desplazamiento para revelar la frase.")
    
    st.code("xdrpqfkx", language="text")
    st.write("💡 *Pista: Mueve cada letra el numero más cool en posiciones hacia atrás en el abecedario.*")
    
    input_n1 = st.text_input("Ingresa la frase descifrada:", key="n1_input")
    
    if st.button("🔓 Validar Nivel 1"):
        # Cambia aquí la respuesta si deseas (usa hash si no quieres texto plano)
        if input_n1.strip().lower() == "agustina":  
            st.success("HOTTT...ACCESO NIVEL 1 CONCEDIDO!")
            st.session_state.nivel = 2
            st.rerun()
        else:
            st.error("❌ Código incorrecto.buu you whore")

# ==========================================
# 🔑 NIVEL 2: CIFRADO VIGENÈRE (Pista Visual)
# ==========================================
elif st.session_state.nivel == 2:
    st.subheader("🍒 Nivel 2: Cifrado Vigenère")
    st.info("Inspecciona los registros del sistema para encontrar la Clave Maestra oculta.")
    
    log_falso = """
    [SYS_BOOT]: Iniciando protocolo de diagnóstico...
    [NET_TRACE]: BUSCANDO....
    [SECURITY_LOG]: Clave encriptada -> 'EL MEJOR GATO'
    [SYS_STATUS]: ÑAUUUU...
    """
    st.code(log_falso, language="syslog")
    
    input_n2 = st.text_input("Ingresa la clave identificada:", key="n2_input")
    
    if st.button("❤️ Validar Nivel 2"):
        if input_n2.strip().upper() == "ZARZUR":
            st.success("🐈 ¡CLAVE MAESTRA CONFIRMADA APROBADA POR EL TAYS!")
            st.session_state.nivel = 3
            st.rerun()
        else:
            st.error("❌ Clave no válida. Lee con atención las líneas [SECURITY_LOG].")

# ==========================================
# 🛡️ NIVEL 3: CIFRADO AES
# ==========================================
elif st.session_state.nivel == 3:
    st.subheader("🛡️ Nivel 3: Protocolo Criptográfico AES")
    st.info("2cf15ead85.")
    
    st.write("🔑 **Clave AES: chocolate fav")
    
    input_n3 = st.text_input("Ingresa la respuesta AES:", key="n3_input")
    
    if st.button("🔓 Validar Nivel 3"):
        if input_n3.strip().lower() == "teamo":
            st.success("BLOQUE AES DESENCRIPTADO CON ÉXITO! YOU ARE COOL")
            st.session_state.nivel = 4
            st.rerun()
        else:
            st.error("❌ Clave incorrecta.")

# ==========================================
# ⚛️ NIVEL 4: PROTOCOLO CUÁNTICO BB84
# ==========================================
elif st.session_state.nivel == 4:
    st.subheader("🐆 Nivel 4: Distribución Cuántica (BB84)")
    st.info("Compara las bases de medición para sintetizar los bits de la clave cuántica.")
    
    st.markdown("""
    | Fotones | Bases Enviadas | Bases Medidas | Coinciden? |
    | :---: | :---: | :---: | :---: |
    | 1 | + | + | Sí (1) |
    | 0 | x | + | No |
    | 1 | x | x | Sí (1) |
    | 0 | + | + | Sí (0) |
    """)
    
    input_n4 = st.text_input("Ingresa la cadena binaria resultante:", key="n4_input")
    
    if st.button("Gánale a un computador"):
        if input_n4.strip() == "110":
            st.success(" ERES MEJOR QUE UN COMPUTADOR CUÁNTICO!")
            st.session_state.nivel = 5
            st.rerun()
        else:
            st.error("▄︻デ══━一 Los bits no coinciden con las bases filtradas.")

# ==========================================
# 🖼️ NIVEL 5: ESTEGANOGRAFÍA Y MÚSICA (FINAL)
# ==========================================

# ==========================================
# 🏁 NIVEL 5: REVELACIÓN FINAL Y MÚSICA
# ==========================================
elif st.session_state.nivel == 5:
    st.subheader("🏁 Nivel 5: Desencriptación Final")
    st.info("Ingresa la Clave y libera la transmisión de audio y el mensaje secreto.")
    
    input_clave_final = st.text_input("Clave Cuántica de Activación:", placeholder="sex number...")
    
    if st.button("🎉 REVELAR REGALO Y FINAL"):
        if input_clave_final.strip() == "69":
            st.balloons()
            st.success("💖 esooo")
            
            st.markdown("### 💌 Mensaje Secreto:")
            st.write("lo lograste baddie... elige tu premio")
            
            st.divider()
            st.subheader("🎧 Transmisión de Audio Secreta:")
            
            link_youtube = "https://youtu.be/SA7AIQw-7Ms?si=eFJHaLEO36ktj6yp" # Tu enlace de YouTube
            
            if qrcode:
                qr = qrcode.make(link_youtube)
                buf = io.BytesIO()
                qr.save(buf)
                st.image(buf.getvalue(), caption="📲 Escanea con tu celular para escuchar nuestra canción", width=220)
            
            st.link_button("▶ Escuchar transmisión directa en YouTube", link_youtube)
        else:
            st.error("mala vola")
