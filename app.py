import streamlit as st
import numpy as np
import pandas as pd
import io
import matplotlib.pyplot as plt

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

    st.sidebar.image(
        "modulo2.jpg",
        use_container_width=True
    )

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
                "de las variables numéricas mediante la función .describe() "
                "y se realiza una interpretación básica de la media, mediana "
                "y dispersión de las variables más representativas."
            )

            # ----------------------------------------------------------
            # 1. ESTADÍSTICAS DESCRIPTIVAS
            # ----------------------------------------------------------

            st.markdown("### 1. Estadísticas descriptivas")

            estadisticas = df.describe()

            st.dataframe(
                estadisticas,
                use_container_width=True
            )

            # ----------------------------------------------------------
            # 2. SELECCIÓN DE VARIABLES REPRESENTATIVAS
            # ----------------------------------------------------------

            st.markdown("### 2. Selección de variables representativas")

            st.write(
                "Para realizar la interpretación de las estadísticas "
                "descriptivas se seleccionaron las variables **Income** y "
                "**premium**, debido a que ambas son variables numéricas "
                "continuas y representan aspectos económicos relevantes "
                "del conjunto de datos. **Income** representa el ingreso "
                "mensual de los clientes, mientras que **premium** representa "
                "el valor de la prima del seguro. Además, ambas variables "
                "permiten analizar de manera clara su valor promedio, valor "
                "central y nivel de variabilidad."
            )

            # ----------------------------------------------------------
            # 3. INTERPRETACIÓN DE LA MEDIA
            # ----------------------------------------------------------

            st.markdown("### 3. Interpretación de la media")

            st.write(
                "La media permite identificar el valor promedio de las "
                "variables numéricas y proporciona una referencia sobre "
                "el comportamiento general de los datos."
            )

            media_income = df["Income"].mean()
            media_premium = df["premium"].mean()

            st.write(
                f"**Income:** los datos se mueven alrededor de un ingreso "
                f"mensual promedio de **{media_income:,.2f}**."
            )

            st.write(
                f"**Premium:** los datos se mueven alrededor de una prima "
                f"promedio de **{media_premium:,.2f}**."
            )

            # ----------------------------------------------------------
            # 4. INTERPRETACIÓN DE LA MEDIANA
            # ----------------------------------------------------------

            st.markdown("### 4. Interpretación de la mediana")

            st.write(
                "La mediana representa el valor central de los datos. "
                "Su comparación con la media permite identificar posibles "
                "diferencias en la distribución y la influencia de valores "
                "extremos."
            )

            mediana_income = df["Income"].median()
            mediana_premium = df["premium"].median()

            st.write(
                f"**Income:** el valor central de los ingresos mensuales "
                f"es **{mediana_income:,.2f}**, por lo que aproximadamente "
                f"la mitad de los clientes presenta ingresos inferiores "
                f"a este valor y la otra mitad superiores."
            )

            st.write(
                f"**Premium:** el valor central de las primas es "
                f"**{mediana_premium:,.2f}**, por lo que aproximadamente "
                f"la mitad de las pólizas presenta primas inferiores "
                f"a este valor y la otra mitad superiores."
            )

            # ----------------------------------------------------------
            # 5. INTERPRETACIÓN DE LA DISPERSIÓN
            # ----------------------------------------------------------

            st.markdown("### 5. Interpretación de la dispersión")

            st.write(
                "La desviación estándar permite evaluar qué tan dispersos "
                "se encuentran los datos respecto a su media. Una mayor "
                "desviación estándar indica una mayor variabilidad de los "
                "datos."
            )

            desviacion_income = df["Income"].std()
            desviacion_premium = df["premium"].std()

            st.write(
                f"**Income:** presenta una desviación estándar de "
                f"**{desviacion_income:,.2f}**, lo que indica el nivel "
                f"de variabilidad de los ingresos respecto a su media "
                f"de **{media_income:,.2f}**."
            )

            st.write(
                f"**Premium:** presenta una desviación estándar de "
                f"**{desviacion_premium:,.2f}**, lo que indica el nivel "
                f"de variabilidad de las primas respecto a su media "
                f"de **{media_premium:,.2f}**."
            )

            # ----------------------------------------------------------
            # 6. VISUALIZACIÓN DE LA DISPERSIÓN
            # ----------------------------------------------------------

            st.markdown(
                "### 6. Visualización e interpretación de la dispersión"
            )

            dispersion = pd.DataFrame({
                "Variable": ["Income", "Premium"],
                "Desviación estándar": [
                    desviacion_income,
                    desviacion_premium
                ]
            })

            st.write(
                "El siguiente gráfico permite visualizar la desviación "
                "estándar de las dos variables seleccionadas."
            )

            st.bar_chart(
                dispersion.set_index("Variable")
            )

            st.write(
                f"**Income:** la desviación estándar es de "
                f"**{desviacion_income:,.2f}**, lo que indica que los "
                f"ingresos presentan variabilidad alrededor del ingreso "
                f"mensual promedio de **{media_income:,.2f}**."
            )

            st.write(
                f"**Premium:** la desviación estándar es de "
                f"**{desviacion_premium:,.2f}**, lo que indica que los "
                f"valores de las primas presentan variabilidad alrededor "
                f"de la prima promedio de **{media_premium:,.2f}**."
            )


        # ==========================================================
        # ÍTEM 4: ANÁLISIS DE VALORES FALTANTES
        # ==========================================================

        with tabs[3]:

            st.write(
                "En este análisis se identifican y contabilizan los valores "
                "faltantes presentes en el dataset. Además, se presenta una "
                "visualización simple para facilitar su identificación y se "
                "realiza una breve discusión sobre su impacto en el análisis."
            )

            # ----------------------------------------------------------
            # 1. CONTEO DE VALORES FALTANTES
            # ----------------------------------------------------------

            st.markdown("### 1. Conteo de valores faltantes")

            valores_faltantes = df.isnull().sum()

            tabla_faltantes = pd.DataFrame({
                "Variable": valores_faltantes.index,
                "Valores faltantes": valores_faltantes.values
            })

            st.dataframe(
                tabla_faltantes,
                use_container_width=True
            )

            total_faltantes = valores_faltantes.sum()

            if total_faltantes == 0:

                st.success(
                    "El dataset no presenta valores faltantes."
                )

            else:

                st.warning(
                    f"Se identificaron **{total_faltantes:,} valores faltantes "
                    f"en el dataset."
                )

            # ----------------------------------------------------------
            # 2. VISUALIZACIÓN SIMPLE
            # ----------------------------------------------------------

            st.markdown("### 2. Visualización de valores faltantes")

            if total_faltantes > 0:

                faltantes_grafico = tabla_faltantes[
                    tabla_faltantes["Valores faltantes"] > 0
                ].copy()

                st.write(
                    "El siguiente gráfico muestra la cantidad de valores "
                    "faltantes encontrados en las variables que presentan "
                    "datos ausentes."
                )

                st.bar_chart(
                    faltantes_grafico.set_index("Variable")
                )

            else:

                st.info(
                    "No se genera una visualización de valores faltantes "
                    "debido a que todas las variables contienen datos completos."
                )

            # ----------------------------------------------------------
            # 3. DISCUSIÓN BREVE
            # ----------------------------------------------------------

            st.markdown("### 3. Discusión breve")

            if total_faltantes == 0:

                st.write(
                    "El análisis muestra que el dataset no contiene valores "
                    "faltantes. Esto facilita el procesamiento y análisis "
                    "posterior de las variables, ya que no es necesario "
                    "aplicar técnicas de imputación ni eliminar registros "
                    "por ausencia de información."
                )

            else:

                variables_con_faltantes = (
                    valores_faltantes[valores_faltantes > 0]
                    .sort_values(ascending=False)
                )

                cantidad_variables = len(variables_con_faltantes)

                st.write(
                    f"El análisis muestra que existen valores faltantes en "
                    f"**{cantidad_variables} variable(s)**, con un total de "
                    f"**{total_faltantes:,} registros faltantes**. Estos "
                    f"valores deben ser considerados antes de realizar análisis "
                    f"posteriores, ya que su presencia puede afectar algunos "
                    f"cálculos estadísticos y modelos."
                )

                st.write(
                    "La decisión de mantener, eliminar o imputar estos valores "
                    "dependerá de la cantidad de datos faltantes y de la "
                    "importancia de cada variable para el análisis."
                )


        # ==========================================================
        # ÍTEM 5: DISTRIBUCIÓN DE VARIABLES NUMÉRICAS
        # ==========================================================

        with tabs[4]:

            st.write(
                "En este análisis se observa la distribución de las variables "
                "numéricas mediante histogramas, utilizando Matplotlib. "
                "La visualización permite identificar la concentración de los "
                "datos, su dispersión y la posible presencia de valores extremos."
            )

            # ----------------------------------------------------------
            # 1. IDENTIFICACIÓN DE VARIABLES NUMÉRICAS
            # ----------------------------------------------------------

            st.markdown("### 1. Variables numéricas")

            variables_numericas = df.select_dtypes(
                include="number"
            ).columns.tolist()

            st.write(
                f"El dataset contiene **{len(variables_numericas)} variables "
                "numéricas, las cuales pueden ser analizadas mediante "
                "histogramas."
            )

            st.write(
                "Variables numéricas identificadas:"
            )

            st.write(
                ", ".join(variables_numericas)
            )

            # ----------------------------------------------------------
            # 2. HISTOGRAMAS
            # ----------------------------------------------------------

            st.markdown("### 2. Histogramas")

            st.write(
                "Los histogramas permiten observar cómo se distribuyen "
                "los valores de cada variable numérica y en qué rangos "
                "se concentra la mayor cantidad de observaciones."
            )

            # Selección de variables para visualizar
            variables_histograma = st.multiselect(
                "Selecciona las variables que deseas visualizar:",
                variables_numericas,
                default=variables_numericas[:2]
            )

            if variables_histograma:

                for variable in variables_histograma:

                    fig, ax = plt.subplots(figsize=(8, 4))

                    ax.hist(
                        df[variable].dropna(),
                        bins=30,
                        edgecolor="black"
                    )

                    ax.set_title(
                        f"Distribución de {variable}"
                    )

                    ax.set_xlabel(variable)
                    ax.set_ylabel("Frecuencia")

                    ax.grid(
                        axis="y",
                        alpha=0.3
                    )

                    st.pyplot(fig)

                    plt.close(fig)

            else:

                st.info(
                    "Selecciona al menos una variable para visualizar "
                    "su distribución."
                )

            # ----------------------------------------------------------
            # 3. INTERPRETACIÓN VISUAL
            # ----------------------------------------------------------

            st.markdown("### 3. Interpretación visual")

            st.write(
                "La interpretación de los histogramas permite identificar "
                "la forma de la distribución, los rangos donde se concentra "
                "la mayor cantidad de observaciones, el nivel de dispersión "
                "y la posible presencia de valores extremos."
            )

            # Interpretación automática básica de las variables seleccionadas
            for variable in variables_histograma:

                serie = df[variable].dropna()

                media = serie.mean()
                mediana = serie.median()
                desviacion = serie.std()
                minimo = serie.min()
                maximo = serie.max()

            # Rango intercuartílico
                q1 = serie.quantile(0.25)
                q3 = serie.quantile(0.75)

                if media > mediana:

                    forma_distribucion = (
                    "La media es mayor que la mediana, lo que sugiere "
                    "una distribución con cierta concentración de valores "
                    "hacia niveles más altos."
                    )

                elif media < mediana:

                     forma_distribucion = (
                    "La media es menor que la mediana, lo que sugiere "
                    "una distribución con cierta concentración de valores "
                    "hacia niveles más bajos."
                    )

                else:

                    forma_distribucion = (
                    "La media y la mediana presentan valores similares, "
                    "lo que sugiere una distribución relativamente equilibrada."
                    )

                   st.write(
                    f"**{variable}:** {forma_distribucion}"
                    )

                    st.write(
                    f"Los valores se encuentran entre **{minimo:,.2f}** y "
                    f"**{maximo:,.2f}**. El 50% central de las observaciones "
                    f"se concentra aproximadamente entre **{q1:,.2f}** y "
                    f"**{q3:,.2f}**."
                    )
                
                    st.write(
                        f"La variable presenta una desviación estándar de "
                        f"**{desviacion:,.2f}**, lo que indica una dispersión "
                        f"considerable de los datos alrededor de la media de "
                        f"**{media:,.2f}**."
                    )
                
                    st.write(
                        f"Visualmente, el histograma permite identificar si existen "
                        f"observaciones alejadas de la concentración principal de "
                        f"los datos, las cuales podrían corresponder a posibles "
                        f"valores extremos. Estos casos deben verificarse "
                        f"directamente en la distribución antes de considerarlos "
                        f"como valores atípicos."
                    )

        # ==========================================================
        # ÍTEMS 6 AL 10
        # ==========================================================
        # Aquí puedes colocar posteriormente el código correspondiente
        # a los Items 6, 7, 8, 9 y 10, manteniendo la misma estructura:
        #
        # with tabs[5]:
        #     ...
        #
        # with tabs[6]:
        #     ...
        #
        # with tabs[7]:
        #     ...
        #
        # with tabs[8]:
        #     ...
        #
        # with tabs[9]:
        #     ...
