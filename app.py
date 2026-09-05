import streamlit as st
import base64
from datetime import date, time, timedelta

# ============================================================
# CONFIGURACIÓN
# ============================================================

st.set_page_config(
    page_title="Dulce Amanecer",
    page_icon="🌅",
    layout="wide"
)

# ============================================================
# DISPONIBILIDAD DE DESAYUNOS
# ============================================================
# Por ahora hay 3 cupos máximos por día.
# Esta primera versión mantiene los cupos durante la sesión.
# Después conectaremos esto a una base de datos para que todos
# los clientes compartan los mismos cupos.

MAX_CUPOS_POR_DIA = 3

if "cupos_por_dia" not in st.session_state:
    st.session_state.cupos_por_dia = {}

def cupos_disponibles(fecha):
    fecha_texto = fecha.isoformat()
    usados = st.session_state.cupos_por_dia.get(fecha_texto, 0)
    return MAX_CUPOS_POR_DIA - usados



# ============================================================
# IMAGEN DE FONDO
# ============================================================

def cargar_fondo(ruta):
    with open(ruta, "rb") as archivo:
        return base64.b64encode(archivo.read()).decode()


fondo = cargar_fondo("fondo.png")


# ============================================================
# DISEÑO
# ============================================================

st.markdown(
    f"""
    <style>

    .stApp {{
        background-image:
            linear-gradient(
                rgba(255, 240, 242, 0.15),
                rgba(255, 240, 242, 0.15)
            ),
            url("data:image/png;base64,{fondo}");

        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    #MainMenu {{
        visibility: hidden;
    }}

    footer {{
        visibility: hidden;
    }}

    .block-container {{
        max-width: 1050px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }}

    /* ========================================================
       TEXTOS
       ======================================================== */

    h1,
    h2,
    h3,
    h4,
    h5,
    h6 {{
        color: #111111 !important;
    }}

    .stApp p,
    .stApp span {{
        color: #111111;
    }}

    .stTextInput label,
    .stTextArea label,
    .stSelectbox label,
    .stMultiSelect label {{
        color: #111111 !important;
        font-weight: 600;
    }}

    /* ========================================================
       CAMPOS
       ======================================================== */

    .stTextInput input,
    .stTextArea textarea {{
        color: #111111 !important;
        background-color: rgba(255, 255, 255, 0.92) !important;
        border-radius: 12px;
    }}

    .stSelectbox div[data-baseweb="select"],
    .stMultiSelect div[data-baseweb="select"] {{
        background-color: rgba(255, 255, 255, 0.92);
        border-radius: 12px;
    }}

    .stSelectbox div[data-baseweb="select"] *,
    .stMultiSelect div[data-baseweb="select"] * {{
        color: #111111 !important;
    }}

    /* ========================================================
       BOTONES
       ======================================================== */

    .stButton > button {{
        background-color: #e88aa5;
        color: #111111 !important;
        border: none;
        border-radius: 15px;
        padding: 0.7rem 1rem;
        font-size: 18px;
        font-weight: bold;
        box-shadow: 0 4px 10px rgba(0,0,0,0.25);
    }}

    .stButton > button:hover {{
        background-color: #d96f8f;
        color: #111111 !important;
    }}

    hr {{
        border-color: rgba(0,0,0,0.35);
    }}

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# PORTADA
# ============================================================

st.title("🌅 Dulce Amanecer")

st.subheader(
    "Desayunos que convierten momentos en recuerdos ❤️"
)

st.write(
    "🎁 Sorprende a esa persona especial "
    "con un detalle preparado con amor."
)


# ============================================================
# SELECCIÓN DEL DESAYUNO
# ============================================================

st.write("---")

st.header("🎁 Selecciona tu desayuno")

desayuno = st.selectbox(
    "Elige una opción:",
    [
        "Desayuno Dulce",
        "Desayuno Salado",
        "Desayuno Mixto"
    ]
)


# ============================================================
# EL TIPO DE DESAYUNO NO AFECTA EL PRECIO
# ============================================================

precio_desayuno = 0


# ============================================================
# BASE DE TU SORPRESA
# ============================================================

st.write("---")

st.header("🎀 Base de tu sorpresa")

base_sorpresa = st.selectbox(
    "Elige la presentación de tu sorpresa:",
    [
        "Bandeja Estándar",
        "Caja de Madera",
        "Caja Octagonal",
        "Caja de Madera con Patas"
    ]
)


# ============================================================
# TAMAÑO
# ============================================================

tamano = None


if base_sorpresa == "Caja de Madera":

    tamano = st.selectbox(
        "Elige el tamaño:",
        [
            "Grande",
            "Mediana",
            "Pequeña"
        ]
    )


elif base_sorpresa == "Caja Octagonal":

    tamano = st.selectbox(
        "Elige el tamaño:",
        [
            "Grande",
            "Mediana"
        ]
    )


elif base_sorpresa == "Caja de Madera con Patas":

    tamano = st.selectbox(
        "Elige el tamaño:",
        [
            "Grande",
            "Mediana",
            "Pequeña"
        ]
    )


else:

    tamano = "Estándar"


# ============================================================
# PRECIOS OCULTOS DE LAS BASES
# ============================================================

precios_base = {

    "Bandeja Estándar": {
        "Estándar": 45000
    },

    "Caja de Madera": {
        "Grande": 90000,
        "Mediana": 80000,
        "Pequeña": 70000
    },

    "Caja Octagonal": {
        "Grande": 90000,
        "Mediana": 80000
    },

    "Caja de Madera con Patas": {
        "Grande": 95000,
        "Mediana": 85000,
        "Pequeña": 75000
    }
}


precio_base = precios_base[base_sorpresa][tamano]


# ============================================================
# PRODUCTOS DULCES
# ============================================================

productos_dulces = {

    "Nucitas": 2900,

    "Torta brownie": 4900,

    "Nutella mini": 5900,

    "Choco Break": 4900,

    "Choco Break Cookies": 4900,

    "Choco Break Frutal": 5900,

    "Gomitas surtidas Trululú": 4900,

    "Gomitas surtidas Besties": 3900,

    "Rollito de bocadillo": 3900,

    "Almendras con chocolate": 7900,

    "Moritas de goma": 4900,

    "Masmelos": 3900,

    "Chocolatina con leche": 4900,

    "Caramelo sabor a frutilla": 3900,

    "Super Coco": 4900,

    "Galleta Oreo": 4900,

    "Biscolata galleta": 6990,

    "Galletas de chocolate": 4990,

    "Ponqué Memito": 4900,

    "Gansito": 4900,

    "Chocorramo": 3900,

    "Leche saborizada": 2900,

    "Maní mezcla": 2900,

    "M&M maní/chocolate": 5900,

    "Piazza chocolate o vainilla": 4900,

    "Fruta x3": 5900,

    "Donas": 4900
}


# ============================================================
# PRODUCTOS SALADOS
# ============================================================

productos_salados = {

    "Alitas BBQ": 5900,

    "Croquetas de yuca": 2900,

    "Pinchos de pollo": 6900,

    "Empanadas de queso": 4900,

    "Empanadas de carne": 4900,

    "Milanesa de pollo apanado": 5900,

    "Nuggets": 3900,

    "Huevos rancheros": 4000,

    "Huevos de codorniz": 2000,

    "Salchicha tradicional": 1900,

    "Sándwich de jamón y queso": 6900,

    "Papas a la francesa": 6900,

    "Pan croissant": 2000
}


# ============================================================
# BEBIDAS
# ============================================================

bebidas = {

    "No quiero bebida": 0,

    "Milo frío o caliente": 8900,

    "Choco Listo": 8900,

    "Jugo de naranja": 10900,

    "Café en leche": 7900
}


# ============================================================
# TOPPINGS ESPECIALES
# ============================================================

toppings_especiales = {

    "Sándwich de pollo": 18000,

    "Chocolatina Jumbo grande": 10000,

    "Ferrero Rocher grande": 16000,

    "Ferrero Rocher pequeño": 11000,

    "Nutella": 14900,

    "Cerveza Corona": 5000 ,
  
    "Boung Yourth": 4900,

    "Torta de chocolate": 9000,

    "Rosas decoradas": 29000,

    "Peluche pequeño": 29000

}


# ============================================================
# PERSONALIZACIÓN
# ============================================================

st.write("---")

st.header("🍓 Personaliza tu desayuno")


# ============================================================
# MENSAJE SEGÚN LA BASE
# ============================================================

if base_sorpresa == "Bandeja Estándar":

    st.write(
        "Puedes agregar 6 productos de tu elección + 1 bebida."
    )

else:

    st.write(
        "Puedes agregar los productos que deseas "
        "incluir en tu sorpresa."
    )


# ============================================================
# VARIABLES DE PRODUCTOS
# ============================================================

productos_dulces_seleccionados = []
productos_salados_seleccionados = []


# ============================================================
# DESAYUNO DULCE
# ============================================================

if desayuno == "Desayuno Dulce":

    st.subheader("🍫 Productos dulces")

    productos_dulces_seleccionados = st.multiselect(
        "Elige tus productos dulces:",
        list(productos_dulces.keys()),
        key="dulces"
    )


# ============================================================
# DESAYUNO SALADO
# ============================================================

elif desayuno == "Desayuno Salado":

    st.subheader("🍗 Productos salados")

    productos_salados_seleccionados = st.multiselect(
        "Elige tus productos salados:",
        list(productos_salados.keys()),
        key="salados"
    )


# ============================================================
# DESAYUNO MIXTO
# ============================================================

elif desayuno == "Desayuno Mixto":

    st.subheader("🍫 Productos dulces")

    productos_dulces_seleccionados = st.multiselect(
        "Elige tus productos dulces:",
        list(productos_dulces.keys()),
        key="mixto_dulces"
    )

    st.subheader("🍗 Productos salados")

    productos_salados_seleccionados = st.multiselect(
        "Elige tus productos salados:",
        list(productos_salados.keys()),
        key="mixto_salados"
    )


# ============================================================
# UNIFICAR PRODUCTOS
# ============================================================

productos_seleccionados = (
    productos_dulces_seleccionados
    + productos_salados_seleccionados
)


# ============================================================
# CONTROL DE PRODUCTOS PARA BANDEJA ESTÁNDAR
# ============================================================

if base_sorpresa == "Bandeja Estándar":

    if len(productos_seleccionados) > 6:

        st.error(
            "La Bandeja Estándar permite máximo "
            "6 productos en total."
        )

    elif len(productos_seleccionados) < 6:

        st.info(
            f"Has seleccionado {len(productos_seleccionados)} "
            "de 6 productos."
        )

    else:

        st.success(
            "✓ Has seleccionado los 6 productos."
        )


# ============================================================
# FRUTA X3
# ============================================================

frutas_seleccionadas = []


if "Fruta x3" in productos_seleccionados:

    st.write("---")

    st.subheader("🍓 Selecciona tus 3 frutas")

    frutas = [
        "Banano",
        "Fresas",
        "Kiwi",
        "Papaya",
        "Manzana",
        "Mango"
    ]

    frutas_seleccionadas = st.multiselect(
        "Puedes escoger exactamente 3:",
        frutas,
        key="frutas"
    )

    if len(frutas_seleccionadas) < 3:

        st.warning(
            f"Debes seleccionar 3 frutas. "
            f"Hasta ahora has seleccionado "
            f"{len(frutas_seleccionadas)}."
        )

    elif len(frutas_seleccionadas) > 3:

        st.error(
            "Solo puedes seleccionar 3 frutas."
        )


# ============================================================
# BEBIDA
# ============================================================

st.write("---")

st.subheader("🥤 Elige tu bebida")

bebida = st.selectbox(
    "Selecciona una bebida:",
    [
        "No quiero bebida",
        "Milo frío o caliente",
        "Choco Listo",
        "Jugo de naranja",
        "Café en leche"
    ]
)


# ============================================================
# PRECIO DE LA BEBIDA
# ============================================================

precio_bebida = bebidas[bebida]


# ============================================================
# TOPPINGS ESPECIALES
# ============================================================

st.write("---")

st.subheader("✨ Toppings especiales")

toppings_especiales_seleccionados = st.multiselect(
    "Puedes agregar toppings especiales a tu sorpresa:",
    list(toppings_especiales.keys()),
    key="toppings_especiales"
)


# ============================================================
# CÁLCULO DE PRODUCTOS
# ============================================================

costo_productos = 0


for producto in productos_dulces_seleccionados:

    costo_productos += productos_dulces[producto]


for producto in productos_salados_seleccionados:

    costo_productos += productos_salados[producto]


# ============================================================
# CÁLCULO DE TOPPINGS ESPECIALES
# ============================================================

costo_toppings_especiales = 0


for topping in toppings_especiales_seleccionados:

    costo_toppings_especiales += toppings_especiales[topping]


# ============================================================
# FECHA Y HORA DE ENTREGA
# ============================================================

st.write("---")
st.header("📅 Fecha y hora de entrega")

st.write(
    "Selecciona el día y la hora en que deseas recibir tu desayuno."
)

fecha_minima = date.today()
fecha_maxima = fecha_minima + timedelta(days=90)

fecha_entrega = st.date_input(
    "📅 Selecciona la fecha:",
    value=fecha_minima,
    min_value=fecha_minima,
    max_value=fecha_maxima,
    format="DD/MM/YYYY",
    key="fecha_entrega"
)

cupos = cupos_disponibles(fecha_entrega)

if cupos <= 0:
    st.error(
        "🚫 Esta fecha ya está agotada. Selecciona otro día."
    )
else:
    if cupos == 1:
        st.warning("⚠️ ¡Último cupo disponible para este día!")
    else:
        st.success(
            f"🟢 Hay {cupos} de {MAX_CUPOS_POR_DIA} "
            "cupos disponibles para este día."
        )

    hora_entrega = st.time_input(
        "🕐 Selecciona la hora de entrega:",
        value=time(8, 0),
        step=timedelta(minutes=30),
        key="hora_entrega"
    )

st.info(
    "💡 El cupo se descontará únicamente cuando el pago "
    "sea confirmado. Seleccionar una fecha no reserva "
    "el cupo todavía."
)

# ============================================================
# DATOS DEL PEDIDO
# ============================================================

st.write("---")

st.header("💌 Datos del pedido")

nombre = st.text_input(
    "Nombre de la persona que recibirá el desayuno"
)

mensaje = st.text_area(
    "Mensaje para la persona:",
    placeholder="Escribe aquí tu mensaje..."
)

direccion = st.text_input(
    "Dirección de entrega"
)


# ============================================================
# PRECIO TOTAL
# ============================================================

total = (
    precio_base
    + costo_productos
    + precio_bebida
    + costo_toppings_especiales
)


# ============================================================
# RESUMEN
# ============================================================

st.write("---")

st.header("🛒 Resumen del pedido")

st.write(
    f"**Desayuno:** {desayuno}"
)

st.write(
    f"**Presentación:** {base_sorpresa}"
)

st.write(
    f"**Tamaño:** {tamano}"
)

st.write(
    f"**Bebida:** {bebida}"
)

st.write(
    f"**📅 Fecha de entrega:** {fecha_entrega.strftime('%d/%m/%Y')}"
)

st.write(
    f"**🕐 Hora de entrega:** {hora_entrega.strftime('%I:%M %p')}"
)

st.write(
    f"**Cupos disponibles para ese día:** "
    f"{cupos} de {MAX_CUPOS_POR_DIA}"
)


# ============================================================
# PRODUCTOS DULCES EN EL RESUMEN
# ============================================================

if productos_dulces_seleccionados:

    st.write("**🍫 Productos dulces:**")

    for producto in productos_dulces_seleccionados:

        if producto == "Fruta x3":

            if len(frutas_seleccionadas) == 3:

                st.write(
                    "✓ Fruta x3: "
                    + ", ".join(frutas_seleccionadas)
                )

        else:

            st.write(
                f"✓ {producto}"
            )


# ============================================================
# PRODUCTOS SALADOS EN EL RESUMEN
# ============================================================

if productos_salados_seleccionados:

    st.write("**🍗 Productos salados:**")

    for producto in productos_salados_seleccionados:

        st.write(
            f"✓ {producto}"
        )


# ============================================================
# TOPPINGS ESPECIALES EN EL RESUMEN
# ============================================================

if toppings_especiales_seleccionados:

    st.write("**✨ Toppings especiales:**")

    for topping in toppings_especiales_seleccionados:

        st.write(
            f"✓ {topping}"
        )


# ============================================================
# SI NO HAY PRODUCTOS
# ============================================================

if not productos_seleccionados:

    st.info(
        "Todavía no has seleccionado productos."
    )


# ============================================================
# PRECIO TOTAL
# ============================================================

st.write("---")

st.write(
    f"## 💰 Total: ${total:,.0f}"
)


# ============================================================
# BOTÓN
# ============================================================

if st.button(
    "🎁 REALIZAR PEDIDO",
    use_container_width=True
):

    if not nombre or not direccion:

        st.warning(
            "Por favor, completa el nombre "
            "y la dirección de entrega."
        )

    elif cupos <= 0:

        st.warning(
            "La fecha seleccionada ya no tiene cupos disponibles. "
            "Por favor, selecciona otro día."
        )

    elif (
        base_sorpresa == "Bandeja Estándar"
        and len(productos_seleccionados) != 6
    ):

        st.warning(
            "La Bandeja Estándar debe tener "
            "exactamente 6 productos."
        )

    elif (
        "Fruta x3" in productos_seleccionados
        and len(frutas_seleccionadas) != 3
    ):

        st.warning(
            "Debes seleccionar exactamente "
            "3 frutas para la opción Fruta x3."
        )

    else:

        st.success(
            "🎉 ¡Pedido preparado!"
        )

        st.write(
            f"**Destinatario:** {nombre}"
        )

        st.write(
            f"**Dirección:** {direccion}"
        )

        st.write(
            f"**Desayuno:** {desayuno}"
        )

        st.write(
            f"**Presentación:** {base_sorpresa}"
        )

        st.write(
            f"**Tamaño:** {tamano}"
        )

        st.write(
            f"**Bebida:** {bebida}"
        )

        st.write(
            f"**📅 Fecha de entrega:** "
            f"{fecha_entrega.strftime('%d/%m/%Y')}"
        )

        st.write(
            f"**🕐 Hora de entrega:** "
            f"{hora_entrega.strftime('%I:%M %p')}"
        )

        # ----------------------------------------------------
        # PRODUCTOS DULCES
        # ----------------------------------------------------

        if productos_dulces_seleccionados:

            st.write("**🍫 Productos dulces:**")

            for producto in productos_dulces_seleccionados:

                if producto == "Fruta x3":

                    st.write(
                        "✓ Fruta x3: "
                        + ", ".join(frutas_seleccionadas)
                    )

                else:

                    st.write(
                        f"✓ {producto}"
                    )

        # ----------------------------------------------------
        # PRODUCTOS SALADOS
        # ----------------------------------------------------

        if productos_salados_seleccionados:

            st.write("**🍗 Productos salados:**")

            for producto in productos_salados_seleccionados:

                st.write(
                    f"✓ {producto}"
                )

        # ----------------------------------------------------
        # TOPPINGS ESPECIALES
        # ----------------------------------------------------

        if toppings_especiales_seleccionados:

            st.write("**✨ Toppings especiales:**")

            for topping in toppings_especiales_seleccionados:

                st.write(
                    f"✓ {topping}"
                )

        # ----------------------------------------------------
        # MENSAJE
        # ----------------------------------------------------

        if mensaje:

            st.write(
                f"**Mensaje:** {mensaje}"
            )

        # ----------------------------------------------------
        # TOTAL
        # ----------------------------------------------------

        st.write(
            f"### 💰 Total: ${total:,.0f}"
        )

        st.balloons()

        # IMPORTANTE:
        # El cupo NO se descuenta aquí.
        # Cuando integremos el pago, el descuento de 1 cupo
        # se hará únicamente después de recibir la confirmación
        # de pago exitoso.


# ============================================================
# PIE DE PÁGINA
# ============================================================

st.write("---")

st.markdown(
    "❤️ **Dulce Amanecer** — "
    "Desayunos que convierten momentos en recuerdos."
)
