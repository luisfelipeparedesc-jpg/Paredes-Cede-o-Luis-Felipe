import streamlit as st
import itertools

# 🎨 Estilos
st.markdown("""
<style>
body {
    background-color: #f4f4f4;
}
.titulo {
    text-align: center;
    color: #333;
}
.caja {
    display: flex;
    justify-content: center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='titulo'>🧮 Calculadora de Tabla de Verdad</h1>", unsafe_allow_html=True)

# 📥 Entrada
expr = st.text_input("Escribe la expresión lógica:", placeholder="Ej: p and q or not p")

st.info("Usa: and (∧), or (∨), not (¬)")

# 🔘 Botón
if st.button("Calcular"):
    
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

        # 📊 Mostrar tabla
        st.subheader("Tabla de verdad")
        st.table(tabla)

        # Encabezados
        st.write("Columnas:", variables + ["Resultado"])