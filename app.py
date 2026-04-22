import streamlit as st
import itertools

st.title("🧮 Calculadora de Tabla de Verdad")

# 🔹 Inicializar expresión
if "expr" not in st.session_state:
    st.session_state.expr = ""

# 🔹 Mostrar expresión
st.text_input("Expresión:", value=st.session_state.expr, key="input_expr")

# 🔹 Función para agregar texto
def agregar(valor):
    st.session_state.expr += valor

# 🔹 Botones tipo calculadora
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button("p", on_click=agregar, args=("p ",))
    st.button("q", on_click=agregar, args=("q ",))
    st.button("r", on_click=agregar, args=("r ",))

with col2:
    st.button("AND", on_click=agregar, args=("and ",))
    st.button("OR", on_click=agregar, args=("or ",))
    st.button("NOT", on_click=agregar, args=("not ",))

with col3:
    st.button("(", on_click=agregar, args=("(",))
    st.button(")", on_click=agregar, args=(")",))
    st.button("CLEAR", on_click=lambda: st.session_state.update(expr=""))

# 🔹 Botón calcular
if st.button("Calcular"):
    expr = st.session_state.expr

    variables = sorted(set([c for c in expr if c in "pqrst"]))

    if not variables:
        st.error("❌ Expresión inválida")
    else:
        filas = list(itertools.product([True, False], repeat=len(variables)))
        tabla = []

        for fila in filas:
            valores = dict(zip(variables, fila))
            try:
                resultado = eval(expr, {}, valores)
                fila_resultado = ["V" if v else "F" for v in fila]
                fila_resultado.append("V" if resultado else "F")
                tabla.append(fila_resultado)
            except:
                st.error("❌ Error en la expresión")
                break

        st.subheader("📊 Tabla de verdad")
        st.write("Columnas:", variables + ["Resultado"])
        st.table(tabla)