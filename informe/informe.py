import streamlit as st
import matplotlib.pyplot as plt


def mostrar_informe():

    # Informe: Evaluación y Recomendación para la Tienda de Sr. Juan
    # Titulo Principal
    st.title("Informe Final: Evaluación y Recomendación para la Tienda de Sr. Juan")
    st.markdown("**Alura Store**")

    # Sección de Introducción
    st.header("Introducción")
    st.write("""
    El objetivo de este análisis es proporcionar al Sr. Juan una recomendación fundamentada sobre qué tienda debería vender,
    considerando diversos factores clave como los ingresos totales, las categorías de productos más y menos vendidos, las calificaciones
    promedio de los clientes, los productos más y menos vendidos, y el costo de envío. Tras realizar un análisis exhaustivo, se recomienda
    considerar especialmente la tienda con el menor desempeño general para la toma de decisiones. A continuación, se presentan los
    hallazgos clave derivados de este análisis y una justificación clara para la elección final.
    """)

    # Sección de Insights Obtenidos y Gráficos
    st.header("Insights Obtenidos y Gráficos")

    # 1. Ingresos Totales de las Tiendas
    st.subheader("1. Ingresos Totales de las Tiendas")
    st.write("""
    El análisis de los ingresos totales proporciona una visión clara de la rentabilidad de cada tienda. Estos son los hallazgos más relevantes:

    - **Tienda 1** tiene el mayor ingreso total, lo que refleja una buena capacidad de generación de ventas.
    - **Tienda 2** sigue de cerca con ingresos relativamente altos.
    - **Tienda 3** tiene ingresos competitivos, aunque son más bajos en comparación con Tienda 1 y Tienda 2.
    - **Tienda 4**, por el contrario, presenta los ingresos más bajos, lo que refleja un desempeño económico inferior frente a las demás tiendas.
    """)
    # Gráfico de Ingresos (Gráfico de Tienda que más factura)
    # Aquí usas la función de Streamlit para mostrar gráficos. Ejemplo de gráfico:
    # plt.plot([1000, 2000, 3000, 4000])  # Aquí colocas tus datos
    # st.pyplot(plt)

    # 2. Categorías de Productos Más y Menos Vendidos
    st.subheader("2. Categorías de Productos Más y Menos Vendidos")
    st.write("""
    El análisis de las categorías de productos más y menos vendidos da una idea del desempeño en cada tienda:

    - **Tienda 1** tiene el mayor número de productos más vendidos, lo que sugiere que ciertas categorías tienen una fuerte demanda.
    - **Tienda 2** tiene una buena relación entre productos más vendidos y menos vendidos, lo que indica que no tiene grandes dificultades en gestionar su inventario.
    - **Tienda 3** muestra un alto número de productos menos vendidos, lo que sugiere dificultades en ciertas categorías de productos. A pesar de esto, su calificación alta podría compensar en parte esta debilidad.
    - **Tienda 4** tiene un número competitivo de productos vendidos, pero su bajo rendimiento en ingresos totaliza una debilidad.
    """)
    # Gráfico de productos más vendidos
    # plt.bar([1, 2, 3, 4], [10, 20, 5, 3])  # Aquí debes colocar los datos reales
    # st.pyplot(plt)

    # 3. Calificaciones Promedio de los Clientes
    st.subheader("3. Calificaciones Promedio de los Clientes")
    st.write("""
    La satisfacción del cliente es crucial para la fidelidad y la retención. En este sentido:

    - **Tienda 1** tiene la calificación más baja (3.98), lo que refleja una menor satisfacción de los clientes en comparación con las otras tiendas.
    - **Tienda 2** con una calificación de 4.04 presenta una excelente puntuación, lo que indica una experiencia positiva para los clientes.
    - **Tienda 3** con una calificación de 4.05 también muestra un desempeño destacado en términos de satisfacción del cliente.
    - **Tienda 4** con una calificación de 4.00 refleja un nivel de satisfacción algo por debajo de Tienda 2 y Tienda 3.
    """)
    # Gráfico de calificación promedio por tienda
    # plt.bar([1, 2, 3, 4], [3.98, 4.04, 4.05, 4.00])  # Los datos reales deben ir aquí
    # st.pyplot(plt)

    # 4. Productos Más y Menos Vendidos
    st.subheader("4. Productos Más y Menos Vendidos")
    st.write("""
    El análisis de los productos más y menos vendidos revela lo siguiente:

    - **Tienda 1** tiene un alto número de productos más vendidos, pero también tiene una cantidad considerable de productos menos vendidos.
    - **Tienda 2** mantiene un balance adecuado entre productos más vendidos y menos vendidos.
    - **Tienda 3** sigue destacándose por su buena calificación, a pesar de tener muchos productos menos vendidos.
    - **Tienda 4** tiene un número competitivo de productos vendidos, pero su bajo desempeño en ingresos refleja sus debilidades en este aspecto.
    """)
    # Gráfico de productos más y menos vendidos
    # plt.bar([1, 2, 3, 4], [50, 80, 30, 20])  # Inserta los datos correspondientes
    # st.pyplot(plt)

    # 5. Costo de Envío Promedio
    st.subheader("5. Costo de Envío Promedio")
    st.write("""
    El costo de envío es otro factor clave que afecta las decisiones de compra de los clientes:

    - **Tienda 4** tiene el costo de envío más bajo, lo que la hace más competitiva en términos de costos adicionales para los clientes.
    - **Tienda 3** tiene un costo de envío razonable, lo que también la coloca en una posición competitiva.
    - **Tienda 1** tiene el costo de envío más alto, lo que podría estar afectando su eficiencia y la satisfacción del cliente.
    - **Tienda 2** tiene un costo de envío promedio, pero no tan eficiente como el de Tienda 4.
    """)
    # Gráfico del costo promedio de envío por tienda
    # plt.bar([1, 2, 3, 4], [5.50, 4.00, 6.00, 3.50])  # Los datos reales van aquí
    # st.pyplot(plt)

    # Conclusión y Recomendación Final
    st.header("Conclusión y Recomendación Final")
    st.write("""
    Tras analizar todos los criterios clave — ingresos totales, productos más y menos vendidos, calificación promedio de los clientes,
    y costo de envío promedio — la tienda con el peor desempeño general en estos aspectos es **Tienda 4**.

    Las razones que sustentan esta recomendación son las siguientes:

    1. **Bajos Ingresos**: Tienda 4 tiene los ingresos más bajos entre todas las tiendas.
    2. **Desempeño en Productos**: Aunque tiene un número competitivo de productos vendidos, su bajo rendimiento en productos más vendidos y productos menos vendidos sugiere ineficiencia.
    3. **Calificación Promedio Baja**: Tienda 4 tiene una calificación promedio de 4.00.
    4. **Costo de Envío Alto**: Aunque su costo de envío es bajo, no es suficiente para contrarrestar sus debilidades en ingresos y satisfacción del cliente.

    ### **Recomendación Final:**
    #### **¡Tienda 4 es la opción menos competitiva y, por lo tanto, es la tienda que se recomienda vender!**
    
    ***Esta recomendación se basa en un análisis exhaustivo de los factores clave, y se considera que Tienda 4 tiene un desempeño insuficiente en comparación con las demás opciones.***
    """)