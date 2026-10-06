import streamlit as st
import numpy as np
import libreria_funciones_proyecto1 as lf
import librería_clases_proyecto1 as lc

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
    ### 💡 Datos del Autor

    * Nombre completo: Stefany Salazar Espinoza 
    * Curso / Especialización: Especialización en Python for Analytics  
    * Año: 2026 """)

     st.markdown("""
    ### 💡 Explicación del Dataset

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
# EJERCICIO 1
# ==========================================

elif modulos == "Ejercicio 1":

    st.sidebar.markdown("---")

    st.sidebar.image(
        "image_ejercicio1.jpg",
        use_container_width=True
    )


    st.markdown("""
        <div class="custom-data-title">
            <h1>💰 Flujo de caja con listas</h1>
        </div>
    """, unsafe_allow_html=True)


    st.markdown("""
    ### Descripción del ejercicio

    En este ejercicio se desarrolla un módulo para el registro y control de movimientos de flujo de caja,
    utilizando listas de Python para almacenar y gestionar la información.
    Permite registrar ingresos y gastos, indicando el concepto y valor de cada movimiento. 
    A partir de los registros ingresados, se calculan automáticamente el total de ingresos, total de gastos
    y saldo final, permitiendo conocer el estado del flujo de caja.
    """)


    st.markdown("---")

    st.subheader("Registrar movimiento")


    concepto = st.text_input(
        "Ingrese el concepto del movimiento"
    )


    tipo = st.selectbox(
        "Seleccione el tipo de movimiento",
        ["Ingreso", "Gasto"]
    )


    valor = st.number_input(
        "Ingrese el valor",
        min_value=0.0,
        value=0.0,
        step=10.0
    )


    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []


    if st.button("Registrar movimiento"):

        if concepto != "" and valor > 0:

            movimiento = {
                "Concepto": concepto,
                "Tipo": tipo,
                "Valor": valor
            }

            st.session_state.movimientos.append(
                movimiento
            )

            st.success(
                "Movimiento registrado correctamente."
            )

        else:

            st.error(
                "Ingrese un concepto válido y un valor mayor que 0."
            )


    st.markdown("---")

    st.subheader("Movimientos registrados")


    if len(st.session_state.movimientos) > 0:

        col1, col2, col3, col4 = st.columns(
            [3, 2, 2, 1]
        )

        col1.markdown("**Concepto**")
        col2.markdown("**Tipo**")
        col3.markdown("**Valor**")
        col4.markdown("**Eliminar**")


        for i, movimiento in enumerate(
            st.session_state.movimientos
        ):

            col1, col2, col3, col4 = st.columns(
                [3, 2, 2, 1]
            )

            col1.write(
                movimiento["Concepto"]
            )

            col2.write(
                movimiento["Tipo"]
            )

            col3.write(
                f"S/ {movimiento['Valor']:,.2f}"
            )


            if col4.button(
                "🗑️",
                key=f"eliminar_movimiento_{i}"
            ):

                st.session_state.movimientos.pop(i)

                st.rerun()


        total_ingresos = sum(
            movimiento["Valor"]
            for movimiento in st.session_state.movimientos
            if movimiento["Tipo"] == "Ingreso"
        )


        total_gastos = sum(
            movimiento["Valor"]
            for movimiento in st.session_state.movimientos
            if movimiento["Tipo"] == "Gasto"
        )


        saldo_final = (
            total_ingresos - total_gastos
        )


        st.markdown("---")

        st.subheader(
            "Resumen del flujo de caja"
        )


        col_m1, col_m2, col_m3 = st.columns(3)


        col_m1.metric(
            "Total de ingresos",
            f"S/ {total_ingresos:,.2f}"
        )


        col_m2.metric(
            "Total de gastos",
            f"S/ {total_gastos:,.2f}"
        )


        col_m3.metric(
            "Saldo final",
            f"S/ {saldo_final:,.2f}"
        )


        if saldo_final > 0:

            st.success(
                "Flujo de caja: A FAVOR 📈"
            )

        elif saldo_final < 0:

            st.error(
                "Flujo de caja: EN CONTRA 📉"
            )

        else:

            st.info(
                "Flujo de caja: EN EQUILIBRIO ⚖️"
            )


        st.markdown("---")


        if st.button(
            "Borrar todos los movimientos"
        ):

            st.session_state.movimientos = []

            st.rerun()


    else:

        st.write(
            "No hay movimientos registrados."
        )


# ==========================================
# EJERCICIO 2
# ==========================================

elif modulos == "Ejercicio 2":

    st.sidebar.markdown("---")

    st.sidebar.image(
        "image_ejercicio2.jpg",
        use_container_width=True
    )


    st.markdown("""
        <div class="custom-data-title">
            <h1>📦 Formulario de registro de ventas</h1>
        </div>
    """, unsafe_allow_html=True)


    st.markdown("""
    ### Descripción del ejercicio

   En este ejercicio se desarrolla un módulo interactivo para el registro y control de ventas, utilizando arreglos de NumPy
   para almacenar y gestionar la información de los productos.
   La aplicación permite registrar el nombre del producto, categoría, precio y cantidad, calculando automáticamente el total
   de cada venta. Además, permite visualizar y gestionar los productos registrados.
    """)

    st.markdown("---")

    st.subheader("Registrar producto")


    nombre = st.text_input(
        "Ingrese el nombre del producto"
    )


    categoria = st.selectbox(
        "Seleccione la categoría",
        [
            "Limpieza",
            "Tecnología",
            "Alimentos",
            "Bebidas",
            "Otros"
        ]
    )


    precio = st.number_input(
        "Ingrese el precio",
        min_value=0.0,
        value=0.0,
        step=1.0
    )


    cantidad = st.number_input(
        "Ingrese la cantidad",
        min_value=1,
        value=1,
        step=1
    )


    if "productos" not in st.session_state:

        st.session_state.productos = np.empty(
            (0, 5),
            dtype=object
        )


    if st.button("Registrar producto"):

        if nombre != "" and precio > 0:

            total = precio * cantidad

            nuevo_producto = np.array(
                [[
                    nombre,
                    categoria,
                    precio,
                    cantidad,
                    total
                ]],
                dtype=object
            )


            st.session_state.productos = np.vstack(
                [
                    st.session_state.productos,
                    nuevo_producto
                ]
            )


            st.success(
                "Producto registrado correctamente."
            )

        else:

            st.error(
                "Ingrese un nombre válido y un precio mayor que 0."
            )


    st.markdown("---")

    st.subheader("Productos registrados")


    if len(st.session_state.productos) > 0:

        st.dataframe(
            st.session_state.productos,
            column_config={
                1: "Nombre",
                2: "Categoría",
                3: st.column_config.NumberColumn(
                    "Precio",
                    format="S/ %.2f"
                ),
                4: "Cantidad",
                5: st.column_config.NumberColumn(
                    "Total",
                    format="S/ %.2f"
                )
            },
            hide_index=True,
            use_container_width=True
        )


        st.markdown("---")

        st.subheader("Eliminar producto")


        nombres_productos = [
            producto[0]
            for producto in st.session_state.productos
        ]


        producto_seleccionado = st.selectbox(
            "Seleccione el producto que desea eliminar",
            nombres_productos
        )


        col_elim1, col_elim2 = st.columns(2)


        with col_elim1:

            if st.button(
                "Eliminar producto seleccionado"
            ):

                indice = nombres_productos.index(
                    producto_seleccionado
                )


                st.session_state.productos = np.delete(
                    st.session_state.productos,
                    indice,
                    axis=0
                )


                st.rerun()


        with col_elim2:

            if st.button(
                "Borrar todo el inventario"
            ):

                st.session_state.productos = np.empty(
                    (0, 5),
                    dtype=object
                )

                st.rerun()


    else:

        st.write(
            "No hay productos registrados."
        )


# ==========================================
# EJERCICIO 3
# ==========================================

elif modulos == "Ejercicio 3":

    st.sidebar.markdown("---")

    st.sidebar.image(
        "image_ejercicio3.jpg",
        use_container_width=True
    )


    st.markdown("""
        <div class="custom-data-title">
            <h1>📊 Cálculo de tasa de error de transacciones</h1>
        </div>
    """, unsafe_allow_html=True)


    st.markdown("""
    ### Descripción del ejercicio

    En este ejercicio se desarrolla un módulo para analizar el desempeño de un conjunto de transacciones, utilizando una función definida
    en una librería externa de Python.
    La aplicación permite ingresar el periodo de análisis, número de transacciones fallidas y número total de transacciones. 
    A partir de estos datos, la función calcula automáticamente la tasa de error y la tasa de éxito, mostrando los resultados obtenidos de
    manera interactiva. Asimismo, se mantiene un histórico de los análisis realizados, permitiendo visualizar y gestionar los resultados
    registrados.
    """)


    st.markdown("---")

    st.subheader("Seleccionar función")


    funcion = st.selectbox(
        "Seleccione la función que desea ejecutar",
        [
            "Calcular tasa de error de transacciones"
        ]
    )


    if funcion == "Calcular tasa de error de transacciones":

        st.subheader("Ingresar parámetros")


        periodo = st.text_input(
            "Ingrese el periodo del análisis"
        )


        transacciones_fallidas = st.number_input(
            "Número de transacciones fallidas",
            min_value=0,
            value=0,
            step=1
        )


        transacciones_totales = st.number_input(
            "Número de transacciones totales",
            min_value=1,
            value=1,
            step=1
        )


        if st.button("Ejecutar función"):

            if periodo == "":

                st.write(
                    "Debe ingresar el periodo del análisis."
                )

            else:

                try:

                    resultado = (
                        lf.calcular_tasa_error_transacciones(
                            transacciones_fallidas,
                            transacciones_totales
                        )
                    )


                    st.write(
                        "Función ejecutada correctamente."
                    )


                    st.subheader(
                        f"Resultado - {periodo}"
                    )


                    st.write(
                        f"Tasa de error: "
                        f"{resultado['tasa_error_pct']:.4f}%"
                    )


                    st.write(
                        f"Tasa de éxito: "
                        f"{resultado['tasa_exito_pct']:.4f}%"
                    )


                    if "historico_tasa_error" not in st.session_state:

                        st.session_state.historico_tasa_error = []


                    registro = {
                        "Periodo": periodo,
                        "Transacciones fallidas": transacciones_fallidas,
                        "Transacciones totales": transacciones_totales,
                        "Tasa de error (%)": resultado[
                            "tasa_error_pct"
                        ],
                        "Tasa de éxito (%)": resultado[
                            "tasa_exito_pct"
                        ]
                    }


                    st.session_state.historico_tasa_error.append(
                        registro
                    )


                except ValueError as e:

                    st.write(str(e))


    st.markdown("---")

    st.subheader("Histórico de resultados")


    if (
        "historico_tasa_error" in st.session_state
        and len(
            st.session_state.historico_tasa_error
        ) > 0
    ):

        st.dataframe(
            st.session_state.historico_tasa_error,
            use_container_width=True
        )


        if st.button(
            "Eliminar todos los registros"
        ):

            st.session_state.historico_tasa_error = []

            st.rerun()


    else:

        st.write(
            "No hay resultados registrados."
        )


# ==========================================
# EJERCICIO 4
# ==========================================

elif modulos == "Ejercicio 4":

    st.sidebar.markdown("---")

    st.sidebar.image(
        "image_ejercicio4.jpg",
        use_container_width=True
    )

    st.markdown("""
        <div class="custom-data-title">
            <h1>🏥 Gestión de pacientes</h1>
        </div>
    """, unsafe_allow_html=True)


    st.markdown("""
    ### Descripción del ejercicio

    En este ejercicio se utilizará la clase **Paciente**, almacenada
    en la librería externa `libreria_clases_proyecto1.py`.

    La aplicación implementa las operaciones básicas de un CRUD:

    - **Crear** registros.
    - **Leer** y visualizar registros.
    - **Actualizar** información.
    - **Eliminar** registros.

    La clase permite calcular el IMC, su clasificación y la superficie
    corporal.
    """)


    if "pacientes" not in st.session_state:

        st.session_state.pacientes = []


    st.markdown("---")

    st.subheader("Seleccionar clase")


    clase = st.selectbox(
        "Seleccione la clase que desea utilizar",
        ["Paciente"]
    )


    if clase == "Paciente":

        # ======================================
        # CREAR
        # ======================================

        st.subheader("Crear registro")


        nombre_p = st.text_input(
            "Ingrese el nombre del paciente"
        )


        peso_p = st.number_input(
            "Ingrese el peso en kg",
            min_value=0.1,
            value=60.0,
            step=0.1
        )


        altura_p = st.number_input(
            "Ingrese la altura en metros",
            min_value=0.1,
            value=1.60,
            step=0.01
        )


        if st.button("Crear paciente"):

            if nombre_p == "":

                st.write(
                    "Debe ingresar el nombre del paciente."
                )

            else:

                try:

                    paciente = lc.Paciente(
                        nombre_p,
                        peso_p,
                        altura_p
                    )


                    st.session_state.pacientes.append(
                        paciente
                    )


                    st.write(
                        "Paciente registrado correctamente."
                    )


                except ValueError as e:

                    st.write(str(e))


        # ======================================
        # LEER
        # ======================================

        st.markdown("---")

        st.subheader("Registros de pacientes")


        if len(st.session_state.pacientes) > 0:

            registros = []


            for paciente in st.session_state.pacientes:

                registros.append(
                    paciente.resumen()
                )


            st.dataframe(
                registros,
                use_container_width=True,
                hide_index=True
            )


        else:

            st.write(
                "No hay pacientes registrados."
            )


        # ======================================
        # ACTUALIZAR
        # ======================================

        if len(st.session_state.pacientes) > 0:

            st.markdown("---")

            st.subheader("Actualizar paciente")


            nombres = [
                paciente.nombre
                for paciente in st.session_state.pacientes
            ]


            paciente_actualizar = st.selectbox(
                "Seleccione el paciente que desea actualizar",
                nombres,
                key="paciente_actualizar"
            )


            nuevo_peso = st.number_input(
                "Nuevo peso en kg",
                min_value=0.1,
                value=60.0,
                step=0.1,
                key="nuevo_peso"
            )


            nueva_altura = st.number_input(
                "Nueva altura en metros",
                min_value=0.1,
                value=1.60,
                step=0.01,
                key="nueva_altura"
            )


            if st.button(
                "Actualizar paciente"
            ):

                indice = nombres.index(
                    paciente_actualizar
                )


                paciente = (
                    st.session_state.pacientes[indice]
                )


                paciente.peso_kg = nuevo_peso
                paciente.altura_m = nueva_altura


                st.rerun()


            # ======================================
            # ELIMINAR
            # ======================================

            st.markdown("---")

            st.subheader("Eliminar paciente")


            paciente_eliminar = st.selectbox(
                "Seleccione el paciente que desea eliminar",
                nombres,
                key="paciente_eliminar"
            )


            if st.button(
                "Eliminar paciente"
            ):

                indice = nombres.index(
                    paciente_eliminar
                )


                st.session_state.pacientes.pop(
                    indice
                )


                st.rerun()












