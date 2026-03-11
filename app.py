import streamlit as st
import pandas as pd

# Configuración de la página con marca Comfenalco
st.set_page_config(page_title="DTIA - Comfenalco Antioquia", page_icon="📈")

st.title("🚀 Diagnóstico Empresarial Automatizado")
st.subheader("Departamento de Tecnología, Innovación y Analítica")

# Formulario de entrada
with st.form("diagnostico_form"):
    nombre_empresa = st.text_input("Nombre de la Empresa")
    rotacion = st.slider("Porcentaje de Rotación Anual (%)", 0, 100, 15)
    tiene_sst = st.checkbox("¿Cuenta con Sistema SST al día?")
    brechas = st.multiselect("Brechas detectadas:", 
                            ["Liderazgo", "Habilidades Técnicas", "Cultura Organizacional", "Transformación Digital"])
    
    boton_enviar = st.form_submit_button("Generar Informe e Impacto")

# Lógica y Resultados
if boton_enviar:
    st.divider()
    st.write(f"### Informe para: {nombre_empresa}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if rotacion > 15:
            st.error(f"⚠️ Rotación Crítica: {rotacion}%")
            st.info("Acción: Priorizar Plan de Intermediación con IA.")
        else:
            st.success(f"✅ Rotación Estable: {rotacion}%")
            
    with col2:
        if not tiene_sst:
            st.warning("⚠️ Riesgo Legal detectado en SST.")
            st.info("Acción: Agendar Consultoría Especializada.")
        else:
            st.success("✅ Estándares SST cumplidos.")

    # Simulación de Auditoría
    st.toast("Datos registrados en el banco de I+D para auditoría interna.")
