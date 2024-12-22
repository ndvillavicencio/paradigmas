import streamlit as st
from datetime import datetime

st.title('Mi Primera Aplicación en Streamlit')
st.title('Nixon Villavicencio')

# Agregar un input box en la barra lateral para ingresar la edad
edad = st.sidebar.slider(
    'Ingresa tu edad:',
    0, 100, 25
)

# Agregar un input de texto en la barra lateral para nombres y apellidos
nombre = st.sidebar.text_input('Ingresa tu nombre:')
apellido = st.sidebar.text_input('Ingresa tu apellido:')

# Agregar un slider en la barra lateral para seleccionar un mes
mes = st.sidebar.slider(
    'Selecciona un mes:',
    1, 12, 6
)

# Agregar opciones de género usando radio buttons
genero = st.sidebar.radio(
    'Selecciona tu género:',
    ('Masculino', 'Femenino', 'Otro')
)

# Agregar un selectbox en la barra lateral para seleccionar un país
pais = st.sidebar.selectbox(
    'Selecciona tu país:',
    ("Ecuador", "Bolivia", "Brasil", "Chile", "Colombia", "Argentina", "Guyana", "Paraguay", "Perú", "Surinam", "Uruguay", "Venezuela")
)

# Permitir a los usuarios cargar un archivo
archivo = st.sidebar.file_uploader('Cargar un archivo', type=['csv', 'txt', 'xlsx'])

# Agregar un selector de fecha en la barra lateral
fecha = st.sidebar.date_input('Selecciona una fecha:', datetime.now())

# Agregar un selector de hora en la barra lateral
hora = st.sidebar.time_input('Selecciona una hora:', datetime.now())

# Agregar un checkbox en la barra lateral para aceptar términos y condiciones
aceptar_terminos = st.sidebar.checkbox('Acepto los términos y condiciones')

# Agregar un botón para enviar la información ingresada
if st.sidebar.button('Enviar'):
    # Mostrar la edad, nombre, apellido, mes, género, país, fecha, hora y aceptación de términos en la página principal
    st.write('Tu edad es:', edad)
    st.write('Tu nombre es:', nombre)
    st.write('Tu apellido es:', apellido)
    st.write('El mes seleccionado es:', mes)
    st.write('Tu género es:', genero)
    st.write('Tu país es:', pais)
    st.write('La fecha seleccionada es:', fecha)
    st.write('La hora seleccionada es:', hora)
    st.write('Aceptaste los términos y condiciones:', aceptar_terminos)
    
    # Mostrar información del archivo cargado
    if archivo is not None:
        st.write('Nombre del archivo cargado:', archivo.name)
        st.write('Tipo de archivo:', archivo.type)
        st.write('Tamaño del archivo:', archivo.size, 'bytes')