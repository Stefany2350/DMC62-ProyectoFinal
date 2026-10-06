import streamlit as st
import numpy as np

# ==========================================
# BARRA LATERAL
# ==========================================

st.sidebar.markdown("""
    <div class="sidebar-custom-title">
        <h2>🎛️ Panel de Navegación</h2>
    </div>
""", unsafe_allow_html=True)


modulos = st.sidebar.selectbox(
    "Seleccione la sección a consultar",
    [
        "Modulo 1: Home",
        "Modulo 2: Carga del Dataset",
           ]
)

# ==========================================
# HOME
# ==========================================

if modulos == "Modulo 1: Home":

    st.sidebar.markdown("---")

    st.sidebar.image(
        "image_home.png",
        use_container_width=True
    )

    st.markdown("""
        <div class="custom-data-title">
            <h1>Aplicación interactiva en Streamlit orientada al Análisis Exploratorio de Datos (EDA) </h1>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    ### 💡 Objeto de Análisis

    El objetivo principal es analizar los factores que influyen en la renovación de una 
    póliza de seguro, utilizando la variable renewal como variable objetivo. Este 
    conjunto de datos permite aplicar análisis exploratorio, visualización de datos y 
    modelos predictivos para identificar patrones de clientes que renuevan o no su 
    seguro""")

    st.markdown("""
    ### 📝 Datos del Autor

    * Nombre completo: Stefany Salazar Espinoza 
    * Curso / Especialización: Especialización en Python for Analytics  
    * Año: 2026 """)

    st.markdown("""
    ### 👨‍🏫 Explicación del Dataset

     Este dataset InsuranceCompany.csv contiene información histórica de clientes de 
    una compañía de seguros. Incluye variables demográficas, económicas, historial de 
    pagos, comportamiento de morosidad, canal de captación, tipo de residencia, valor 
    de la prima y puntaje de evaluación del cliente

    ### 🛠️ Tecnologías utilizadas  """) 
    
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.image("Python_logo.png", width=220)

    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.image("GitHub.png", width=220)

    col3, col4 = st.columns(2)

    with col3:
        st.image("Numpy.png", width=220)

    with col4:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.image("streamlit.jpg", width=220)
    

    












