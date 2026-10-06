import streamlit as st
import numpy as np
import pandas as pd

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
        "Home",
        "Carga del Dataset",
        "Análisis Exploratorio de Datos",
           ]
)

# ==========================================
# MODULO 1: HOME
# ==========================================

if modulos == "Home":

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
    * Curso: Especialización en Python for Analytics  
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


# ==========================================
# MODULO 2: CARGA DEL DATASET
# ==========================================

elif modulos == "Carga del Dataset":

    st.title("Análisis Exploratorio de Datos - Compañía de Seguros")

    st.write(
        "Carga el archivo para iniciar "
        "el Análisis Exploratorio de Datos (EDA)."
    )

    # ==========================================
    # CARGA DEL ARCHIVO
    # ==========================================

    archivo = st.file_uploader(
        "Selecciona el archivo CSV",
        type=["csv"],
        help="Carga el archivo"
    )

    # ==========================================
    # VALIDACIÓN Y LECTURA DEL DATASET
    # ==========================================

    if archivo is not None:

        try:
            # Leer el archivo CSV
            df = pd.read_csv(archivo)

            # Validar que el dataset tenga información
            if df.empty:

                st.warning(
                    "⚠️ El archivo fue cargado, "
                    "pero el dataset no contiene registros."
                )

            else:

                # Mensaje de carga exitosa
                st.success(
                    f"✅ El archivo **{archivo.name}** "
                    "fue cargado correctamente."
                )

                # ==========================================
                # DIMENSIONES DEL DATASET
                # ==========================================

                filas, columnas = df.shape

                st.subheader("Dimensiones del Dataset")

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "Filas",
                        f"{filas:,}"
                    )

                with col2:
                    st.metric(
                        "Columnas",
                        f"{columnas:,}"
                    )

                # ==========================================
                # VISTA PREVIA DEL DATASET
                # ==========================================

                st.subheader("Vista previa del Dataset")

                st.write("Primeras 5 filas del dataset:")

                st.dataframe(
                    df.head(),
                    use_container_width=True
                )

        except Exception as e:

            st.error(
                f"❌ Ocurrió un error al cargar el archivo: {e}"
            )

    else:

        # ==========================================
        # MENSAJE CUANDO NO SE HA CARGADO ARCHIVO
        # ==========================================

        st.info(
            "ℹ️ Debes cargar el archivo "
            "para continuar con el análisis."
        )

# ==========================================
# MODULO 3: Análisis Exploratorio de Datos
# ==========================================

elif modulos == "Análisis Exploratorio de Datos":

    st.subheader("Item 1: Información general del dataset")

    st.markdown("""
    En este ítem se presenta un resumen de la estructura del dataset,
    considerando el número de filas, columnas, valores no nulos,
    tipos de datos y uso de memoria.
    """)

    # ==========================================================
    # 1. INFORMACIÓN GENERAL - .info()
    # ==========================================================

    st.markdown("### 🔹 1. Resumen de la información del dataset")

    # Ejecutar .info() para obtener la información solicitada
    buffer = io.StringIO()
    df.info(buf=buffer)

    # Información general
    memoria_mb = df.memory_usage(deep=True).sum() / (1024 ** 2)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Número de filas",
            f"{df.shape[0]:,}"
        )

    with col2:
        st.metric(
            "Número de columnas",
            f"{df.shape[1]:,}"
        )

    with col3:
        st.metric(
            "Uso de memoria",
            f"{memoria_mb:.2f} MB"
        )

    st.markdown("#### 📊 Detalle por columna")

    # Resumen equivalente a la información proporcionada por .info()
    resumen_info = pd.DataFrame({
        "Columna": df.columns,
        "Valores no nulos": df.notna().sum(),
        "Valores nulos": df.isna().sum(),
        "Tipo de dato": df.dtypes.astype(str)
    }).reset_index(drop=True)

    st.dataframe(
        resumen_info,
        use_container_width=True,
        hide_index=True
    )


    # ==========================================================
    # 2. TIPOS DE DATOS
    # ==========================================================

    st.markdown("### 🔹 2. Tipos de datos")

    tipos_datos = (
        df.dtypes
        .astype(str)
        .value_counts()
        .reset_index()
    )

    tipos_datos.columns = ["Tipo de dato", "Cantidad de columnas"]

    st.dataframe(
        tipos_datos,
        use_container_width=True,
        hide_index=True
    )


    # ==========================================================
    # 3. CONTEO DE VALORES NULOS
    # ==========================================================

    st.markdown("### 🔹 3. Conteo de valores nulos")

    nulos = (
        df.isnull()
        .sum()
        .reset_index()
    )

    nulos.columns = ["Columna", "Valores nulos"]

    st.dataframe(
        nulos,
        use_container_width=True,
        hide_index=True
    )

    # Mensaje general
    total_nulos = df.isnull().sum().sum()

    if total_nulos == 0:
        st.success("✅ El dataset no contiene valores nulos.")
    else:
        st.warning(
            f"⚠️ El dataset contiene {total_nulos:,} valores nulos."
        )

