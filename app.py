import streamlit as st
import base64
import io
import os
from PIL import Image
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


# Cargamos el fondo y lo aplicamos realmente a la aplicación.
# Antes se estaba codificando la imagen, pero nunca se utilizaba
# en el CSS, por eso Streamlit mostraba el fondo blanco.
if os.path.exists("fondo.png"):
    fondo = cargar_fondo("fondo.png")

    st.markdown(
        f"""
        <style>
        /* Fondo general de la aplicación */
        [data-testid="stAppViewContainer"] {{
            background-image:
                linear-gradient(rgba(255, 248, 245, 0.78), rgba(255, 248, 245, 0.78)),
                url("data:image/png;base64,{fondo}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        /* Mantener transparente el contenedor principal para que se vea el fondo */
        [data-testid="stAppViewContainer"] > .main {{
            background: transparent;
        }}

        /* Barra superior transparente */
        [data-testid="stHeader"] {{
            background: rgba(255, 255, 255, 0.15);
        }}

        /* Contenido con una ligera transparencia para conservar la lectura */
        [data-testid="stMainBlockContainer"] {{
            background: rgba(255, 255, 255, 0.25);
            border-radius: 20px;
            padding-top: 2rem;
            padding-bottom: 2rem;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.warning(
        "⚠️ No se encontró el archivo fondo.png. "
        "Colócalo en la misma carpeta que este archivo de Streamlit."
    )


# ============================================================
# PORTADA
# ============================================================

st.title("🌅 Dulce Amanecer")

st.subheader(
    "Desayunos que convierten momentos en recuerdos ❤️"
)

st.info(
    "✨ Base decorada + 🧁 Toppings + 🌷 Decoración a tu gusto + "
    "💌 Tarjeta personalizada + 🎁 Toppings especiales (opcional) + "
    "🥤 Bebida (opcional).\n\n"
    "💖 Si gustas personalizar aún más tu detalle e incluir otros detalles, "
    "puedes hacerlo al interno cuando realices tu pedido.\n\n"
    "🌸 ¡Queremos ayudarte a crear una sorpresa única y especial!"
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
        "Puedes agregar 6 productos de tu elección + una o varias bebidas."
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

st.subheader("🥤 Elige tus bebidas")

bebidas_seleccionadas = st.multiselect(
    "Puedes elegir una o varias bebidas:",
    [
        "Milo frío o caliente",
        "Choco Listo",
        "Jugo de naranja",
        "Café en leche"
    ],
    key="bebidas"
)


# ============================================================
# PRECIO DE LAS BEBIDAS
# ============================================================

precio_bebida = sum(
    bebidas[bebida_seleccionada]
    for bebida_seleccionada in bebidas_seleccionadas
)


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


# ----------------------------------------------------
# IDEAS DE DECORACIÓN SEGÚN LA BASE
# ----------------------------------------------------

idea_seleccionada = None

ideas_por_base = {
    "Bandeja Estándar": ("estandar", 15),
    "Caja de Madera - Grande": ("cajagrande", 4),
    "Caja de Madera - Mediana": ("cajamediana", 3),
    "Caja de Madera - Pequeña": ("cajapequeña", 7),
    "Caja Octagonal - Grande": ("cajaoctogonalgrande", 3),
    "Caja Octagonal - Mediana": ("cajaoctagonalmediana", 3),
    "Caja de Madera con Patas - Grande": ("cajagrandeconpatas", 4),
    "Caja de Madera con Patas - Mediana": ("cajamedianaconpatas", 3),
    "Caja de Madera con Patas - Pequeña": ("cajaconpataspequeña", 2)
}

clave_ideas = None
nombre_idea = None

if base_sorpresa == "Bandeja Estándar":
    clave_ideas = "Bandeja Estándar"
elif base_sorpresa == "Caja de Madera":
    clave_ideas = f"Caja de Madera - {tamano}"
elif base_sorpresa == "Caja Octagonal":
    clave_ideas = f"Caja Octagonal - {tamano}"
elif base_sorpresa == "Caja de Madera con Patas":
    clave_ideas = f"Caja de Madera con Patas - {tamano}"

if clave_ideas in ideas_por_base:

    nombre_idea, cantidad_ideas = ideas_por_base[clave_ideas]

    st.write("---")

    # Cada presentación tiene su propio botón para mostrar sus ideas.
    clave_mostrar = f"mostrar_ideas_{nombre_idea}"

    if clave_mostrar not in st.session_state:
        st.session_state[clave_mostrar] = False

    if st.button("🌷 VER IDEAS", key=f"ver_ideas_{nombre_idea}"):
        st.session_state[clave_mostrar] = True

    if st.session_state[clave_mostrar]:

        st.subheader("🌸 Ideas de decoración")

        st.write(
            "Estos son algunos de nuestros hermosos detalles. "
            "La decoración la escoges tú a tu gusto 💕"
        )

        st.markdown(
            "### 💕 Escoge una de las ideas para hacer la base de tu desayuno"
        )

        imagenes_ideas = [
            f"{nombre_idea}{i}.jfif" for i in range(1, cantidad_ideas + 1)
        ]

        # Mostrar las ideas numeradas en una cuadrícula de 3 columnas.
        for fila in range(0, len(imagenes_ideas), 3):

            columnas = st.columns(3)

            for posicion, columna in enumerate(columnas):

                indice = fila + posicion

                if indice < len(imagenes_ideas):

                    numero = indice + 1
                    ruta = imagenes_ideas[indice]

                    with columna:
                        st.markdown(f"**Idea {numero}**")
                        st.image(ruta, use_container_width=True)

        # El cliente puede escoger una sola idea.
        opciones_ideas = [
            f"Idea {i}" for i in range(1, cantidad_ideas + 1)
        ]

        idea_seleccionada = st.selectbox(
            "🌷 Escoge una de las ideas para hacer la base de tu desayuno:",
            opciones_ideas,
            key=f"idea_{nombre_idea}"
        )

        st.success(
            f"💕 Has escogido la **{idea_seleccionada}** como base "
            "de tu desayuno."
        )

        if st.button("✖ OCULTAR IDEAS", key=f"ocultar_ideas_{nombre_idea}"):
            st.session_state[clave_mostrar] = False
            st.rerun()


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

st.warning(
    "⏰ Recuerda hacer tu pedido mínimo con 2 días de anticipación "
    "para verificar disponibilidad."
)

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

hora_entrega = st.time_input(
    "🕐 Selecciona la hora de entrega:",
    value=time(8, 0),
    step=timedelta(minutes=30),
    key="hora_entrega"
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
    f"**🥤 Bebidas:** {', '.join(bebidas_seleccionadas) if bebidas_seleccionadas else 'Ninguna'}"
)

st.write(
    f"**📅 Fecha de entrega:** {fecha_entrega.strftime('%d/%m/%Y')}"
)

st.write(
    f"**🕐 Hora de entrega:** {hora_entrega.strftime('%I:%M %p')}"
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
# BOTÓN REALIZAR PAGO
# ============================================================

if "mostrar_pago" not in st.session_state:
    st.session_state.mostrar_pago = False

if st.button(
    "💳 REALIZAR PAGO",
    use_container_width=True
):
    # IMPORTANTE:
    # El pago puede iniciarse aunque el cliente todavía no haya
    # completado todos los datos del pedido.
    st.session_state.mostrar_pago = True


# ============================================================
# OPCIONES DE PAGO
# ============================================================

if st.session_state.mostrar_pago:

    st.write("---")
    st.header("💳 Selecciona cómo deseas pagar")

    st.info(
        "Puedes realizar el pago de la base ahora o pagar "
        "el valor total de tu pedido."
    )

    opcion_pago = st.radio(
        "Elige una opción:",
        [
            f"💰 Pago base — ${precio_base:,.0f}",
            f"💳 Pago total — ${total:,.0f}"
        ],
        key="opcion_pago"
    )

    if opcion_pago.startswith("💰 Pago base"):
        valor_a_pagar = precio_base
        tipo_pago = "Pago base"
    else:
        valor_a_pagar = total
        tipo_pago = "Pago total"

    st.success(
        f"Has seleccionado **{tipo_pago}**. "
        f"Valor a pagar: **${valor_a_pagar:,.0f}**"
    )

    st.subheader("📱 Realiza tu pago")

    st.write(
        "Escanea el siguiente código QR para realizar el pago:"
    )

    ruta_qr = "QR.jfif"

    if os.path.exists(ruta_qr):
        st.image(
            ruta_qr,
            caption="Código QR de pago",
            use_container_width=False,
            width=350
        )
    else:
        st.error(
            "⚠️ No se encontró QR.jfif. "
            "Coloca la imagen QR.jfif en la misma carpeta "
            "que este archivo de Streamlit."
        )

    st.markdown(
        """
        ### 🔑 Pago mediante Llave

        **3143564845**
        """
    )

    st.write(
        f"💵 **Valor seleccionado para pagar: ${valor_a_pagar:,.0f}**"
    )

    st.caption(
        "El pago base corresponde únicamente al precio de la "
        "presentación seleccionada. El pago total corresponde "
        "al valor completo del pedido."
    )

    # ========================================================
    # ENVÍO DEL COMPROBANTE Y FOTOS POR WHATSAPP
    # ========================================================

    st.write("---")
    st.header("📲 Envía tu comprobante y fotos")

    st.info(
        "Después de realizar el pago, envía por WhatsApp tu "
        "comprobante de pago. Si deseas una tarjeta especial con "
        "mensaje, también puedes enviar 2 o 3 fotos. 💕 "
        "Las fotos son opcionales."
    )

    productos_dulces_texto = (
        ", ".join(productos_dulces_seleccionados)
        if productos_dulces_seleccionados else "Ninguno"
    )

    productos_salados_texto = (
        ", ".join(productos_salados_seleccionados)
        if productos_salados_seleccionados else "Ninguno"
    )

    toppings_texto = (
        ", ".join(toppings_especiales_seleccionados)
        if toppings_especiales_seleccionados else "Ninguno"
    )

    frutas_texto = (
        ", ".join(frutas_seleccionadas)
        if frutas_seleccionadas else "No aplica"
    )

    idea_texto = idea_seleccionada if idea_seleccionada else "No seleccionada"

    mensaje_whatsapp = f"""Hola, Dulce Amanecer 🌅💕

Acabo de realizar un pedido y voy a enviar el comprobante de pago por este medio.

📋 DATOS DEL PEDIDO

👤 Persona que recibe: {nombre if nombre else "No especificado"}
📱 Tipo de desayuno: {desayuno}

🎁 Presentación: {base_sorpresa}
📦 Tamaño: {tamano}
🌷 Idea de decoración: {idea_texto}

🍫 Productos dulces:
{productos_dulces_texto}

🍗 Productos salados:
{productos_salados_texto}

🍓 Frutas:
{frutas_texto}

🥤 Bebidas: {", ".join(bebidas_seleccionadas) if bebidas_seleccionadas else "Ninguna"}

✨ Toppings especiales:
{toppings_texto}

💌 Mensaje para la persona:
{mensaje if mensaje else "Sin mensaje"}

📅 Fecha de entrega: {fecha_entrega.strftime("%d/%m/%Y")}
🕐 Hora de entrega: {hora_entrega.strftime("%I:%M %p")}
📍 Dirección de entrega: {direccion if direccion else "No especificada"}

💰 Tipo de pago: {tipo_pago}
💵 Valor seleccionado para pagar: ${valor_a_pagar:,.0f}
💰 Valor total del pedido: ${total:,.0f}

📸 Voy a adjuntar el comprobante de pago y, si corresponde,
las fotos para la tarjeta especial.

Gracias 💕
"""

st.link_button(
    "📲 ENVIAR COMPROBANTE POR WHATSAPP",
    "https://wa.me/qr/LUMZA6QOLXY4M1",
    use_container_width=True
)

    


# ============================================================
# PIE DE PÁGINA
# ============================================================
st.write("---")

st.markdown(
    "❤️ **Dulce Amanecer** — "
    "Desayunos que convierten momentos en recuerdos."
)
