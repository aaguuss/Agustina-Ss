import streamlit as st
import hashlib
import io
import base64
from PIL import Image

# Verificación e importación de QR
try:
    import qrcode
except ImportError:
    qrcode = None

# ==========================================
# ⚙️ CONFIGURACIÓN DE PÁGINA Y ESTILO HACKER
# ==========================================
st.set_page_config(
    page_title="CYBER-ESCAPE: Misión Secreta",
    page_icon="🕵️‍♀️",
    layout="centered"
)

# Estilo Neón/Cyberpunk
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

# Validación mediante SHA-256 (Anti-Trampa)
def verificar_hash(texto, hash_esperado):
    return hashlib.sha256(texto.strip().lower().encode()).hexdigest() == hash_esperado

# ==========================================
# 🧠 ESTADO DEL JUEGO
# ==========================================
if 'nivel' not in st.session_state:
    st.session_state.nivel = 1

# ==========================================
# 🖥️ ENCABEZADO
# ==========================================
st.title("💻 CYBER-ESCAPE ROOM")
st.caption("🔒 Terminal de Operaciones Espaciales - Nivel de Seguridad Alfa")

progreso = (st.session_state.nivel - 1) / 5.0
st.progress(progreso)
st.write(f"**Progreso:** Nivel {st.session_state.nivel} / 5")
st.divider()

# ==========================================
# 🔒 NIVEL 1: CÉSAR
# ==========================================
if st.session_state.nivel == 1:
    st.subheader("🏛️ Nivel 1: Cifrado César")
    st.info("Interceptado canal primario. Aplica el desplazamiento necesario para descifrar la frase.")
    
    st.code("MFRXF B RFG15 (Shift: 5)", language="text")
    st.write("💡 *Pista: Desplaza cada letra 5 posiciones hacia atrás en el abecedario.*")
    
    input_n1 = st.text_input("Ingresa la frase descifrada:", key="n1_input")
    
    if st.button("🔓 Validar Nivel 1"):
        # Hash de "hola a todos" (Puedes cambiar la respuesta calculando tu propio hash)
        if verificar_hash(input_n1, "a9987a020be8a9840ef403faed5578ee150d1704257850ed319fb4f4c8032e3a"): 
            st.success("✅ ¡ACCESO NIVEL 1 CONCEDIDO!")
            st.session_state.nivel = 2
            st.rerun()
        else:
            st.error("❌ Frase incorrecta.")

# ==========================================
# 🔑 NIVEL 2: VIGENÈRE (Pista Visual)
# ==========================================
elif st.session_state.nivel == 2:
    st.subheader("🔑 Nivel 2: Cifrado Vigenère")
    st.info("Inspecciona los registros del sistema. La clave maestra fue grabada en los logs.")
    
    log_falso = """
    [SYS_BOOT]: Protocolo de diagnóstico activado...
    [NET_TRACE]: Nodo #7 respondiendo correctamente.
    [SECURITY_LOG]: Master Key temporal capturada -> 'GATO'
    [SYS_STATUS]: Esperando ingreso de credenciales...
    """
    st.code(log_falso, language="syslog")
    
    input_n2 = st.text_input("Ingresa la clave hallada:", key="n2_input")
    
    if st.button("🔓 Validar Nivel 2"):
        if input_n2.strip().upper() == "GATO":
            st.success("✅ ¡CLAVE ACEPTADA!")
            st.session_state.nivel = 3
            st.rerun()
        else:
            st.error("❌ Clave no válida. Lee las líneas de [SECURITY_LOG].")

# ==========================================
# 🛡️ NIVEL 3: CIFRADO AES
# ==========================================
elif st.session_state.nivel == 3:
    st.subheader("🛡️ Nivel 3: Protocolo AES")
    st.info("Sintetiza la clave AES combinando la respuesta del Nivel 2 + el número del Nivel 1.")
    
    st.write("🔑 **Clave AES requerida:** `GATO` + `5` = `GATO5`")
    
    input_n3 = st.text_input("Ingresa la solución del bloque AES:", key="n3_input")
    
    if st.button("🔓 Validar Nivel 3"):
        # Hash de "cyberamor"
        if verificar_hash(input_n3, "667a760de8f58b8f2d593fa8ea260a9f5d3ff216f4ad259b39dfed4142f9b2d3"):
            st.success("✅ ¡DESENCRIPTACIÓN AES COMPLETADA!")
            st.session_state.nivel = 4
            st.rerun()
        else:
            st.error("❌ Clave incorrecta.")

# ==========================================
# ⚛️ NIVEL 4: BB84 Y CÓDIGO QR
# ==========================================
elif st.session_state.nivel == 4:
    st.subheader("⚛️ Nivel 4: Distribución Cuántica (BB84)")
    st.info("Compara las bases de medición y extrae los bits donde ambas coincidan.")
    
    st.markdown("""
    | Fotón | Base Enviada | Base Medida | Bit Valido |
    | :---: | :---: | :---: | :---: |
    | 1 | + | + | **1** |
    | 0 | x | + | *Descartado* |
    | 1 | x | x | **1** |
    | 0 | + | + | **0** |
    """)
    
    input_n4 = st.text_input("Ingresa la cadena binaria (3 bits):", key="n4_input")
    
    if st.button("🔓 Validar Nivel 4"):
        if input_n4.strip() == "110":
            st.success("✅ ¡CANAL CUÁNTICO ESTABLECIDO!")
            st.session_state.nivel = 5
            st.rerun()
        else:
            st.error("❌ Secuencia binaria errónea.")

# ==========================================
# 🖼️ NIVEL 5: ESTEGANOGRAFÍA Y MÚSICA
# ==========================================
elif st.session_state.nivel == 5:
    st.subheader("🏁 Nivel 5: Extracción Esteganográfica")
    st.write("Carga la foto `.png` interceptada para desencriptar las instrucciones finales.")
    
    subir_foto = st.file_uploader("Subir Foto Secreta (.png)", type=["png"])
    input_clave_final = st.text_input("Clave Cuántica (Nivel 4):", value="110")
    
    if st.button("🎉 REVELAR FINAL"):
        if subir_foto is not None and input_clave_final == "110":
            st.balloons()
            st.success("💖 ¡SISTEMA TOTALMENTE HACKEADO!")
            st.markdown("### 💌 Mensaje Secreto:")
            st.write("¡Completaste la misión! Tu premio real te espera guardado en el cajón de la mesa de noche. 🎁")
            
            st.divider()
            st.subheader("🎧 Transmisión de Audio Secreta:")
            
            link_youtube = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" # Tu enlace de YouTube
            
            if qrcode:
                qr = qrcode.make(link_youtube)
                buf = io.BytesIO()
                qr.save(buf)
                st.image(buf.getvalue(), caption="📲 Escanea para escuchar nuestra canción", width=220)
            
            st.link_button("▶️ Escuchar transmisión directa en YouTube", link_youtube)
        else:
            st.error("⚠️ Sube la foto `.png` para procesar los píxeles.")
