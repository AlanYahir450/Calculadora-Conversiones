# Calculadora_web.py
import streamlit as st

st.set_page_config(page_title="⚡ Calculadora de Conversiones by Alan ⚡",
                   layout="centered",
                   initial_sidebar_state="collapsed")

# --- Estilo "gamer" oscuro ---
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #0b0f1a 0%, #001021 50%, #061021 100%);
        color: #cfe8ff;
        font-family: "Segoe UI", Roboto, Arial, sans-serif;
    }
    .stButton>button {
        background: linear-gradient(90deg,#7c4dff,#00d4ff);
        color: black;
        font-weight: 700;
        border-radius: 8px;
        padding: 8px 14px;
    }
    .title {
        text-align: center;
        font-size:32px;
        font-weight:800;
        color: #7c4dff;
        text-shadow: 0 0 8px rgba(124,77,255,0.6);
    }
    .subtitle {
        color: #9fd6ff;
        text-align:center;
        margin-bottom:18px;
    }
    .card {
        background: rgba(255,255,255,0.03);
        padding:16px;
        border-radius:12px;
        border: 1px solid rgba(124,77,255,0.12);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Animated / stylized title
st.markdown('<div class="title">⚡ Calculadora de Conversiones by Alan ⚡</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Interfaz gamer • Selecciona categoría y convierte</div>', unsafe_allow_html=True)

# Helper: conversion function using factor dictionaries (base units)
def convert_using_factors(value, origen_factor, destino_factor):
    base = value * origen_factor
    return base / destino_factor

# Menú principal
categorias = [
    "Longitud",
    "Masa",
    "Velocidad y Aceleración",
    "Fuerza",
    "Temperatura",
    "Tiempo"
]
categoria = st.selectbox("Selecciona categoría", categorias)

st.markdown("<div class='card'>", unsafe_allow_html=True)

# --- LONGITUD (base: metro) ---
if categoria == "Longitud":
    unidades = {
        "Milímetro (mm)": 0.001,
        "Centímetro (cm)": 0.01,
        "Metro (m)": 1,
        "Kilómetro (km)": 1000,
        "Pulgada (in)": 0.0254,
        "Pie (ft)": 0.3048,
        "Yarda (yd)": 0.9144,
        "Milla (mi)": 1609.34
    }

    origen = st.selectbox("Unidad origen", list(unidades.keys()))
    destino = st.selectbox("Unidad destino", list(unidades.keys()))
    valor = st.number_input(f"Valor en {origen}", value=1.0, format="%.6f")

    if st.button("Convertir"):
        resultado = convert_using_factors(valor, unidades[origen], unidades[destino])
        st.success(f"{valor} → {resultado:.6f} ({destino})")

# --- MASA (base: gramo) ---
elif categoria == "Masa":
    unidades = {
        "Miligramo (mg)": 0.001,
        "Gramo (g)": 1,
        "Kilogramo (kg)": 1000,
        "Tonelada métrica (t)": 1_000_000,
        "Onza (oz)": 28.3495,
        "Libra (lb)": 453.592,
        "Tonelada corta (short ton)": 907_185,
        "Tonelada larga (long ton)": 1_016_047
    }

    origen = st.selectbox("Unidad origen", list(unidades.keys()))
    destino = st.selectbox("Unidad destino", list(unidades.keys()))
    valor = st.number_input(f"Valor en {origen}", value=1.0, format="%.6f")

    if st.button("Convertir"):
        resultado = convert_using_factors(valor, unidades[origen], unidades[destino])
        st.success(f"{valor} → {resultado:.6f} ({destino})")

# --- VELOCIDAD y ACELERACIÓN ---
elif categoria == "Velocidad y Aceleración":
    sub = st.radio("Tipo", ["Velocidad", "Aceleración"])
    if sub == "Velocidad":
        unidades = {
            "Metro/segundo (m/s)": 1,
            "Kilómetro/hora (km/h)": 0.277778,
            "Milla/hora (mph)": 0.44704,
            "Nudo (kt)": 0.514444,
            "Pie/segundo (ft/s)": 0.3048
        }
    else:  # Aceleración (base m/s^2)
        unidades = {
            "Metro/segundo² (m/s²)": 1,
            "Kilómetro/hora² (km/h²)": 0.00007716,
            "Pie/segundo² (ft/s²)": 0.3048,
            "Gal (cm/s²)": 0.01,
            "g (gravedad)": 9.80665
        }

    origen = st.selectbox("Unidad origen", list(unidades.keys()))
    destino = st.selectbox("Unidad destino", list(unidades.keys()))
    valor = st.number_input(f"Valor en {origen}", value=1.0, format="%.6f")

    if st.button("Convertir"):
        resultado = convert_using_factors(valor, unidades[origen], unidades[destino])
        st.success(f"{valor} → {resultado:.6f} ({destino})")

# --- FUERZA ---
elif categoria == "Fuerza":
    unidades = {
        "Newton (N)": 1,
        "Kilonewton (kN)": 1000,
        "Dina (dyn)": 1e-5,
        "Kilogramo-fuerza (kgf)": 9.80665,
        "Libra-fuerza (lbf)": 4.44822,
        "Onza-fuerza (ozf)": 0.2780139
    }

    origen = st.selectbox("Unidad origen", list(unidades.keys()))
    destino = st.selectbox("Unidad destino", list(unidades.keys()))
    valor = st.number_input(f"Valor en {origen}", value=1.0, format="%.6f")

    if st.button("Convertir"):
        resultado = convert_using_factors(valor, unidades[origen], unidades[destino])
        st.success(f"{valor} → {resultado:.6f} ({destino})")

# --- TEMPERATURA (usa fórmulas) ---
elif categoria == "Temperatura":
    opciones = {
        "Celsius (°C)": "C",
        "Fahrenheit (°F)": "F",
        "Kelvin (K)": "K",
        "Rankine (°R)": "R"
    }
    origen_label = st.selectbox("Unidad origen", list(opciones.keys()))
    destino_label = st.selectbox("Unidad destino", list(opciones.keys()))
    valor = st.number_input(f"Valor en {origen_label}", value=0.0, format="%.6f")

    def to_kelvin(v, code):
        if code == "C":
            return v + 273.15
        if code == "F":
            return (v - 32) * 5/9 + 273.15
        if code == "K":
            return v
        if code == "R":
            return v * 5/9

    def from_kelvin(vk, code):
        if code == "C":
            return vk - 273.15
        if code == "F":
            return (vk - 273.15) * 9/5 + 32
        if code == "K":
            return vk
        if code == "R":
            return vk * 9/5

    origen = opciones[origen_label]
    destino = opciones[destino_label]

    if st.button("Convertir"):
        try:
            vk = to_kelvin(valor, origen)
            resultado = from_kelvin(vk, destino)
            st.success(f"{valor} {origen_label} → {resultado:.6f} {destino_label}")
        except Exception as e:
            st.error("Error en conversión de temperatura.")

# --- TIEMPO ---
elif categoria == "Tiempo":
    unidades = {
        "Segundo (s)": 1,
        "Minuto (min)": 60,
        "Hora (h)": 3600,
        "Día": 86400,
        "Semana": 604800,
        "Mes (30 días)": 2592000,
        "Año (365 días)": 31536000
    }

    origen = st.selectbox("Unidad origen", list(unidades.keys()))
    destino = st.selectbox("Unidad destino", list(unidades.keys()))
    valor = st.number_input(f"Valor en {origen}", value=1.0, format="%.6f")

    if st.button("Convertir"):
        resultado = convert_using_factors(valor, unidades[origen], unidades[destino])
        st.success(f"{valor} → {resultado:.6f} ({destino})")

st.markdown("</div>", unsafe_allow_html=True)

# Footer pequeño
st.markdown(
    """
    <div style="text-align:center;color:#6fb3ff;margin-top:14px;">
    Hecha por Alan • ¡Preséntala con orgullo! 🎮
    </div>
    """,
    unsafe_allow_html=True
)
