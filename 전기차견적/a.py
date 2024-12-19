import streamlit as st

st.session_state['id_dados_gerais'] = (st.session_state['df_dados_gerais_unidades'].loc[st.session_state['df_dados_gerais_unidades']['Unidade'] == st.session_state['cliente']])
        
st.data_editor(st.session_state['id_dados_gerais'], hide_index=True, column_order=('Distribuidora', 'Classe de Tensão', 'Modalidade Tarifária', 'Demanda Contratada Ponta', 'Demanda Contratada Fora Ponta', 'Desconto', 'CDE Covid', 'CDE Escassez Hídrica', 'Comunhão'), disabled=('Distribuidora', 'Classe de Tensão'))