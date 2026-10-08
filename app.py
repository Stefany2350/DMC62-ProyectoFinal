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
# CLASE DATA ANALYZER - PROGRAMACIÓN ORIENTADA A OBJETOS
# ==========================================

class DataAnalyzer:

    def __init__(self, df):
        self.df = df

    # ------------------------------------------
    # Clasificación de variables
    # ------------------------------------------

    def clasificar_variables(self):

        variables_numericas = []
        variables_categoricas = []

        for columna in self.df.columns:

            if pd.api.types.is_numeric_dtype(self.df[columna]):

                variables_numericas.append(columna)

            else:

                variables_categoricas.append(columna)

        return variables_numericas, variables_categoricas

    # ------------------------------------------
    # Estadísticas descriptivas
    # ------------------------------------------

    def estadisticas_descriptivas(self):

        return self.df.describe()

    # ------------------------------------------
    # Media
    # ------------------------------------------

    def media(self, variable):

        return self.df[variable].mean()

    # ------------------------------------------
    # Mediana
    # ------------------------------------------

    def mediana(self, variable):

        return self.df[variable].median()

    # ------------------------------------------
    # Moda
    # ------------------------------------------

    def moda(self, variable):

        return self.df[variable].mode()

    # ------------------------------------------
    # Valores faltantes
    # ------------------------------------------

    def valores_faltantes(self):

        return self.df.isnull().sum()

    # ------------------------------------------
    # Histograma
    # ------------------------------------------

    def graficar_histograma(
        self,
        variable,
        bins=30
    ):

        fig, ax = plt.subplots(
            figsize=(8, 4)
        )

        ax.hist(
            self.df[variable].dropna(),
            bins=bins,
            edgecolor="black"
        )

        ax.set_title(
            f"Distribución de {variable}"
        )

        ax.set_xlabel(variable)

        ax.set_ylabel(
            "Frecuencia"
        )

        ax.grid(
            axis="y",
            alpha=0.3
        )

        return fig

    # ------------------------------------------
    # Gráfico de barras
    # ------------------------------------------

    def graficar_barras(self, variable):

        frecuencias = (
            self.df[variable]
            .value_counts(dropna=False)
        )

        fig, ax = plt.subplots(
            figsize=(8, 4)
        )

        frecuencias.plot(
            kind="bar",
            ax=ax
        )

        ax.set_title(
            f"Distribución de {variable}"
        )

        ax.set_xlabel(variable)

        ax.set_ylabel(
            "Frecuencia"
        )

        ax.tick_params(
            axis="x",
            rotation=45
        )

        plt.tight_layout()

        return fig


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
        "Conclusiones Finales",
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
    conjunto de datos permite aplicar análisis exploratorio y visualización de datos para identificar 
    patrones de clientes que renuevan o no su seguro.
    """)

    st.markdown("""
    ### 📝 Datos del Autor

    * Nombre completo: Stefany Salazar Espinoza 
    * Curso: Especialización en Python for Analytics  
    * Año: 2026
    """)

    st.markdown("""
    ### 👨‍🏫 Explicación del Dataset

    El dataset escogido, InsuranceCompany.csv, contiene información histórica de clientes de 
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

    col5, col6 = st.columns(2)

    with col5:
        st.image("Pandas_python.png", width=220)

    with col6:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.image("matplot_logo.png", width=220)

# ==========================================
# MODULO 2: CARGA DEL DATASET
# ==========================================

elif modulos == "Carga del Dataset":

    st.title("Análisis Exploratorio de Datos - Compañía de Seguros")

    st.write(
        "Carga el archivo InsuranceCompany.csv para iniciar "
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
        # CREAR OBJETO DE LA CLASE DATA ANALYZER
        # ==========================================

        analizador = DataAnalyzer(df)

        # Clasificación de variables mediante POO
        variables_numericas, variables_categoricas = (
            analizador.clasificar_variables()
        )

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
                "la clase DataAnalyzer."
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
                "numéricas mediante la clase DataAnalyzer."
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

     
        # ==========================================================
        # ÍTEM 3: ESTADÍSTICAS DESCRIPTIVAS
        # ==========================================================

        with tabs[2]:

            st.write(
                "En este análisis se obtienen las estadísticas descriptivas "
                "de las variables numéricas mediante la función .describe() "
                "y se realiza una interpretación básica de la media, mediana, "
                "moda y dispersión de las variables."
            )

            # ----------------------------------------------------------
            # 1. ESTADÍSTICAS DESCRIPTIVAS
            # ----------------------------------------------------------

            st.markdown("### 1. Estadísticas descriptivas")

            estadisticas = (
                analizador.estadisticas_descriptivas()
            )

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
                "y representan aspectos económicos relevantes del conjunto "
                "de datos."
            )

            # ----------------------------------------------------------
            # 3. MEDIA, MEDIANA Y DISPERSIÓN
            # ----------------------------------------------------------

            st.markdown(
                "### 3. Media, mediana y dispersión"
            )

            media_income = analizador.media("Income")
            media_premium = analizador.media("premium")

            mediana_income = analizador.mediana("Income")
            mediana_premium = analizador.mediana("premium")

            desviacion_income = df["Income"].std()
            desviacion_premium = df["premium"].std()

            col1, col2 = st.columns(2)

            with col1:

                st.markdown("#### Income")

                st.metric(
                    "Media",
                    f"{media_income:,.2f}"
                )

                st.metric(
                    "Mediana",
                    f"{mediana_income:,.2f}"
                )

                st.metric(
                    "Desviación estándar",
                    f"{desviacion_income:,.2f}"
                )

            with col2:

                st.markdown("#### Premium")

                st.metric(
                    "Media",
                    f"{media_premium:,.2f}"
                )

                st.metric(
                    "Mediana",
                    f"{mediana_premium:,.2f}"
                )

                st.metric(
                    "Desviación estándar",
                    f"{desviacion_premium:,.2f}"
                )

            # ----------------------------------------------------------
            # 4. MODA
            # ----------------------------------------------------------

            st.markdown(
                "### 5. Moda"
            )

            st.write(
                "La moda corresponde al valor que aparece con mayor "
                "frecuencia. En variables numéricas continuas puede "
                "tener menor utilidad interpretativa, por lo que se "
                "aplica principalmente a variables categóricas."
            )

            if len(variables_categoricas) > 0:

                variable_moda = variables_categoricas[0]

                moda = analizador.moda(
                    variable_moda
                )

                if not moda.empty:

                    st.write(
                        f"La variable categórica seleccionada para "
                        f"ejemplificar la moda es **{variable_moda}**."
                    )

                    st.write(
                        f"La categoría con mayor frecuencia es "
                        f"**{moda.iloc[0]}**."
                    )      

            # ----------------------------------------------------------
            # 5. INTERPRETACIÓN
            # ----------------------------------------------------------
            
            st.markdown(
                "### 4. Interpretación"
            )
            
            # Desviación estándar
            desviacion_income = df["Income"].std()
            desviacion_premium = df["premium"].std()
            
            # ==========================================================
            # INTERPRETACIÓN DE INCOME
            # ==========================================================
            
            st.write(
                f"**Income:** los datos presentan un ingreso mensual "
                f"promedio de **{media_income:,.2f}**, una mediana de "
                f"**{mediana_income:,.2f}** y una desviación estándar de "
                f"**{desviacion_income:,.2f}**."
            )
            
            if media_income > mediana_income:
            
                st.write(
                    "La media es superior a la mediana, lo que puede indicar "
                    "cierta asimetría hacia valores altos."
                )
            
            elif media_income < mediana_income:
            
                st.write(
                    "La media es inferior a la mediana, lo que puede indicar "
                    "cierta asimetría hacia valores bajos."
                )
            
            else:
            
                st.write(
                    "La media y la mediana presentan valores similares."
                )
            
            st.write(
                f"La desviación estándar de **{desviacion_income:,.2f}** "
                f"indica la dispersión de los ingresos respecto a su promedio. "
                f"Un valor mayor representa una mayor variabilidad entre los ingresos."
            )
            
            
            # ==========================================================
            # INTERPRETACIÓN DE PREMIUM
            # ==========================================================
            
            st.write(
                f"**Premium:** los datos presentan una prima promedio de "
                f"**{media_premium:,.2f}**, una mediana de **{mediana_premium:,.2f}** "
                f"y una desviación estándar de **{desviacion_premium:,.2f}**."
            )
            
            if media_premium > mediana_premium:
            
                st.write(
                    "La media es superior a la mediana, lo que puede indicar "
                    "cierta asimetría hacia valores altos."
                )
            
            elif media_premium < mediana_premium:
            
                st.write(
                    "La media es inferior a la mediana, lo que puede indicar "
                    "cierta asimetría hacia valores bajos."
                )
            
            else:
            
                st.write(
                    "La media y la mediana presentan valores similares."
                )
            
            st.write(
                f"La desviación estándar de **{desviacion_premium:,.2f}** "
                f"indica la dispersión de las primas respecto a su promedio. "
                f"Un valor mayor representa una mayor variabilidad en las primas."
            )
        # ==========================================================
        # ÍTEM 4: ANÁLISIS DE VALORES FALTANTES
        # ==========================================================

        with tabs[3]:

            st.write(
                "En este análisis se identifican y contabilizan los valores "
                "faltantes presentes en el dataset. Además, se presenta una "
                "visualización simple para facilitar su identificación."
            )

            # ----------------------------------------------------------
            # 1. CONTEO DE VALORES FALTANTES
            # ----------------------------------------------------------

            st.markdown(
                "### 1. Conteo de valores faltantes"
            )

            valores_faltantes = (
                analizador.valores_faltantes()
            )

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
                    f"Se identificaron **{total_faltantes:,} valores "
                    f"faltantes en el dataset."
                )

            # ----------------------------------------------------------
            # 2. VISUALIZACIÓN
            # ----------------------------------------------------------

            st.markdown(
                "### 2. Visualización de valores faltantes"
            )

            if total_faltantes > 0:

                faltantes_grafico = tabla_faltantes[
                    tabla_faltantes["Valores faltantes"] > 0
                ].copy()

                st.bar_chart(
                    faltantes_grafico.set_index(
                        "Variable"
                    )
                )

            else:

                st.info(
                    "No se genera una visualización debido a que "
                    "el dataset no presenta valores faltantes."
                )

            # ----------------------------------------------------------
            # 3. DISCUSIÓN
            # ----------------------------------------------------------
            
            st.markdown(
                "### 3. Discusión breve"
            )
            
            if total_faltantes == 0:
            
                st.write(
                    "El dataset no contiene valores faltantes, lo cual "
                    "facilita el procesamiento y análisis posterior."
                )
            
            else:
            
                variables_con_faltantes = (
                    valores_faltantes[
                        valores_faltantes > 0
                    ]
                    .sort_values(
                        ascending=False
                    )
                )
            
                st.write(
                    f"Se identificaron valores faltantes en "
                    f"**{len(variables_con_faltantes)} variable(s)**."
                )
            
                st.write(
                    "Las variables que presentan valores faltantes son:"
                )
            
                # Tabla de variables con valores faltantes
                tabla_faltantes = pd.DataFrame({
                    "Variable": variables_con_faltantes.index,
                    "Valores faltantes": variables_con_faltantes.values,
                    "Porcentaje faltante (%)": (
                        variables_con_faltantes.values / len(df) * 100
                    ).round(2)
                })
            
                st.dataframe(
                    tabla_faltantes,
                    use_container_width=True,
                    hide_index=True
                )
            
                st.markdown(
                    "#### 💡 Posibles acciones"
                )
            
                st.write(
                    "El tratamiento de los valores faltantes dependerá del tipo "
                    "de variable y de la cantidad de información ausente:"
                )
            
                st.write(
                    "• **Variables numéricas:** se puede evaluar la imputación "
                    "utilizando medidas como la mediana o la media, especialmente "
                    "cuando el porcentaje de datos faltantes es reducido."
                )
            
                st.write(
                    "• **Porcentaje elevado de faltantes:** antes de imputar, "
                    "se debe analizar si la variable aporta información suficiente "
                    "para justificar su conservación."
                )
            
                st.write(
                    "• **Registros con pocos datos faltantes:** se puede evaluar "
                    "la eliminación de determinados registros, siempre que esto "
                    "no genere una pérdida significativa de información."
                )
            
                st.write(
                    "• **Antes de realizar análisis posteriores:** se recomienda "
                    "evaluar el origen de los valores faltantes y aplicar un "
                    "tratamiento consistente para evitar distorsionar los resultados."
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
            # 1. VARIABLES NUMÉRICAS
            # ----------------------------------------------------------
            
            st.markdown(
                "### 1. Variables numéricas"
            )
            
            variables_numericas = (
                df.select_dtypes(
                    include="number"
                )
                .columns
                .tolist()
            )
            
            st.write(
                f"El dataset contiene **{len(variables_numericas)} "
                "variables numéricas."
            )
            
            # Tabla de variables numéricas
            tabla_numericas = pd.DataFrame({
                "N°": range(1, len(variables_numericas) + 1),
                "Variable numérica": variables_numericas
            })
            
            st.dataframe(
                tabla_numericas,
                use_container_width=True,
                hide_index=True
            )

            # ----------------------------------------------------------
            # 2. MULTISELECT
            # ----------------------------------------------------------

            st.markdown(
                "### 2. Selección de variables"
            )

            variables_histograma = st.multiselect(
                "Selecciona las variables que deseas visualizar:",
                variables_numericas,
                default=variables_numericas[:2]
            )

            # ----------------------------------------------------------
            # 3. SLIDER
            # ----------------------------------------------------------

            st.markdown(
                "### 3. Configuración del histograma"
            )

            numero_bins = st.slider(
                "Selecciona el número de intervalos del histograma:",
                min_value=5,
                max_value=50,
                value=30,
                step=5
            )

            # ----------------------------------------------------------
            # 4. CHECKBOX
            # ----------------------------------------------------------

            mostrar_interpretacion = st.checkbox(
                "Mostrar interpretación estadística",
                value=True
            )

            # ----------------------------------------------------------
            # 5. HISTOGRAMAS
            # ----------------------------------------------------------

            st.markdown(
                "### 4. Histogramas"
            )

            if variables_histograma:

                for variable in variables_histograma:

                    fig = (
                        analizador
                        .graficar_histograma(
                            variable,
                            numero_bins
                        )
                    )

                    st.pyplot(fig)

                    plt.close(fig)

            else:

                st.info(
                    "Selecciona al menos una variable para visualizar "
                    "su distribución."
                )

            # ----------------------------------------------------------
            # 6. INTERPRETACIÓN
            # ----------------------------------------------------------

            if mostrar_interpretacion:

                st.markdown(
                    "### 5. Interpretación visual"
                )

                for variable in variables_histograma:

                    serie = df[variable].dropna()

                    media = serie.mean()
                    mediana = serie.median()
                    desviacion = serie.std()

                    minimo = serie.min()
                    maximo = serie.max()

                    q1 = serie.quantile(0.25)
                    q3 = serie.quantile(0.75)

                    if media > mediana:

                        forma_distribucion = (
                            "La media es mayor que la mediana, "
                            "lo que sugiere cierta asimetría hacia "
                            "valores altos."
                        )

                    elif media < mediana:

                        forma_distribucion = (
                            "La media es menor que la mediana, "
                            "lo que sugiere cierta asimetría hacia "
                            "valores bajos."
                        )

                    else:

                        forma_distribucion = (
                            "La media y la mediana presentan valores "
                            "similares, lo que sugiere una distribución "
                            "relativamente equilibrada."
                        )

                    st.write(
                        f"**{variable}:** "
                        f"{forma_distribucion}"
                    )

                    st.write(
                        f"Los valores se encuentran entre "
                        f"**{minimo:,.2f}** y **{maximo:,.2f}**. "
                        f"El 50% central de las observaciones se "
                        f"encuentra aproximadamente entre "
                        f"**{q1:,.2f}** y **{q3:,.2f}**."
                    )

                    st.write(
                        f"La desviación estándar es de "
                        f"**{desviacion:,.2f}**, lo que permite "
                        f"evaluar la dispersión de los datos "
                        f"respecto a su media de "
                        f"**{media:,.2f}**."
                    )


        # ==========================================================
        # ÍTEM 6: ANÁLISIS DE VARIABLES CATEGÓRICAS
        # ==========================================================

        with tabs[5]:

            st.write(
                "En este análisis se estudia la distribución de las variables "
                "categóricas mediante conteos y proporciones. Los gráficos de "
                "barras permiten identificar visualmente las categorías con "
                "mayor y menor frecuencia."
            )

            # ----------------------------------------------------------
            # 1. VARIABLES CATEGÓRICAS
            # ----------------------------------------------------------

            st.markdown(
                "### 1. Variables categóricas"
            )

            if len(variables_categoricas) == 0:

                st.info(
                    "El dataset no contiene variables categóricas."
                )

            else:

                st.write(
                    f"Se identificaron **{len(variables_categoricas)} "
                    f"variables categóricas**."
                )

                st.dataframe(
                    pd.DataFrame({
                        "Variables categóricas":
                            variables_categoricas
                    }),
                    use_container_width=True,
                    hide_index=True
                )

                # ------------------------------------------------------
                # 2. CONTEOS
                # ------------------------------------------------------

                st.markdown(
                    "### 2. Conteos por categoría"
                )

                for variable in variables_categoricas:

                    st.markdown(
                        f"#### {variable}"
                    )

                    conteos = (
                        df[variable]
                        .value_counts(
                            dropna=False
                        )
                        .reset_index()
                    )

                    conteos.columns = [
                        "Categoría",
                        "Cantidad"
                    ]

                    st.dataframe(
                        conteos,
                        use_container_width=True,
                        hide_index=True
                    )

                # ------------------------------------------------------
                # 3. GRÁFICOS DE BARRAS
                # ------------------------------------------------------

                st.markdown(
                    "### 3. Gráficos de barras"
                )

                for variable in variables_categoricas:

                    st.markdown(
                        f"#### Distribución de {variable}"
                    )

                    conteos_grafico = (
                        df[variable]
                        .value_counts(
                            dropna=False
                        )
                    )

                    st.bar_chart(
                        conteos_grafico
                    )

                # ------------------------------------------------------
                # 4. PROPORCIONES
                # ------------------------------------------------------

                st.markdown(
                    "### 4. Proporciones"
                )

                for variable in variables_categoricas:

                    proporciones = (
                        df[variable]
                        .value_counts(
                            normalize=True,
                            dropna=False
                        )
                        .mul(100)
                        .round(2)
                        .reset_index()
                    )

                    proporciones.columns = [
                        "Categoría",
                        "Proporción (%)"
                    ]

                    st.markdown(
                        f"#### Proporciones de {variable}"
                    )

                    st.dataframe(
                        proporciones,
                        use_container_width=True,
                        hide_index=True
                    )


        # ==========================================================
        # ÍTEM 7: ANÁLISIS BIVARIADO
        # ==========================================================

        with tabs[6]:

            st.write(
                "En este análisis se estudia la relación entre variables "
                "numéricas y la variable categórica **renewal**. "
                "Se comparan los valores de las variables numéricas según "
                "las categorías de renovación."
            )

            # ----------------------------------------------------------
            # 1. INCOME VS RENEWAL
            # ----------------------------------------------------------

            st.markdown(
                "### 1. Income vs renewal"
            )

            resumen_income = (
                df.groupby(
                    "renewal",
                    as_index=False
                )["Income"]
                .agg(
                    Media="mean",
                    Mediana="median",
                    Mínimo="min",
                    Máximo="max"
                )
                .round(2)
            )

            st.dataframe(
                resumen_income,
                use_container_width=True,
                hide_index=True
            )

            promedio_income = (
                df.groupby("renewal")["Income"]
                .mean()
                .round(2)
                .reset_index()
            )

            promedio_income.columns = [
                "renewal",
                "Ingreso promedio"
            ]

            st.bar_chart(
                promedio_income.set_index(
                    "renewal"
                )
            )

            # ----------------------------------------------------------
            # 2. NO_OF_PREMIUMS_PAID VS RENEWAL
            # ----------------------------------------------------------

            st.markdown(
                "### 2. no_of_premiums_paid vs renewal"
            )

            resumen_primas = (
                df.groupby(
                    "renewal",
                    as_index=False
                )["no_of_premiums_paid"]
                .agg(
                    Media="mean",
                    Mediana="median",
                    Mínimo="min",
                    Máximo="max"
                )
                .round(2)
            )

            st.dataframe(
                resumen_primas,
                use_container_width=True,
                hide_index=True
            )

            promedio_primas = (
                df.groupby(
                    "renewal"
                )["no_of_premiums_paid"]
                .mean()
                .round(2)
                .reset_index()
            )

            promedio_primas.columns = [
                "renewal",
                "Primas pagadas promedio"
            ]

            st.bar_chart(
                promedio_primas.set_index(
                    "renewal"
                )
            )

            # ----------------------------------------------------------
            # 3. INTERPRETACIÓN
            # ----------------------------------------------------------

            st.markdown(
                "### 3. Interpretación"
            )

            income_0 = df.loc[
                df["renewal"] == 0,
                "Income"
            ].mean()

            income_1 = df.loc[
                df["renewal"] == 1,
                "Income"
            ].mean()

            if income_1 > income_0:

                st.write(
                    f"**Income vs renewal:** los clientes con "
                    f"**renewal = 1** presentan un ingreso promedio "
                    f"mayor. El promedio es **{income_1:,.2f}**, "
                    f"frente a **{income_0:,.2f}** para renewal = 0."
                )

            elif income_1 < income_0:

                st.write(
                    f"**Income vs renewal:** los clientes con "
                    f"**renewal = 1** presentan un ingreso promedio "
                    f"menor. El promedio es **{income_1:,.2f}**, "
                    f"frente a **{income_0:,.2f}** para renewal = 0."
                )

            else:

                st.write(
                    "El ingreso promedio es igual entre ambos grupos."
                )

            primas_0 = df.loc[
                df["renewal"] == 0,
                "no_of_premiums_paid"
            ].mean()

            primas_1 = df.loc[
                df["renewal"] == 1,
                "no_of_premiums_paid"
            ].mean()

            if primas_1 > primas_0:

                st.write(
                    f"**no_of_premiums_paid vs renewal:** los clientes "
                    f"con renewal = 1 presentan un mayor promedio de "
                    f"primas pagadas: **{primas_1:,.2f}** frente a "
                    f"**{primas_0:,.2f}**."
                )

            elif primas_1 < primas_0:

                st.write(
                    f"**no_of_premiums_paid vs renewal:** los clientes "
                    f"con renewal = 1 presentan un menor promedio de "
                    f"primas pagadas: **{primas_1:,.2f}** frente a "
                    f"**{primas_0:,.2f}**."
                )

            else:

                st.write(
                    "El promedio de primas pagadas es igual entre ambos grupos."
                )

            st.caption(
                "Las diferencias observadas representan asociaciones "
                "entre grupos y no implican necesariamente causalidad."
            )


        # ==========================================================
        # ÍTEM 8: ANÁLISIS BIVARIADO CATEGÓRICO VS CATEGÓRICO
        # ==========================================================

        with tabs[7]:

            st.write(
                "En este análisis se estudia la relación entre dos variables "
                "categóricas. Se comparan **residence_area_type** y "
                "**sourcing_channel** según **renewal**."
            )

            # ----------------------------------------------------------
            # 1. RESIDENCE_AREA_TYPE VS RENEWAL
            # ----------------------------------------------------------

            st.markdown(
                "### 1. residence_area_type vs renewal"
            )

            tabla_residencia = pd.crosstab(
                df["residence_area_type"],
                df["renewal"]
            )

            tabla_residencia.columns = [
                "No renovó (0)",
                "Renovó (1)"
            ]

            st.markdown(
                "#### Conteos"
            )

            st.dataframe(
                tabla_residencia,
                use_container_width=True
            )

            proporciones_residencia = (
                pd.crosstab(
                    df["residence_area_type"],
                    df["renewal"],
                    normalize="index"
                ) * 100
            )

            proporciones_residencia.columns = [
                "No renovó (0) %",
                "Renovó (1) %"
            ]

            proporciones_residencia = (
                proporciones_residencia.round(2)
            )

            st.markdown(
                "#### Proporciones por tipo de residencia"
            )

            st.dataframe(
                proporciones_residencia,
                use_container_width=True
            )

            st.bar_chart(
                proporciones_residencia
            )

            # ----------------------------------------------------------
            # 2. SOURCING_CHANNEL VS RENEWAL
            # ----------------------------------------------------------

            st.markdown(
                "### 2. sourcing_channel vs renewal"
            )

            tabla_canal = pd.crosstab(
                df["sourcing_channel"],
                df["renewal"]
            )

            tabla_canal.columns = [
                "No renovó (0)",
                "Renovó (1)"
            ]

            st.markdown(
                "#### Conteos"
            )

            st.dataframe(
                tabla_canal,
                use_container_width=True
            )

            proporciones_canal = (
                pd.crosstab(
                    df["sourcing_channel"],
                    df["renewal"],
                    normalize="index"
                ) * 100
            )

            proporciones_canal.columns = [
                "No renovó (0) %",
                "Renovó (1) %"
            ]

            proporciones_canal = (
                proporciones_canal.round(2)
            )

            st.markdown(
                "#### Proporciones por canal"
            )

            st.dataframe(
                proporciones_canal,
                use_container_width=True
            )

            st.bar_chart(
                proporciones_canal
            )

            # ----------------------------------------------------------
            # 3. INTERPRETACIÓN
            # ----------------------------------------------------------

            st.markdown(
                "### 3. Interpretación"
            )

            renovacion_residencia = (
                df.groupby(
                    "residence_area_type"
                )["renewal"]
                .mean()
                .mul(100)
                .round(2)
                .sort_values(
                    ascending=False
                )
            )

            if len(renovacion_residencia) > 0:

                residencia_mayor = (
                    renovacion_residencia.index[0]
                )

                porcentaje_mayor = (
                    renovacion_residencia.iloc[0]
                )

                residencia_menor = (
                    renovacion_residencia.index[-1]
                )

                porcentaje_menor = (
                    renovacion_residencia.iloc[-1]
                )

                st.write(
                    f"**residence_area_type vs renewal:** "
                    f"**{residencia_mayor}** presenta la mayor "
                    f"proporción de renovación, con "
                    f"**{porcentaje_mayor:.2f}%**. "
                    f"**{residencia_menor}** presenta la menor, "
                    f"con **{porcentaje_menor:.2f}%**."
                )

            renovacion_canal = (
                df.groupby(
                    "sourcing_channel"
                )["renewal"]
                .mean()
                .mul(100)
                .round(2)
                .sort_values(
                    ascending=False
                )
            )

            if len(renovacion_canal) > 0:

                canal_mayor = (
                    renovacion_canal.index[0]
                )

                porcentaje_canal_mayor = (
                    renovacion_canal.iloc[0]
                )

                canal_menor = (
                    renovacion_canal.index[-1]
                )

                porcentaje_canal_menor = (
                    renovacion_canal.iloc[-1]
                )

                st.write(
                    f"**sourcing_channel vs renewal:** "
                    f"**{canal_mayor}** presenta la mayor "
                    f"proporción de renovación, con "
                    f"**{porcentaje_canal_mayor:.2f}%**. "
                    f"**{canal_menor}** presenta la menor, "
                    f"con **{porcentaje_canal_menor:.2f}%**."
                )

            st.caption(
                "Las diferencias observadas representan asociaciones "
                "entre variables y no permiten establecer causalidad "
                "por sí solas."
            )


        # ==========================================================
        # ÍTEM 9: ANÁLISIS BASADO EN PARÁMETROS SELECCIONADOS
        # ==========================================================

        with tabs[8]:

            st.write(
                "En este apartado el usuario puede seleccionar las variables "
                "que desea analizar mediante controles interactivos. "
                "El análisis se actualiza dinámicamente de acuerdo con "
                "las columnas seleccionadas."
            )

            # ----------------------------------------------------------
            # 1. VARIABLES DISPONIBLES
            # ----------------------------------------------------------

            st.markdown(
                "### 1. Selección de parámetros"
            )

            variables_categoricas_parametros = [
                columna
                for columna in df.columns
                if not pd.api.types.is_numeric_dtype(
                    df[columna]
                )
            ]

            variables_numericas_parametros = [
                columna
                for columna in df.columns
                if pd.api.types.is_numeric_dtype(
                    df[columna]
                )
            ]

            # ----------------------------------------------------------
            # 2. SELECTBOX
            # ----------------------------------------------------------

            variable_categorica_seleccionada = (
                st.selectbox(
                    "Seleccione una variable categórica:",
                    variables_categoricas_parametros
                )
            )

            # ----------------------------------------------------------
            # 3. MULTISELECT
            # ----------------------------------------------------------

            variables_numericas_seleccionadas = (
                st.multiselect(
                    "Seleccione una o más variables numéricas:",
                    variables_numericas_parametros,
                    default=variables_numericas_parametros[:2]
                )
            )

            # ----------------------------------------------------------
            # 4. TIPO DE ANÁLISIS
            # ----------------------------------------------------------

            tipo_analisis = st.selectbox(
                "Seleccione el tipo de análisis:",
                [
                    "Promedio por categoría",
                    "Mediana por categoría",
                    "Mínimo por categoría",
                    "Máximo por categoría"
                ]
            )

            # ----------------------------------------------------------
            # 5. VALIDACIÓN
            # ----------------------------------------------------------

            if len(
                variables_numericas_seleccionadas
            ) == 0:

                st.warning(
                    "Seleccione al menos una variable numérica "
                    "para realizar el análisis."
                )

            else:

                st.markdown(
                    "### 2. Resultado del análisis"
                )

                st.write(
                    f"Variable categórica seleccionada: "
                    f"**{variable_categorica_seleccionada}**"
                )

                st.write(
                    "Variables numéricas seleccionadas: "
                    + ", ".join(
                        f"**{variable}**"
                        for variable
                        in variables_numericas_seleccionadas
                    )
                )

                # ------------------------------------------------------
                # FUNCIÓN DE AGRUPACIÓN
                # ------------------------------------------------------

                if tipo_analisis == "Promedio por categoría":

                    funcion_agrupacion = "mean"

                elif tipo_analisis == "Mediana por categoría":

                    funcion_agrupacion = "median"

                elif tipo_analisis == "Mínimo por categoría":

                    funcion_agrupacion = "min"

                else:

                    funcion_agrupacion = "max"

                # ------------------------------------------------------
                # 6. TABLA DINÁMICA
                # ------------------------------------------------------

                columnas_analisis = [
                    variable_categorica_seleccionada
                ] + variables_numericas_seleccionadas

                datos_analisis = (
                    df[columnas_analisis]
                    .copy()
                )

                resultado = (
                    datos_analisis
                    .groupby(
                        variable_categorica_seleccionada
                    )[variables_numericas_seleccionadas]
                    .agg(
                        funcion_agrupacion
                    )
                    .round(8)
                )

                st.dataframe(
                    resultado,
                    use_container_width=True
                )

                # ------------------------------------------------------
                # 7. GRÁFICOS
                # ------------------------------------------------------

                st.markdown(
                    "### 3. Visualización"
                )

                for variable in (
                    variables_numericas_seleccionadas
                ):

                    datos_grafico = (
                        df.groupby(
                            variable_categorica_seleccionada
                        )[variable]
                        .agg(
                            funcion_agrupacion
                        )
                        .round(8)
                    )

                    st.markdown(
                        f"#### {variable} según "
                        f"{variable_categorica_seleccionada}"
                    )

                    st.bar_chart(
                        datos_grafico
                    )

                # ------------------------------------------------------
                # 8. INTERPRETACIÓN
                # ------------------------------------------------------

                st.markdown(
                    "### 4. Interpretación"
                )

                for variable in (
                    variables_numericas_seleccionadas
                ):

                    datos_interpretacion = (
                        df.groupby(
                            variable_categorica_seleccionada
                        )[variable]
                        .agg(
                            funcion_agrupacion
                        )
                        .dropna()
                        .sort_values(
                            ascending=False
                        )
                    )

                    if len(datos_interpretacion) > 0:

                        categoria_mayor = (
                            datos_interpretacion.index[0]
                        )

                        valor_mayor = (
                            datos_interpretacion.iloc[0]
                        )

                        categoria_menor = (
                            datos_interpretacion.index[-1]
                        )

                        valor_menor = (
                            datos_interpretacion.iloc[-1]
                        )

                        st.write(
                            f"**{variable}:** según el análisis "
                            f"seleccionado (**{tipo_analisis.lower()}**), "
                            f"la categoría **{categoria_mayor}** presenta "
                            f"el valor más alto con "
                            f"**{valor_mayor:,.8f}**, mientras que "
                            f"**{categoria_menor}** presenta el valor "
                            f"más bajo con "
                            f"**{valor_menor:,.8f}**."
                        )


        # ==========================================================
        # ÍTEM 10: HALLAZGOS CLAVE
        # ==========================================================

        with tabs[9]:

            st.write(
                "En este apartado se resumen los principales hallazgos "
                "obtenidos durante el análisis exploratorio de datos. "
                "Los resultados permiten identificar características "
                "relevantes del dataset y posibles relaciones entre "
                "las variables analizadas."
            )

            # ----------------------------------------------------------
            # 1. VISUALIZACIÓN RESUMEN
            # ----------------------------------------------------------

            st.markdown(
                "### 1. Visualización resumen"
            )

            total_registros = len(df)

            total_variables = len(
                df.columns
            )

            variables_con_nulos = (
                df.isnull().sum()
            )

            cantidad_variables_nulos = (
                variables_con_nulos[
                    variables_con_nulos > 0
                ]
                .count()
            )

            porcentaje_renovacion = (
                df["renewal"].mean() * 100
            )

            promedio_primas = (
                df["no_of_premiums_paid"].mean()
            )

            col1, col2, col3, col4 = st.columns(4)

            with col1:

                st.metric(
                    "Registros",
                    f"{total_registros:,}"
                )

            with col2:

                st.metric(
                    "Variables",
                    total_variables
                )

            with col3:

                st.metric(
                    "Variables con nulos",
                    cantidad_variables_nulos
                )

            with col4:

                st.metric(
                    "Renovación",
                    f"{porcentaje_renovacion:.2f}%"
                )

            # ----------------------------------------------------------
            # 2. PRINCIPALES INSIGHTS
            # ----------------------------------------------------------

            st.markdown(
                "### 2. Insights principales derivados del EDA"
            )

            st.write(
                f"**• Estructura del dataset:** el conjunto de datos "
                f"contiene **{total_registros:,} registros y "
                f"{total_variables} variables**, lo que proporciona "
                "una base amplia para realizar análisis descriptivos."
            )

            if cantidad_variables_nulos > 0:

                variables_nulas_lista = (
                    variables_con_nulos[
                        variables_con_nulos > 0
                    ]
                    .index
                    .tolist()
                )

                st.write(
                    f"**• Valores faltantes:** se identificaron "
                    f"valores faltantes en **{cantidad_variables_nulos} "
                    f"variables**: **{', '.join(variables_nulas_lista)}**."
                )

            else:

                st.write(
                    "**• Valores faltantes:** no se identificaron "
                    "valores faltantes."
                )

            # ----------------------------------------------------------
            # Income
            # ----------------------------------------------------------

            media_income = (
                analizador.media("Income")
            )

            mediana_income = (
                analizador.mediana("Income")
            )

            if media_income > mediana_income:

                interpretacion_income = (
                    "La media es superior a la mediana, lo que indica "
                    "una posible asimetría hacia valores altos."
                )

            elif media_income < mediana_income:

                interpretacion_income = (
                    "La media es inferior a la mediana, lo que indica "
                    "una posible asimetría hacia valores bajos."
                )

            else:

                interpretacion_income = (
                    "La media y la mediana presentan valores similares."
                )

            st.write(
                f"**• Income:** el ingreso promedio es de "
                f"**{media_income:,.2f}**, mientras que la mediana es "
                f"**{mediana_income:,.2f}**. "
                f"{interpretacion_income}"
            )

            # ----------------------------------------------------------
            # Renovación
            # ----------------------------------------------------------

            st.write(
                f"**• Renovación:** aproximadamente el "
                f"**{porcentaje_renovacion:.2f}%** de los registros "
                "corresponde a clientes que renovaron."
            )

            # ----------------------------------------------------------
            # Primas
            # ----------------------------------------------------------

            st.write(
                f"**• Primas pagadas:** en promedio, los clientes "
                f"han pagado **{promedio_primas:.2f} primas**. "
                "Esta variable presentó diferencias al comparar "
                "los grupos de renovación."
            )

            # ----------------------------------------------------------
            # 3. CONCLUSIÓN GENERAL
            # ----------------------------------------------------------

            st.markdown(
                "### 3. Conclusión general"
            )

            st.write(
                "El análisis exploratorio permitió conocer la estructura "
                "del dataset, identificar los tipos de variables, revisar "
                "la calidad de los datos y analizar la distribución y "
                "relación entre diferentes variables. Los resultados "
                "muestran que variables como **Income**, "
                "**no_of_premiums_paid**, **residence_area_type** y "
                "**sourcing_channel** presentan diferencias según el "
                "comportamiento de renovación. Estas diferencias "
                "representan asociaciones observadas en los datos y "
                "no implican necesariamente una relación causal."
            )

# ==========================================
# MODULO 3: CONCLUSIONES FINALES
# ==========================================

elif modulos == "Conclusiones Finales":

    st.sidebar.image(
        "modulo3.jpg",
        use_container_width=True
    )

    st.title("Conclusiones Finales")

    st.write(
        "A partir del análisis exploratorio realizado sobre el dataset de seguros, "
        "se presentan las principales conclusiones orientadas a la interpretación "
        "de la información y a la toma de decisiones."
    )

    st.markdown("---")

    # ==========================================
    # CONCLUSIÓN 1
    # ==========================================

    st.subheader("1. Características económicas de los clientes")

    st.write(
        "El análisis de variables como Income y premium permite identificar "
        "diferencias en las características económicas de los clientes. "
        "La comparación entre medidas como la media y la mediana evidencia "
        "que la distribución de los ingresos puede presentar diferencias "
        "entre los valores centrales y los valores extremos."
    )

    st.info(
        "Implicancia para la toma de decisiones: "
        "la compañía puede utilizar esta información para segmentar mejor "
        "sus estrategias comerciales y evaluar si las características "
        "económicas de los clientes deben considerarse al diseñar productos "
        "o condiciones de renovación."
    )

    # ==========================================
    # CONCLUSIÓN 2
    # ==========================================

    st.subheader("2. El comportamiento de pago es relevante para el análisis")

    st.write(
        "Las variables relacionadas con el historial de pagos y los periodos "
        "de atraso permiten identificar diferentes comportamientos entre los "
        "clientes. La presencia de registros con distintos niveles de atraso "
        "muestra que el comportamiento histórico de pago constituye una "
        "característica importante dentro del análisis de la cartera."
    )

    st.info(
        "Implicancia para la toma de decisiones: "
        "es recomendable fortalecer el seguimiento de los clientes según "
        "su comportamiento de pago, priorizando acciones de comunicación "
        "y gestión para aquellos segmentos que presenten mayores señales "
        "de incumplimiento."
    )

    # ==========================================
    # CONCLUSIÓN 3
    # ==========================================

    st.subheader("3. Existen diferencias entre los grupos según renewal")

    st.write(
        "El análisis bivariado permitió comparar variables numéricas entre "
        "clientes con renewal igual a 0 y renewal igual a 1. Las diferencias "
        "observadas en variables como Income y no_of_premiums_paid muestran "
        "que los grupos presentan características distintas en términos "
        "económicos y de comportamiento dentro de la cartera."
    )

    st.info(
        "Implicancia para la toma de decisiones: "
        "estas diferencias pueden ser utilizadas como insumo para diseñar "
        "estrategias diferenciadas de atención, comunicación y fidelización "
        "para los distintos grupos de clientes."
    )

    # ==========================================
    # CONCLUSIÓN 4
    # ==========================================

    st.subheader("4. El canal de captación y el tipo de residencia muestran diferencias")

    st.write(
        "El análisis de variables categóricas permitió observar diferencias "
        "en la distribución de renewal según el sourcing_channel y "
        "residence_area_type. Esto indica que las características del canal "
        "de captación y del tipo de residencia pueden estar asociadas con "
        "distintos comportamientos dentro de la cartera analizada."
    )

    st.info(
        "Implicancia para la toma de decisiones: "
        "la compañía puede evaluar el desempeño de sus canales de captación "
        "y adaptar sus estrategias de comunicación y fidelización considerando "
        "las características de los diferentes segmentos."
    )

    # ==========================================
    # CONCLUSIÓN 5
    # ==========================================

    st.subheader("5. La calidad de los datos debe considerarse en la gestión")

    st.write(
        "El análisis de valores faltantes evidenció que algunas variables "
        "presentan registros incompletos, principalmente aquellas relacionadas "
        "con el historial de atrasos y el application_underwriting_score. "
        "Esto representa un aspecto importante al momento de interpretar los "
        "resultados obtenidos."
    )

    st.info(
        "Implicancia para la toma de decisiones: "
        "se recomienda fortalecer los procesos de captura, validación y "
        "mantenimiento de la información para mejorar la calidad de los datos "
        "y facilitar análisis posteriores que sirvan como soporte para la "
        "gestión de la cartera."
    )

    # ==========================================
    # CIERRE
    # ==========================================

    st.markdown("---")

    st.success(
        "En conjunto, el análisis exploratorio permite identificar diferencias "
        "económicas, de comportamiento de pago y de características de los "
        "clientes. Estos resultados constituyen información de apoyo para "
        "la toma de decisiones comerciales y de gestión de la cartera, "
        "sin establecer relaciones de causalidad."
    )
