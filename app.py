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

# Estilo personalizado Cyberpunk (Fondo oscuro, texto verde Neón)
st.markdown("""
    <style>
    .stApp {
        background-color: #0d1117;
        color: #00ff66;
        font-family: 'Courier New', Courier, monospace;
    }
    .stButton>button {
        background-color: #1f2937;
        color: #00ff66;
        border: 1px solid #00ff66;
        border-radius: 8px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #00ff66;
        color: #0d1117;
    }
    .stTextInput>div>div>input {
        background-color: #161b22;
        color: #00ff66;
        border: 1px solid #30363d;
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
st.caption("🔒 Acceso Restringido - Nivel de Seguridad HOT AF")

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
    [NET_TRACE]: Conexión establecida con Nodo #7.
    [SECURITY_LOG]: Clave encriptada -> 'GATO'
    [SYS_STATUS]: Esperando autorización de usuario...
    """
    st.code(log_falso, language="syslog")
    
    input_n2 = st.text_input("Ingresa la clave identificada:", key="n2_input")
    
    if st.button("❤️ Validar Nivel 2"):
        if input_n2.strip().upper() == "GATO":
            st.success("✅ ¡CLAVE MAESTRA CONFIRMADA APROBADA POR EL TAYS!")
            st.session_state.nivel = 3
            st.rerun()
        else:
            st.error("❌ Clave no válida. Lee con atención las líneas [SECURITY_LOG].")

# ==========================================
# 🛡️ NIVEL 3: CIFRADO AES
# ==========================================
elif st.session_state.nivel == 3:
    st.subheader("🛡️ Nivel 3: Protocolo Criptográfico AES")
    st.info("Descifra el bloque cifrado con la clave combinada de los niveles anteriores.")
    
    st.write("🔑 **Clave AES:** `GATO` + `5` (Tu clave es: `GATO5`)")
    
    input_n3 = st.text_input("Ingresa la respuesta AES:", key="n3_input")
    
    if st.button("🔓 Validar Nivel 3"):
        if input_n3.strip().lower() == "cyberamor":
            st.success("✅ ¡BLOQUE AES DESENCRIPTADO CON ÉXITO!")
            st.session_state.nivel = 4
            st.rerun()
        else:
            st.error("❌ Clave incorrecta.")

# ==========================================
# ⚛️ NIVEL 4: PROTOCOLO CUÁNTICO BB84
# ==========================================
elif st.session_state.nivel == 4:
    st.subheader("⚛️ Nivel 4: Distribución Cuántica (BB84)")
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
    
    if st.button("🔓 Validar Nivel 4"):
        if input_n4.strip() == "110":
            st.success("✅ ¡CANAL CUÁNTICO ESTABLECIDO!")
            st.session_state.nivel = 5
            st.rerun()
        else:
            st.error("❌ Los bits no coinciden con las bases filtradas.")

# ==========================================
# 🖼️ NIVEL 5: ESTEGANOGRAFÍA Y MÚSICA (FINAL)
# ==========================================
elif st.session_state.nivel == 5:
    st.subheader("🏁 Nivel 5: Extracción Esteganográfica Final")
    st.write("Sube la imagen `.png` para desencriptar el último mensaje y activar la banda sonora.")
    
    subir_foto = st.file_uploader("Cargar Foto Secreta (.png)", type=["png"])
    input_clave_final = st.text_input("Clave Cuántica de Activación (Nivel 4):", value="110")
    
    if st.button("🎉 REVELAR REGALO Y FINAL"):
        if subir_foto is not None and input_clave_final == "110":
            st.balloons()
            st.success("💖 ¡MISIÓN COMPLETADA CON ÉXITO!")
            st.markdown("### 💌 Mensaje Secreto:")
            st.write("¡Hackeaste mi corazón! Tu regalo está esperándote en la mesa de noche. 🎁")
            
            st.divider()
            st.subheader("🎧 Transmisión de Audio Privada:")
            
            # Link a YouTube
            link_youtube = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" # Pon tu canción aquí
            
            if qrcode:
                qr = qrcode.make(link_youtube)
                buf = io.BytesIO()
                qr.save(buf)
                st.image(buf.getvalue(), caption="📲 Escanea con tu celular para escuchar nuestra canción", width=200)
            
            st.link_button("▶️ Abrir canción directamente en YouTube", link_youtube)
        else:
            st.error("⚠️ Sube el archivo de imagen correcto para finalizar.")
