import streamlit as st
from src.model_languages import user_prompt
from src.flashcards_components.get_data import get_cards

def flashcards_component():
    st.title('Estude por flashcards')
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Revisão", "Adicionar/Remover", "Perguntas e respostas", "Procurar", "Ver todos"])

    with tab1:
        st.write('algo')
        st.dataframe(get_cards())

    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            btn_user_answer = st.button('Colocar próprio') 

        with col2:
            btn_generate_ia = st.button('Gerar com IA')

        user_flashcard = st.text_input('Entre com o flashcard')
        btn_send = st.button('Enviar')
        if btn_send:
            guide = 'Você é um assistente especializado na criação de flashcards para ajudar no estudo. Quando o usuário enviar uma pergunta ou uma frase para lembrar, sua escrever apenas a resposta para o flashcard, deixe a resposta mais detalhada possível. Aqui está o prompt do usuário:'
            response = user_prompt(guide, user_flashcard)
            st.write(response)

