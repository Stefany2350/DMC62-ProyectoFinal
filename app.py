import streamlit as st
import numpy as np
import pandas as pd
import io


# ==========================================================
# CONFIGURACIÓN DE LA PÁGINA
# ==========================================================

st.set_page_config(
    page_title="Análisis Exploratorio de Datos",
    layout="wide"
)


# ==========================================================
# INICIALIZACIÓN DEL SESSION STATE
# ==========================================================

if "df" not in st.session_state:
    st.session_state.df = None


# ==========================================================
# FUNCIÓN PERSONALIZADA
# ÍTEM 2: CLASIFICACIÓN DE VARIABLES
# ==========================================================

def clasificar_variables(df):
    """
    Clasifica las variables del DataFrame en:
    - Numéricas
    - Categóricas

    La clasificación se realiza según el tipo
    de dato de cada columna.
    """

    variables_numericas = []
    variables_categoricas = []

    for columna in df.columns:

        if pd.api.types.is_numeric_dtype(df[columna]):
            variables_numericas.append(columna)

        else:
            variables_categoricas.append(columna)

    return variables_numericas, variables_categoricas


# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.title("🎛️ Panel de Navegación")

opcion = st.sidebar.radio(
    "Seleccione una opción:",
    [
        "Home",
        "Carga del Dataset",
        "Análisis Exploratorio de Datos"
    ]
)


# ==========================================================
# HOME
# ==========================================================

if opcion == "Home":

    st.markdown(
        """
        <h1 style="
            text-align: center;
            background: linear-gradient(90deg, #1E293B, #334155, #38BDF8);
            padding: 20px;
            border-radius: 15px;
            color: white;
        ">
            📊 Análisis Exploratorio de Datos
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    st.image("image_home.png", use_container_width=True)

    st.markdown("## 🐍 Python for Analytics")

    st.write(
        """
        Aplicación desarrollada en Python y Streamlit para realizar
        un análisis exploratorio de un dataset de una compañía de seguros.
        """
    )

    st.write(
        """
        El análisis permitirá conocer la estructura de los datos,
        clasificar las variables y posteriormente analizar su
        comportamiento mediante diferentes técnicas estadísticas
        y visualizaciones.
        """
    )

    st.markdown("### 🛠️ Herramientas utilizadas")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image("Python_logo.png", width=100)
        st.write("**Python**")

    with col2:
        st.image("Numpy.png", width=100)
        st.write("**NumPy**")

    with col3:
        st.image("streamlit.jpg", width=100)
        st.write("**Streamlit**")

    with col4:
        st.image("GitHub.png", width=100)
        st.write("**GitHub**")


# ==========================================================
# CARGA DEL DATASET
# ==========================================================

elif opcion == "Carga del Dataset":

    st.title("📂 Carga del Dataset")

    st.write(
        """
        En esta sección se puede cargar el archivo CSV que será
        utilizado posteriormente para realizar el análisis exploratorio.
        """
    )

    archivo = st.file_uploader(
        "Seleccione el archivo CSV",
        type=["csv"]
    )

    if archivo is not None:

        try:

            # Leer archivo CSV
            df = pd.read_csv(archivo)

            # Validar si el dataset está vacío
            if df.empty:

                st.error(
                    "❌ El archivo seleccionado no contiene datos."
                )

            else:

                # Guardar DataFrame en session_state
                st.session_state.df = df

                st.success(
                    "✅ Dataset cargado correctamente."
                )

                # ==================================================
                # INFORMACIÓN GENERAL
                # ==================================================

                st.markdown("### 📊 Información del dataset")

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "Número de filas",
                        df.shape[0]
                    )

                with col2:
                    st.metric(
                        "Número de columnas",
                        df.shape[1]
                    )

                # ==================================================
                # PRIMEROS REGISTROS
                # ==================================================

                st.markdown("### 👀 Primeros 5 registros")

                st.dataframe(
                    df.head(),
                    use_container_width=True,
                    hide_index=True
                )

        except Exception as e:

            st.error(
                f"❌ Se produjo un error al cargar el archivo: {e}"
            )


# ==========================================================
# ANÁLISIS EXPLORATORIO DE DATOS
# ==========================================================

elif opcion == "Análisis Exploratorio de Datos":

    # ==========================================================
    # VERIFICAR SI EXISTE DATASET
    # ==========================================================

    if st.session_state.df is None:

        st.warning(
            "⚠️ Primero debe cargar un dataset en la sección "
            "'Carga del Dataset'."
        )

    else:

        # Recuperar DataFrame
        df = st.session_state.df

        st.title("📊 Análisis Exploratorio de Datos")

        st.write(
            """
            En esta sección se realiza el análisis exploratorio
            del dataset para conocer su estructura, características
            y clasificación de variables.
            """
        )

        # ======================================================
        # TABS
        # ======================================================

        tabs = st.tabs(
            [
                "Ítem 1: Información general del dataset",
                "Ítem 2: Clasificación de variables"
            ]
        )


        # ==========================================================
        # ÍTEM 1: INFORMACIÓN GENERAL DEL DATASET
        # ==========================================================

        with tabs[0]:

            st.write(
                "En este análisis se revisa la estructura general "
                "del dataset, los tipos de datos de sus variables "
                "y la presencia de valores nulos."
            )

            # ==================================================
            # 1. INFORMACIÓN GENERAL
            # ==================================================

            st.markdown("### 1. Información general")

            st.write(
                "Se muestra la estructura del DataFrame, incluyendo "
                "el número de registros, las columnas, los valores "
                "no nulos, los tipos de datos y el uso de memoria."
            )

            # Capturar la información generada por df.info()
            buffer = io.StringIO()

            df.info(buf=buffer)

            # Mostrar información en Streamlit
            st.code(
                buffer.getvalue(),
                language="text"
            )


            # ==================================================
            # 2. TIPOS DE DATOS
            # ==================================================

            st.markdown("### 2. Tipos de datos")

            st.write(
                "Se presenta el conteo de columnas según el tipo "
                "de dato que contienen."
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


            # ==================================================
            # 3. VALORES NULOS
            # ==================================================

            st.markdown("### 3. Valores nulos")

            st.write(
                "Se identifica la cantidad de valores nulos "
                "existentes en cada columna."
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


            # ==================================================
            # RESUMEN DE VALORES NULOS
            # ==================================================

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
                "En este análisis se identifican y clasifican "
                "las variables del dataset en numéricas y categóricas, "
                "utilizando una función personalizada."
            )


            # ==================================================
            # 1. CLASIFICACIÓN DE VARIABLES
            # ==================================================

            st.markdown("### 1. Identificación de variables")

            st.write(
                """
                Las variables son clasificadas de acuerdo con
                el tipo de dato almacenado en cada columna:

                - **Numéricas:** variables cuyos valores son números.
                - **Categóricas:** variables cuyos valores representan
                  categorías o características.
                """
            )


            # Ejecutar función personalizada
            variables_numericas, variables_categoricas = (
                clasificar_variables(df)
            )


            # ==================================================
            # 2. CONTEO DE VARIABLES
            # ==================================================

            st.markdown("### 2. Conteo de variables")

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


            # ==================================================
            # 3. VARIABLES NUMÉRICAS
            # ==================================================

            st.markdown("### 3. Variables numéricas")

            if len(variables_numericas) > 0:

                tabla_numericas = pd.DataFrame(
                    {
                        "Variable numérica":
                            variables_numericas
                    }
                )

                st.dataframe(
                    tabla_numericas,
                    use_container_width=True,
                    hide_index=True
                )

            else:

                st.info(
                    "No se encontraron variables numéricas."
                )


            # ==================================================
            # 4. VARIABLES CATEGÓRICAS
            # ==================================================

            st.markdown("### 4. Variables categóricas")

            if len(variables_categoricas) > 0:

                tabla_categoricas = pd.DataFrame(
                    {
                        "Variable categórica":
                            variables_categoricas
                    }
                )

                st.dataframe(
                    tabla_categoricas,
                    use_container_width=True,
                    hide_index=True
                )

            else:

                st.info(
                    "No se encontraron variables categóricas."
                )


            # ==================================================
            # 5. RESUMEN
            # ==================================================

            st.markdown("### 5. Resumen de la clasificación")

            resumen_variables = pd.DataFrame(
                {
                    "Tipo de variable": [
                        "Numéricas",
                        "Categóricas"
                    ],
                    "Cantidad": [
                        len(variables_numericas),
                        len(variables_categoricas)
                    ]
                }
            )

            st.dataframe(
                resumen_variables,
                use_container_width=True,
                hide_index=True
            )


            # ==================================================
            # 6. GRÁFICO DEL CONTEO
            # ==================================================

            st.markdown("### 6. Distribución de variables")

            st.bar_chart(
                resumen_variables.set_index(
                    "Tipo de variable"
                )
            )
