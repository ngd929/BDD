import os
import streamlit as st

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="BDD Generate Keys", page_icon=":python:")  #:taxi:

# Add a selectbox to the sidebar:
with st.sidebar:
    if 'button' not in st.session_state:
        st.session_state.button = False

    def click_button():
        st.session_state.button = not st.session_state.button

    with st.container(border=True):
        left_column, right_column = st.columns(2)
        right_column.toggle('', on_change=click_button)
        if st.session_state.button:
            # The message and nested widget will remain on the page
            left_column.write('Android')
            # st.slider('Select a value')
        else:
            left_column.write('iOS')

    with st.container(border=True):
        st.text_input("English file", key="enFile")
        st.text_input("Spanish file", key="esFile")
        st.text_input("object file", key="objFile")


with st.container(border=True):
    left_column, right_column = st.columns(2)
    # You can use a column just like st.sidebar:
    left_column.text_area("en", key="enInput")
    # left_column.text_input("es", key="esInput")
    with left_column:
        chosen = st.radio(
            'objectType:',
            ("txt", "msg", "btn", "qrb", "img", "lnk"),
            horizontal=True)
        st.write("")    #(f"You are in {chosen} house!")
    enStr = ''
    enInput = st.session_state.enInput
    if "\n" in enInput:
        enStr = enInput.split("\n")[0]
    else:
        enStr = enInput
    left_column.text_area("tempKey", value=chosen + enStr, key="genKey")
    
    with right_column:
        right_column.text_area("es", key="esInput")

with st.container(border=True):
    enResult = "'{}': \"{}\",".format(st.session_state.genKey, enStr)
    esResult = "'{} spanishKey': \"{}\",".format(st.session_state.genKey, st.session_state.esInput)
    objResult = "'{}': \"{}\",".format(st.session_state.genKey, enStr)
    # result = st.session_state.genKey + ": " + st.session_state.enStr
    # st.text_area("", value=result)
    st.code(enResult, language="javascript")
    st.code(esResult, language="javascript")
    st.code(objResult, language="javascript")

    st.button('Update BDD files!', type="primary")


# with st.form("my_form"):

#     # Every form must have a submit button.
#     submitted = st.form_submit_button("Submit")
#     if submitted:
#         st.write("chosen:", chosen, "enStr:", st.session_state.enStr)