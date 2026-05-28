"""App.py es el nombre tipico de aplicaciones que usan Streamlit"""
import streamlit as st
import pandas as pd

#st.title("Hola slenderman")
#st.write("Pollete")
#st.markdown("## Esto es un subtitulo")
#st.markdown("### Esto es un subtitulo mas pequeño")
#st.markdown("**Negrita** y *cursiva*")

categorias = ["Alimentos", "Transporte", "Entretenimiento", "Salud", "Otros"]

def inicializar_estado():
    """Inicializa la lista de transacciones en `st.session_state` si no existe."""
    if "transacciones" not in st.session_state:
        st.session_state.transacciones = []


def mostrar_formulario():
    """Muestra el formulario de entrada y registra la transacción en el estado."""
    nombre_usuario = st.text_input("Ingresa tu nombre")
    if nombre_usuario:
        st.write(f"{nombre_usuario} bujarrilla")

    with st.form("formulario_transaccion"):
        descripcion = st.text_input("Describe tu gasto o ingreso", placeholder="Ejemplo: Compra de supermercado")
        dineros = st.number_input("Escribe la cantidad", min_value=0.0, step=1.0)
        fecha = st.date_input("Fecha del gasto o ingreso")
        categoria = st.selectbox("Selecciona la categoria", categorias)
        tipo = st.radio("Tipo", ["Gasto", "Ingreso"], horizontal=True)
        btn_submit = st.form_submit_button("Enviar")

    if btn_submit:
        transaccion = {
            "descripcion": descripcion,
            "dineros": dineros,
            "fecha": fecha,
            "categoria": categoria,
            "tipo": tipo,
            "nombre_usuario": nombre_usuario
        }
        st.session_state.transacciones.append(transaccion)
        st.success("Transacción registrada exitosamente")


def mostrar_transacciones():
    """Muestra todas las transacciones registradas o un mensaje informativo si no hay ninguna."""
    st.subheader("Transacciones hechas")
    if st.session_state.transacciones:
        df = pd.DataFrame(st.session_state.transacciones)
        st.dataframe(df)  # <- Mejor forma para mostrar tablas
        # st.table(df)
        # st.data_editor(df)
    else:
        st.info("No has registrado ninguna transacción aún")



def inicializar_app():
    st.title("Tracker de Finanzas Personales")
    st.write("Lleva el control de tus gastos e ingresos de manera simple y visual")
    st.caption("Version 1.0")

    # Llamadas principales
    inicializar_estado()
    mostrar_formulario()
    mostrar_transacciones()

if __name__ == "__main__":
    inicializar_app()
    



# for transaccion in st.session_state.transacciones:
#     st.write(f"{transaccion['tipo']} de {transaccion['dineros']:.2f}€ el {transaccion['fecha']} en {transaccion['categoria']} - {transaccion['descripcion']} ({transaccion['nombre_usuario']})")

# if "contador" not in st.session_state:
#     st.session_state.contador = 0
# 
# if st.button("Contar"):
#     st.session_state.contador += 1
#     st.write(f"Contador: {st.session_state.contador}")