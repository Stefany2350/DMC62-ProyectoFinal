import streamlit as st
import numpy as np
import pandas as pd
import io

# ==========================================
# CONFIGURACIÓN DE LA PÁGINA
# ==========================================

st.set_page_config(
    page_title="Análisis Exploratorio de Datos",
    layout="wide"
)

# ==========================================
# INICIALIZAR SESSION STATE
# ==========================================

if "df" not in st.session_state:
    st.session_state.df = None

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
            <h1>Aplicación interactiva en Streamlit orientada al Análisis Exploratorio de Datos (EDA)</h1>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    ### 💡 Objeto de Análisis

    El objetivo principal es analizar los factores que influyen en la renovación de una 
    póliza de seguro, utilizando la variable renewal como variable objetivo. Este 
    conjunto de datos permite aplicar análisis exploratorio, visualización de datos y 
    modelos predictivos para identificar patrones de clientes que renuevan o no su 
    seguro.
    """)

    st.markdown("""
    ### 📝 Datos del Autor

    * Nombre completo: Stefany Salazar Espinoza 
    * Curso: Especialización en Python for Analytics  
    * Año: 2026
    """)

    st.markdown("""
    ### 👨‍🏫 Explicación del Dataset

    Este dataset InsuranceCompany.csv contiene información histórica de clientes de 
    una compañía de seguros. Incluye variables demográficas, económicas, historial de 
    pagos, comportamiento de morosidad, canal de captación, tipo de residencia, valor 
    de la prima y puntaje de evaluación del cliente.

    ### 🛠️ Tecnologías utilizadas
    """)

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

                # Limpiar session state
                st.session_state.df = None

            else:

                # Guardar dataset en session_state
                st.session_state.df = df

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
        # SI YA EXISTE UN DATASET CARGADO
        # ==========================================

        if st.session_state.df is not None:

            st.info(
                "ℹ️ Ya existe un dataset cargado. "
                "Puedes continuar con el análisis."
            )

        else:

            st.info(
                "ℹ️ Debes cargar el archivo "
                "para continuar con el análisis."
            )


# ==========================================
# MODULO 3: ANÁLISIS EXPLORATORIO DE DATOS
# ==========================================

elif modulos == "Análisis Exploratorio de Datos":

    # ==========================================
    # VERIFICAR SI EXISTE DATASET
    # ==========================================

    if st.session_state.df is None:

        st.warning(
            "⚠️ Primero debes cargar el dataset "
            "en la sección 'Carga del Dataset'."
        )

    else:

        # Recuperar dataset
        df = st.session_state.df

        # ==========================================
        # TÍTULO DEL MÓDULO
        # ==========================================

        st.title(
            "Análisis Exploratorio de Datos (EDA)"
        )

        st.write(
            "En este módulo se desarrolla el análisis exploratorio "
            "del dataset de la compañía de seguros."
        )

        # ==========================================
        # TABS DEL EDA
        # ==========================================

        tabs = st.tabs([
            "Item 1: Información general del dataset",
            "Item 2: Clasificación de variables",
            "Item 3: Estadísticas descriptivas",
            "Item 4: Análisis de valores faltantes",
            "Item 5: Distribución de variables numéricas",
            "Item 6: Análisis de variables categóricas",
            "Item 7: Análisis bivariado (numérico vs categórico)",
            "Item 8: Análisis bivariado (categórico vs categórico)",
            "Item 9: Análisis basado en parámetros seleccionados",
            "Item 10: Hallazgos clave" 
        ])

        # ==========================================================
        # ÍTEM 1: INFORMACIÓN GENERAL DEL DATASET
        # ==========================================================

        with tabs[0]:

            st.write(
                "En este análisis se revisa la estructura general "
                "del dataset, los tipos de datos de sus variables "
                "y la presencia de valores nulos."
            )

            # ======================================================
            # 1. INFORMACIÓN GENERAL
            # ======================================================

            st.markdown(
                "### 1. Información general"
            )

            st.write(
                "Se muestra la estructura del DataFrame, "
                "incluyendo el número de registros, "
                "las columnas, los valores no nulos, los tipos de "
                "datos y el uso de memoria."
            )

            buffer = io.StringIO()

            df.info(buf=buffer)

            st.code(
                buffer.getvalue(),
                language="text"
            )

            # ======================================================
            # 2. TIPOS DE DATOS
            # ======================================================

            st.markdown(
                "### 2. Tipos de datos"
            )

            st.write(
                "Se muestra la cantidad de columnas correspondiente "
                "a cada tipo de dato presente en el dataset."
            )

            tipos_datos = (
                df.dtypes
                .astype(str)
                .value_counts()
                .reset_index()
            )

            tipos_datos.columns = [
                "Tipo de dato",
                "Cantidad de columnas"
            ]

            st.dataframe(
                tipos_datos,
                use_container_width=True,
                hide_index=True
            )

            # ======================================================
            # 3. CONTEO DE VALORES NULOS
            # ======================================================

            st.markdown(
                "### 3. Conteo de valores nulos"
            )

            st.write(
                "Se identifica la cantidad de valores nulos "
                "existentes en cada columna del dataset."
            )

            nulos = (
                df.isnull()
                .sum()
                .reset_index()
            )

            nulos.columns = [
                "Columna",
                "Valores nulos"
            ]

            # ------------------------------------------------------
            # Tabla y gráfico
            # ------------------------------------------------------

            col1, col2 = st.columns(2)

            with col1:

                st.dataframe(
                    nulos,
                    use_container_width=True,
                    hide_index=True
                )

            with col2:

                st.bar_chart(
                    nulos.set_index("Columna")
                )

            # ======================================================
            # RESULTADO GENERAL DE VALORES NULOS
            # ======================================================

            total_nulos = df.isnull().sum().sum()

            if total_nulos == 0:

                st.success(
                    "✅ El dataset no contiene valores nulos."
                )

            else:

                st.warning(
                    f"⚠️ El dataset contiene "
                    f"{total_nulos:,} valores nulos."
                )


        # ==========================================================
        # ÍTEM 2: CLASIFICACIÓN DE VARIABLES
        # ==========================================================

        with tabs[1]:

            st.write(
                "En este análisis se identifican las variables "
                "numéricas y categóricas del dataset mediante "
                "una función personalizada."
            )

            # ======================================================
            # FUNCIÓN PERSONALIZADA
            # ======================================================

            def clasificar_variables(df):

                variables_numericas = []
                variables_categoricas = []

                for columna in df.columns:

                    if pd.api.types.is_numeric_dtype(df[columna]):

                        variables_numericas.append(columna)

                    else:

                        variables_categoricas.append(columna)

                return variables_numericas, variables_categoricas


            # ======================================================
            # APLICAR FUNCIÓN PERSONALIZADA
            # ======================================================

            variables_numericas, variables_categoricas = (
                clasificar_variables(df)
            )


            # ======================================================
            # 1. CONTEO DE VARIABLES
            # ======================================================

            st.markdown(
                "### 1. Conteo de variables"
            )

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "🔢 Variables numéricas",
                    len(variables_numericas)
                )

            with col2:

                st.metric(
                    "🔤 Variables categóricas",
                    len(variables_categoricas)
                )


            # ======================================================
            # 2. VARIABLES NUMÉRICAS
            # ======================================================

            st.markdown(
                "### 2. Variables numéricas"
            )

            st.write(
                "Listado de las variables identificadas como "
                "numéricas según el tipo de dato."
            )

            tabla_numericas = pd.DataFrame({
                "Variable": variables_numericas
            })

            st.dataframe(
                tabla_numericas,
                use_container_width=True,
                hide_index=True
            )


            # ======================================================
            # 3. VARIABLES CATEGÓRICAS
            # ======================================================

            st.markdown(
                "### 3. Variables categóricas"
            )

            st.write(
                "Listado de las variables identificadas como "
                "categóricas según el tipo de dato."
            )

            tabla_categoricas = pd.DataFrame({
                "Variable": variables_categoricas
            })

            st.dataframe(
                tabla_categoricas,
                use_container_width=True,
                hide_index=True
            )


            # ======================================================
            # 4. RESUMEN DEL CONTEO
            # ======================================================

            st.markdown(
                "### 4. Resumen de la clasificación"
            )

            resumen_variables = pd.DataFrame({
                "Tipo de variable": [
                    "Numéricas",
                    "Categóricas"
                ],
                "Cantidad": [
                    len(variables_numericas),
                    len(variables_categoricas)
                ]
            })

            st.dataframe(
                resumen_variables,
                use_container_width=True,
                hide_index=True
            )

# ==========================================================
# ÍTEM 3: ESTADÍSTICAS DESCRIPTIVAS
# ==========================================================

with tabs[2]:

    st.write(
        "En este análisis se obtienen las estadísticas descriptivas "
        "de las variables numéricas del dataset mediante la función "
        ".describe()."
    )

    # ======================================================
    # 1. ESTADÍSTICAS DESCRIPTIVAS
    # ======================================================

    st.markdown(
        "### 1. Estadísticas descriptivas"
    )

    st.write(
        "La función .describe() permite obtener un resumen "
        "estadístico de las variables numéricas, incluyendo "
        "el número de observaciones, media, desviación estándar, "
        "valor mínimo, cuartiles y valor máximo."
    )

    estadisticas = df.describe()

    st.dataframe(
        estadisticas,
        use_container_width=True
    )


    # ======================================================
    # 2. INTERPRETACIÓN DE LA MEDIA
    # ======================================================

    st.markdown(
        "### 2. Interpretación de la media"
    )

    st.write(
        "La media representa el valor promedio de cada variable "
        "numérica. Permite conocer el comportamiento central "
        "de los datos."
    )

    medias = df.describe().loc["mean"].reset_index()

    medias.columns = [
        "Variable",
        "Media"
    ]

    st.dataframe(
        medias,
        use_container_width=True,
        hide_index=True
    )


    # ======================================================
    # 3. INTERPRETACIÓN DE LA MEDIANA
    # ======================================================

    st.markdown(
        "### 3. Interpretación de la mediana"
    )

    st.write(
        "La mediana corresponde al valor central de los datos "
        "cuando estos se encuentran ordenados. Es útil para "
        "comparar el comportamiento central con la media y "
        "detectar posibles efectos de valores extremos."
    )

    medianas = df.describe().loc["50%"].reset_index()

    medianas.columns = [
        "Variable",
        "Mediana"
    ]

    st.dataframe(
        medianas,
        use_container_width=True,
        hide_index=True
    )


    # ======================================================
    # 4. INTERPRETACIÓN DE LA DISPERSIÓN
    # ======================================================

    st.markdown(
        "### 4. Interpretación de la dispersión"
    )

    st.write(
        "La desviación estándar permite evaluar qué tan dispersos "
        "se encuentran los valores respecto a la media. Una "
        "desviación estándar mayor indica una mayor variabilidad "
        "de los datos."
    )

    dispersion = df.describe().loc["std"].reset_index()

    dispersion.columns = [
        "Variable",
        "Desviación estándar"
    ]

    st.dataframe(
        dispersion,
        use_container_width=True,
        hide_index=True
    )


    # ======================================================
    # 5. RESUMEN DE MEDIA, MEDIANA Y DISPERSIÓN
    # ======================================================

    st.markdown(
        "### 5. Resumen estadístico"
    )

    resumen_estadistico = pd.DataFrame({
        "Variable": df.describe().columns,
        "Media": df.describe().loc["mean"].values,
        "Mediana": df.describe().loc["50%"].values,
        "Desviación estándar": df.describe().loc["std"].values
    })

    st.dataframe(
        resumen_estadistico,
        use_container_width=True,
        hide_index=True
    )
