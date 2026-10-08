import streamlit as st
import numpy as np
import pandas as pd
import io
import matplotlib.pyplot as plt


# ==========================================================
# CONFIGURACIÓN DE LA PÁGINA
# ==========================================================

st.set_page_config(
    page_title="Análisis Exploratorio de Datos",
    layout="wide"
)


# ==========================================================
# CLASE PARA EL ANÁLISIS DE DATOS - POO
# ==========================================================

class DataAnalyzer:

    def __init__(self, df):
        self.df = df

    # ------------------------------------------------------
    # Clasificación de variables
    # ------------------------------------------------------

    def clasificar_variables(self):

        variables_numericas = []
        variables_categoricas = []

        for columna in self.df.columns:

            if pd.api.types.is_numeric_dtype(self.df[columna]):
                variables_numericas.append(columna)

            else:
                variables_categoricas.append(columna)

        return variables_numericas, variables_categoricas

    # ------------------------------------------------------
    # Estadísticas descriptivas
    # ------------------------------------------------------

    def estadisticas_descriptivas(self):
        return self.df.describe()

    # ------------------------------------------------------
    # Media
    # ------------------------------------------------------

    def media(self, variable):
        return self.df[variable].mean()

    # ------------------------------------------------------
    # Mediana
    # ------------------------------------------------------

    def mediana(self, variable):
        return self.df[variable].median()

    # ------------------------------------------------------
    # Moda
    # ------------------------------------------------------

    def moda(self, variable):
        return self.df[variable].mode()

    # ------------------------------------------------------
    # Valores faltantes
    # ------------------------------------------------------

    def valores_faltantes(self):
        return self.df.isnull().sum()

    # ------------------------------------------------------
    # Visualización: Histograma
    # ------------------------------------------------------

    def graficar_histograma(self, variable, bins=30):

        fig, ax = plt.subplots(figsize=(8, 4))

        ax.hist(
            self.df[variable].dropna(),
            bins=bins,
            edgecolor="black"
        )

        ax.set_title(f"Distribución de {variable}")
        ax.set_xlabel(variable)
        ax.set_ylabel("Frecuencia")
        ax.grid(axis="y", alpha=0.3)

        return fig

    # ------------------------------------------------------
    # Visualización: Barras
    # ------------------------------------------------------

    def graficar_barras(self, variable):

        frecuencias = (
            self.df[variable]
            .value_counts(dropna=False)
        )

        fig, ax = plt.subplots(figsize=(8, 4))

        frecuencias.plot(
            kind="bar",
            ax=ax
        )

        ax.set_title(f"Distribución de {variable}")
        ax.set_xlabel(variable)
        ax.set_ylabel("Frecuencia")
        ax.tick_params(axis="x", rotation=45)

        plt.tight_layout()

        return fig


# ==========================================================
# SESSION STATE
# ==========================================================

if "df" not in st.session_state:
    st.session_state.df = None


# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.markdown("## 🎛️ Panel de Navegación")

modulos = st.sidebar.selectbox(
    "Seleccione la sección a consultar",
    [
        "Home",
        "Carga del Dataset",
        "Análisis Exploratorio de Datos"
    ]
)


# ==========================================================
# HOME
# ==========================================================

if modulos == "Home":

    st.title("📊 Análisis Exploratorio de Datos")

    st.write(
        """
        Aplicación desarrollada para realizar un análisis exploratorio
        de un dataset mediante Python y Streamlit.

        El proyecto incluye análisis de estructura, clasificación de
        variables, estadísticas descriptivas, valores faltantes,
        distribuciones, análisis bivariado y generación de hallazgos.
        """
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🐍 Lenguaje", "Python")

    with col2:
        st.metric("📊 Librería", "Pandas")

    with col3:
        st.metric("⚡ Framework", "Streamlit")


# ==========================================================
# CARGA DEL DATASET
# ==========================================================

elif modulos == "Carga del Dataset":

    st.title("📂 Carga del Dataset")

    archivo = st.file_uploader(
        "Selecciona un archivo CSV",
        type=["csv"]
    )

    if archivo is not None:

        try:

            df = pd.read_csv(archivo)

            if df.empty:

                st.error(
                    "El archivo no contiene registros."
                )

            else:

                st.session_state.df = df

                st.success(
                    "Dataset cargado correctamente."
                )

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "Número de registros",
                        f"{df.shape[0]:,}"
                    )

                with col2:
                    st.metric(
                        "Número de variables",
                        df.shape[1]
                    )

                st.subheader("Primeras 5 filas")

                st.dataframe(
                    df.head(),
                    use_container_width=True
                )

        except Exception as e:

            st.error(
                f"No fue posible cargar el archivo: {e}"
            )


# ==========================================================
# ANÁLISIS EXPLORATORIO DE DATOS
# ==========================================================

elif modulos == "Análisis Exploratorio de Datos":

    st.title("📈 Análisis Exploratorio de Datos")

    if st.session_state.df is None:

        st.warning(
            "Primero debes cargar un dataset desde "
            "la sección 'Carga del Dataset'."
        )

    else:

        # Recuperar dataset
        df = st.session_state.df

        # Instanciar clase
        analizador = DataAnalyzer(df)

        # Clasificación mediante POO
        variables_numericas, variables_categoricas = (
            analizador.clasificar_variables()
        )

        # ==================================================
        # TABS
        # ==================================================

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


        # ==================================================
        # ÍTEM 1: INFORMACIÓN GENERAL DEL DATASET
        # ==================================================

        with tabs[0]:

            st.header("1. Información general del dataset")

            st.write(
                """
                En este análisis se revisa la estructura general del
                dataset, los tipos de datos de sus variables y la
                presencia de valores nulos.
                """
            )

            # ----------------------------------------------
            # Información general
            # ----------------------------------------------

            buffer = io.StringIO()

            df.info(buf=buffer)

            st.code(
                buffer.getvalue(),
                language="text"
            )

            # ----------------------------------------------
            # Tipos de datos
            # ----------------------------------------------

            tipos_datos = (
                df.dtypes.astype(str)
                .value_counts()
                .reset_index()
            )

            tipos_datos.columns = [
                "Tipo de dato",
                "Cantidad de columnas"
            ]

            # ----------------------------------------------
            # Valores nulos
            # ----------------------------------------------

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

                st.subheader("Tipos de datos")

                st.dataframe(
                    tipos_datos,
                    use_container_width=True
                )

            with col2:

                st.subheader("Valores nulos")

                st.dataframe(
                    nulos,
                    use_container_width=True
                )

            # ----------------------------------------------
            # Gráfico de tipos de datos
            # ----------------------------------------------

            st.subheader("Distribución de tipos de datos")

            st.bar_chart(
                tipos_datos.set_index("Tipo de dato")
            )

            total_nulos = df.isnull().sum().sum()

            if total_nulos > 0:

                st.warning(
                    f"El dataset contiene {total_nulos:,} "
                    "valores faltantes."
                )

            else:

                st.success(
                    "El dataset no contiene valores faltantes."
                )


        # ==================================================
        # ÍTEM 2: CLASIFICACIÓN DE VARIABLES
        # ==================================================

        with tabs[1]:

            st.header("2. Clasificación de variables")

            st.write(
                """
                Las variables se clasifican automáticamente según
                su tipo de dato utilizando la clase DataAnalyzer.
                """
            )

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Variables numéricas",
                    len(variables_numericas)
                )

                st.dataframe(
                    pd.DataFrame({
                        "Variables numéricas":
                            variables_numericas
                    }),
                    use_container_width=True
                )

            with col2:

                st.metric(
                    "Variables categóricas",
                    len(variables_categoricas)
                )

                st.dataframe(
                    pd.DataFrame({
                        "Variables categóricas":
                            variables_categoricas
                    }),
                    use_container_width=True
                )

            st.subheader("Resumen de clasificación")

            resumen_variables = pd.DataFrame({
                "Tipo de variable": [
                    "Numérica",
                    "Categórica"
                ],
                "Cantidad": [
                    len(variables_numericas),
                    len(variables_categoricas)
                ]
            })

            st.bar_chart(
                resumen_variables.set_index(
                    "Tipo de variable"
                )
            )


        # ==================================================
        # ÍTEM 3: ESTADÍSTICAS DESCRIPTIVAS
        # ==================================================

        with tabs[2]:

            st.header("3. Estadísticas descriptivas")

            st.write(
                """
                Se presentan las estadísticas descriptivas de las
                variables numéricas y se interpretan medidas de
                tendencia central y dispersión.
                """
            )

            # ----------------------------------------------
            # Estadísticas mediante POO
            # ----------------------------------------------

            estadisticas = (
                analizador.estadisticas_descriptivas()
            )

            st.subheader("Resumen estadístico")

            st.dataframe(
                estadisticas,
                use_container_width=True
            )

            # ----------------------------------------------
            # Variables representativas
            # ----------------------------------------------

            st.subheader(
                "Interpretación de variables representativas"
            )

            variables_representativas = [
                variable
                for variable in ["Income", "premium"]
                if variable in df.columns
            ]

            for variable in variables_representativas:

                media = analizador.media(variable)
                mediana = analizador.mediana(variable)
                desviacion = df[variable].std()

                st.write(f"### {variable}")

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric(
                        "Media",
                        f"{media:,.2f}"
                    )

                with col2:
                    st.metric(
                        "Mediana",
                        f"{mediana:,.2f}"
                    )

                with col3:
                    st.metric(
                        "Desviación estándar",
                        f"{desviacion:,.2f}"
                    )

                if media > mediana:

                    st.info(
                        f"En **{variable}**, la media es mayor que "
                        "la mediana, lo que puede indicar una "
                        "distribución con asimetría positiva."
                    )

                elif media < mediana:

                    st.info(
                        f"En **{variable}**, la media es menor que "
                        "la mediana, lo que puede indicar una "
                        "distribución con asimetría negativa."
                    )

                else:

                    st.info(
                        f"En **{variable}**, la media y la mediana "
                        "son similares, lo que sugiere una "
                        "distribución relativamente equilibrada."
                    )

                st.write(
                    f"La desviación estándar de **{variable}** "
                    f"es {desviacion:,.2f}, por lo que existe "
                    "variabilidad alrededor de su media."
                )

            # ----------------------------------------------
            # Moda
            # ----------------------------------------------

            if len(variables_categoricas) > 0:

                variable_moda = variables_categoricas[0]

                moda = analizador.moda(variable_moda)

                if not moda.empty:

                    st.subheader("Moda")

                    st.write(
                        f"La moda de **{variable_moda}** es "
                        f"**{moda.iloc[0]}**, es decir, "
                        "es la categoría que aparece con mayor "
                        "frecuencia."
                    )


        # ==================================================
        # ÍTEM 4: VALORES FALTANTES
        # ==================================================

        with tabs[3]:

            st.header("4. Análisis de valores faltantes")

            valores_faltantes = (
                analizador.valores_faltantes()
            )

            tabla_faltantes = pd.DataFrame({
                "Variable": valores_faltantes.index,
                "Valores faltantes":
                    valores_faltantes.values
            })

            st.dataframe(
                tabla_faltantes,
                use_container_width=True
            )

            total_faltantes = valores_faltantes.sum()

            if total_faltantes > 0:

                st.warning(
                    f"Se encontraron {total_faltantes:,} "
                    "valores faltantes."
                )

                faltantes_grafico = (
                    valores_faltantes[
                        valores_faltantes > 0
                    ]
                    .sort_values(ascending=False)
                )

                st.subheader(
                    "Variables con valores faltantes"
                )

                st.bar_chart(
                    faltantes_grafico
                )

                st.write(
                    """
                    Los valores faltantes deben ser considerados
                    antes de realizar modelos predictivos o análisis
                    estadísticos que requieran datos completos.
                    """
                )

            else:

                st.success(
                    "No se identificaron valores faltantes."
                )


        # ==================================================
        # ÍTEM 5: DISTRIBUCIÓN DE VARIABLES NUMÉRICAS
        # ==================================================

        with tabs[4]:

            st.header(
                "5. Distribución de variables numéricas"
            )

            st.write(
                """
                Los histogramas permiten observar la forma de la
                distribución, concentración de los datos,
                dispersión y posibles valores extremos.
                """
            )

            # ----------------------------------------------
            # MULTISELECT
            # ----------------------------------------------

            variables_histograma = st.multiselect(
                "Selecciona las variables que deseas visualizar:",
                variables_numericas,
                default=variables_numericas[:2]
            )

            # ----------------------------------------------
            # SLIDER
            # ----------------------------------------------

            numero_bins = st.slider(
                "Selecciona el número de intervalos "
                "del histograma:",
                min_value=5,
                max_value=50,
                value=30,
                step=5
            )

            # ----------------------------------------------
            # CHECKBOX
            # ----------------------------------------------

            mostrar_interpretacion = st.checkbox(
                "Mostrar interpretación estadística",
                value=True
            )

            if len(variables_histograma) == 0:

                st.info(
                    "Selecciona al menos una variable "
                    "para visualizar su distribución."
                )

            else:

                for variable in variables_histograma:

                    st.subheader(
                        f"Distribución de {variable}"
                    )

                    fig = (
                        analizador
                        .graficar_histograma(
                            variable,
                            numero_bins
                        )
                    )

                    st.pyplot(fig)

                    plt.close(fig)

                # ------------------------------------------
                # Interpretación
                # ------------------------------------------

                if mostrar_interpretacion:

                    st.subheader(
                        "Interpretación estadística"
                    )

                    for variable in variables_histograma:

                        media = analizador.media(variable)
                        mediana = analizador.mediana(variable)
                        desviacion = df[variable].std()
                        minimo = df[variable].min()
                        maximo = df[variable].max()

                        q1 = df[variable].quantile(0.25)
                        q3 = df[variable].quantile(0.75)

                        st.write(
                            f"**{variable}:**"
                        )

                        st.write(
                            f"- Media: {media:,.2f}"
                        )

                        st.write(
                            f"- Mediana: {mediana:,.2f}"
                        )

                        st.write(
                            f"- Desviación estándar: "
                            f"{desviacion:,.2f}"
                        )

                        st.write(
                            f"- Rango observado: "
                            f"{minimo:,.2f} a {maximo:,.2f}"
                        )

                        st.write(
                            f"- Rango intercuartílico: "
                            f"{q1:,.2f} a {q3:,.2f}"
                        )

                        if media > mediana:

                            st.info(
                                "La media es mayor que la mediana, "
                                "lo que puede indicar una "
                                "asimetría hacia valores altos."
                            )

                        elif media < mediana:

                            st.info(
                                "La media es menor que la mediana, "
                                "lo que puede indicar una "
                                "asimetría hacia valores bajos."
                            )

                        else:

                            st.info(
                                "La media y la mediana presentan "
                                "valores similares."
                            )

                        st.write(
                            "La desviación estándar permite evaluar "
                            "la dispersión de los datos, mientras "
                            "que el rango y los cuartiles permiten "
                            "identificar la amplitud y concentración "
                            "de los valores."
                        )


        # ==================================================
        # ÍTEM 6: VARIABLES CATEGÓRICAS
        # ==================================================

        with tabs[5]:

            st.header(
                "6. Análisis de variables categóricas"
            )

            for variable in variables_categoricas:

                st.subheader(variable)

                frecuencias = (
                    df[variable]
                    .value_counts(dropna=False)
                )

                proporciones = (
                    df[variable]
                    .value_counts(
                        dropna=False,
                        normalize=True
                    ) * 100
                )

                tabla_categorica = pd.DataFrame({
                    "Frecuencia": frecuencias,
                    "Proporción (%)":
                        proporciones.round(2)
                })

                st.dataframe(
                    tabla_categorica,
                    use_container_width=True
                )

                st.bar_chart(
                    frecuencias
                )

                # ------------------------------------------
                # Moda
                # ------------------------------------------

                moda = analizador.moda(variable)

                if not moda.empty:

                    categoria_moda = moda.iloc[0]

                    frecuencia_moda = frecuencias.loc[
                        categoria_moda
                    ]

                    porcentaje_moda = (
                        frecuencia_moda /
                        len(df) * 100
                    )

                    st.write(
                        f"**Moda:** {categoria_moda}"
                    )

                    st.write(
                        f"La categoría más frecuente representa "
                        f"aproximadamente el "
                        f"**{porcentaje_moda:.2f}%** de los registros."
                    )


        # ==================================================
        # ÍTEM 7: NUMÉRICO VS CATEGÓRICO
        # ==================================================

        with tabs[6]:

            st.header(
                "7. Análisis bivariado: numérico vs categórico"
            )

            st.write(
                """
                Se comparan variables numéricas entre los grupos
                definidos por la variable de renovación.
                """
            )

            variables_comparacion = [
                variable
                for variable in [
                    "Income",
                    "no_of_premiums_paid"
                ]
                if variable in df.columns
            ]

            if "renewal" in df.columns:

                for variable in variables_comparacion:

                    st.subheader(
                        f"{variable} según renovación"
                    )

                    resumen = (
                        df.groupby("renewal")[variable]
                        .agg([
                            "mean",
                            "median",
                            "min",
                            "max"
                        ])
                        .round(2)
                    )

                    st.dataframe(
                        resumen,
                        use_container_width=True
                    )

                    st.bar_chart(
                        resumen["mean"]
                    )

                    if 0 in resumen.index and 1 in resumen.index:

                        diferencia = (
                            resumen.loc[1, "mean"]
                            - resumen.loc[0, "mean"]
                        )

                        if diferencia > 0:

                            st.info(
                                f"El grupo con renovación = 1 "
                                f"presenta un promedio de "
                                f"{diferencia:,.2f} unidades "
                                "mayor."
                            )

                        elif diferencia < 0:

                            st.info(
                                f"El grupo con renovación = 1 "
                                f"presenta un promedio de "
                                f"{abs(diferencia):,.2f} unidades "
                                "menor."
                            )

                        else:

                            st.info(
                                "Los promedios de ambos grupos "
                                "son iguales."
                            )

                st.caption(
                    "La comparación identifica diferencias o "
                    "asociaciones entre grupos, pero no implica "
                    "necesariamente una relación causal."
                )


        # ==================================================
        # ÍTEM 8: CATEGÓRICO VS CATEGÓRICO
        # ==================================================

        with tabs[7]:

            st.header(
                "8. Análisis bivariado: categórico vs categórico"
            )

            if "renewal" in df.columns:

                variables_categoricas_comparacion = [
                    variable
                    for variable in [
                        "residence_area_type",
                        "sourcing_channel"
                    ]
                    if variable in df.columns
                ]

                for variable in (
                    variables_categoricas_comparacion
                ):

                    st.subheader(
                        f"{variable} vs renovación"
                    )

                    # --------------------------------------
                    # Tabla de frecuencias
                    # --------------------------------------

                    tabla_frecuencias = pd.crosstab(
                        df[variable],
                        df["renewal"]
                    )

                    st.write("Frecuencias:")

                    st.dataframe(
                        tabla_frecuencias,
                        use_container_width=True
                    )

                    # --------------------------------------
                    # Proporciones
                    # --------------------------------------

                    tabla_proporciones = pd.crosstab(
                        df[variable],
                        df["renewal"],
                        normalize="index"
                    ) * 100

                    st.write(
                        "Proporción de renovación por categoría (%):"
                    )

                    st.dataframe(
                        tabla_proporciones.round(2),
                        use_container_width=True
                    )

                    # --------------------------------------
                    # Gráfico
                    # --------------------------------------

                    st.bar_chart(
                        tabla_proporciones
                    )

                    # --------------------------------------
                    # Interpretación
                    # --------------------------------------

                    if 1 in tabla_proporciones.columns:

                        categoria_mayor = (
                            tabla_proporciones[1]
                            .idxmax()
                        )

                        porcentaje_mayor = (
                            tabla_proporciones[1]
                            .max()
                        )

                        st.info(
                            f"La categoría **{categoria_mayor}** "
                            f"presenta el mayor porcentaje de "
                            f"renovación, con aproximadamente "
                            f"**{porcentaje_mayor:.2f}%**."
                        )

                st.caption(
                    "Las diferencias observadas representan "
                    "asociaciones entre variables categóricas y "
                    "no permiten establecer causalidad por sí solas."
                )


        # ==================================================
        # ÍTEM 9: ANÁLISIS BASADO EN PARÁMETROS
        # ==================================================

        with tabs[8]:

            st.header(
                "9. Análisis basado en parámetros seleccionados"
            )

            st.write(
                """
                Esta sección permite seleccionar dinámicamente
                una variable categórica, una o varias variables
                numéricas y la medida estadística que se desea
                analizar.
                """
            )

            # ----------------------------------------------
            # SELECTBOX
            # ----------------------------------------------

            variable_categorica_seleccionada = st.selectbox(
                "Selecciona la variable categórica:",
                variables_categoricas
            )

            # ----------------------------------------------
            # MULTISELECT
            # ----------------------------------------------

            variables_numericas_seleccionadas = st.multiselect(
                "Selecciona las variables numéricas:",
                variables_numericas,
                default=variables_numericas[:2]
            )

            # ----------------------------------------------
            # SELECTBOX PARA EL TIPO DE ANÁLISIS
            # ----------------------------------------------

            tipo_analisis = st.selectbox(
                "Selecciona la medida estadística:",
                [
                    "Media",
                    "Mediana",
                    "Mínimo",
                    "Máximo"
                ]
            )

            if len(variables_numericas_seleccionadas) == 0:

                st.info(
                    "Selecciona al menos una variable numérica."
                )

            else:

                resultados = []

                for variable in (
                    variables_numericas_seleccionadas
                ):

                    if tipo_analisis == "Media":

                        serie = (
                            df.groupby(
                                variable_categorica_seleccionada
                            )[variable]
                            .mean()
                        )

                    elif tipo_analisis == "Mediana":

                        serie = (
                            df.groupby(
                                variable_categorica_seleccionada
                            )[variable]
                            .median()
                        )

                    elif tipo_analisis == "Mínimo":

                        serie = (
                            df.groupby(
                                variable_categorica_seleccionada
                            )[variable]
                            .min()
                        )

                    else:

                        serie = (
                            df.groupby(
                                variable_categorica_seleccionada
                            )[variable]
                            .max()
                        )

                    serie = serie.round(8)

                    tabla_resultado = (
                        serie
                        .reset_index()
                    )

                    tabla_resultado.columns = [
                        variable_categorica_seleccionada,
                        variable
                    ]

                    resultados.append(
                        tabla_resultado
                    )

                    st.subheader(
                        f"{tipo_analisis} de {variable} "
                        f"por {variable_categorica_seleccionada}"
                    )

                    st.dataframe(
                        tabla_resultado,
                        use_container_width=True
                    )

                    st.bar_chart(
                        serie
                    )

                    # --------------------------------------
                    # Interpretación dinámica
                    # --------------------------------------

                    categoria_max = serie.idxmax()
                    valor_max = serie.max()

                    categoria_min = serie.idxmin()
                    valor_min = serie.min()

                    st.write(
                        f"La categoría **{categoria_max}** "
                        f"presenta el valor más alto "
                        f"({valor_max:,.8f}), mientras que "
                        f"**{categoria_min}** presenta el "
                        f"valor más bajo "
                        f"({valor_min:,.8f})."
                    )

                st.success(
                    "El análisis se actualiza dinámicamente "
                    "según los parámetros seleccionados."
                )


        # ==================================================
        # ÍTEM 10: HALLAZGOS CLAVE
        # ==================================================

        with tabs[9]:

            st.header("10. Hallazgos clave")

            # ----------------------------------------------
            # Indicadores generales
            # ----------------------------------------------

            total_registros = len(df)
            total_variables = len(df.columns)

            variables_con_nulos = (
                df.columns[
                    df.isnull().sum() > 0
                ].tolist()
            )

            if "renewal" in df.columns:

                porcentaje_renovacion = (
                    df["renewal"]
                    .mean() * 100
                )

            else:

                porcentaje_renovacion = np.nan

            col1, col2, col3, col4 = st.columns(4)

            with col1:

                st.metric(
                    "Total de registros",
                    f"{total_registros:,}"
                )

            with col2:

                st.metric(
                    "Total de variables",
                    total_variables
                )

            with col3:

                st.metric(
                    "Variables con nulos",
                    len(variables_con_nulos)
                )

            with col4:

                if not np.isnan(porcentaje_renovacion):

                    st.metric(
                        "% de renovación",
                        f"{porcentaje_renovacion:.2f}%"
                    )

            # ----------------------------------------------
            # Hallazgos
            # ----------------------------------------------

            st.subheader(
                "Principales hallazgos"
            )

            # Estructura

            st.write(
                f"""
                **1. Estructura del dataset:** el conjunto de datos
                contiene **{total_registros:,} registros** y
                **{total_variables} variables**.
                """
            )

            # Valores faltantes

            if len(variables_con_nulos) > 0:

                st.write(
                    f"""
                    **2. Valores faltantes:** se identificaron
                    valores faltantes en las variables:
                    **{", ".join(variables_con_nulos)}**.
                    """
                )

            else:

                st.write(
                    """
                    **2. Valores faltantes:** no se identificaron
                    valores faltantes en el dataset.
                    """
                )

            # Income

            if "Income" in df.columns:

                media_income = (
                    analizador.media("Income")
                )

                mediana_income = (
                    analizador.mediana("Income")
                )

                st.write(
                    f"""
                    **3. Income:** presenta una media de
                    **{media_income:,.2f}** y una mediana de
                    **{mediana_income:,.2f}**.
                    """
                )

                if media_income > mediana_income:

                    st.write(
                        "La diferencia entre ambas medidas "
                        "sugiere una posible asimetría positiva."
                    )

                elif media_income < mediana_income:

                    st.write(
                        "La diferencia entre ambas medidas "
                        "sugiere una posible asimetría negativa."
                    )

                else:

                    st.write(
                        "La media y la mediana presentan "
                        "valores similares."
                    )

            # Renovación

            if "renewal" in df.columns:

                st.write(
                    f"""
                    **4. Renovación:** aproximadamente el
                    **{porcentaje_renovacion:.2f}%** de los registros
                    corresponde al grupo con renovación = 1.
                    """
                )

            # Comparación

            if (
                "Income" in df.columns
                and "renewal" in df.columns
            ):

                income_renovacion = (
                    df.groupby("renewal")["Income"]
                    .mean()
                )

                if (
                    0 in income_renovacion.index
                    and 1 in income_renovacion.index
                ):

                    diferencia_income = (
                        income_renovacion.loc[1]
                        - income_renovacion.loc[0]
                    )

                    st.write(
                        f"""
                        **5. Comparación de grupos:** el ingreso
                        promedio presenta una diferencia de
                        **{diferencia_income:,.2f}** entre los
                        grupos con y sin renovación.
                        """
                    )

            # ----------------------------------------------
            # Conclusión general
            # ----------------------------------------------

            st.subheader(
                "Conclusión general"
            )

            st.success(
                """
                El análisis exploratorio permitió identificar la
                estructura del dataset, clasificar sus variables,
                evaluar medidas de tendencia central y dispersión,
                analizar distribuciones y comparar grupos.

                Las diferencias encontradas entre los grupos de
                renovación pueden ser utilizadas como punto de
                partida para análisis posteriores y modelos
                predictivos. Sin embargo, las asociaciones observadas
                no deben interpretarse como relaciones causales sin
                análisis estadísticos adicionales.
                """
            )
