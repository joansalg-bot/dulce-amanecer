import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Desayunos Sorpresa",
    page_icon="🎁",
    layout="centered"
)

# Título principal
st.title("🎁 Desayunos Sorpresa")
st.subheader("Sorprende a esa persona especial ❤️")

st.write("Elige tu desayuno y personalízalo a tu gusto.")

# -----------------------------
# SELECCIÓN DEL DESAYUNO
# -----------------------------

desayuno = st.selectbox(
    "Selecciona tu desayuno:",
    [
        "Desayuno Dulce",
        "Desayuno Salado",
        "Desayuno Mixto"
    ]
)

# Precios
precios = {
    "Desayuno Dulce": 70000,
    "Desayuno Salado": 75000,
    "Desayuno Mixto": 89000
}

precio = precios[desayuno]

st.write(f"### Precio base: ${precio:,.0f}")

# -----------------------------
# PERSONALIZACIÓN
# -----------------------------

st.write("### 🍓 Personaliza tu desayuno")

if desayuno == "Desayuno Dulce":

    opciones = st.multiselect(
        "Escoge tus opciones:",
        [
            "Pancakes",
            "Brownie",
            "Donas",
            "Fresas",
            "Chocolate",
            "Galletas"
        ]
    )

elif desayuno == "Desayuno Salado":

    opciones = st.multiselect(
        "Escoge tus opciones:",
        [
            "Sándwich",
            "Huevo",
            "Arepa",
            "Fruta",
            "Queso",
            "Jamón"
        ]
    )

else:

    opciones = st.multiselect(
        "Escoge tus opciones:",
        [
            "Sándwich",
            "Huevo",
            "Arepa",
            "Fruta",
            "Pancakes",
            "Brownie",
            "Fresas",
            "Donas"
        ]
    )

# -----------------------------
# DATOS DEL PEDIDO
# -----------------------------

st.write("### 💌 Datos del pedido")

nombre = st.text_input("Nombre de la persona que recibirá el desayuno")

mensaje = st.text_area(
    "Mensaje para la persona:",
    placeholder="Escribe aquí tu mensaje..."
)

direccion = st.text_input("Dirección de entrega")

# -----------------------------
# RESUMEN
# -----------------------------

st.write("### 🛒 Resumen del pedido")

st.write(f"**Desayuno:** {desayuno}")
st.write(f"**Precio:** ${precio:,.0f}")

if opciones:
    st.write("**Opciones seleccionadas:**")

    for opcion in opciones:
        st.write(f"✓ {opcion}")

# -----------------------------
# BOTÓN
# -----------------------------

if st.button("🎁 REALIZAR PEDIDO"):

    if nombre and direccion:

        st.success("¡Pedido preparado! 🎉")

        st.write(f"**Destinatario:** {nombre}")
        st.write(f"**Dirección:** {direccion}")
        st.write(f"**Mensaje:** {mensaje}")

    else:

        st.warning(
            "Por favor, completa el nombre y la dirección de entrega."
        )