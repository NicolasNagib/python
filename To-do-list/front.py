import streamlit as st
import time
import requests

# Configs:

st.set_page_config(layout="wide")

st.markdown("""
            <style>
           button{
               min-height: 0 !important;
           }
            
            span.itemP{
                margin: 0px;
                margin-left: 10px !important;
                width:auto;
            }
           
            </style>
            """, unsafe_allow_html=True)
# Configs end

# Functions
@st.dialog("Aguardando resposta...")
def modal_response208(title):
    st.write(f"A tarefa '{title}' já foi informada, deseja registrá-la novamente?")
    yes = st.button("Sim") 
    no = st.button("Não")
    if yes:
        processRequest(title, True, url='http://127.0.0.1:5000/addRepeatItem')
        st.session_state.show_toast = "Tarefa adicionada com sucesso!"
        st.rerun()
    elif no:
        processRequest(title, False, url='http://127.0.0.1:5000/addRepeatItem')

@st.dialog("Aguardando resposta...")
def deleteTask(id, title):
    st.write(f"Realmente deseja excluir a '{title}'")
    yes = st.button("Sim") 
    no = st.button("Não")
    if yes:
        response = requests.put(url=f"http://127.0.0.1:5000/deleteTask/{id}")
        if response.status_code == 200:
            st.session_state.show_toast = f"Tarefa '{title}', excluída com sucesso!"
            st.rerun()
    elif no:
        st.session_state.show_toast = f"Tarefa '{title}', excluída com sucesso!"
        st.rerun()
        

def processRequest(title="", addItem = False, url=str, completed=0, id=0):
    jsonForms = {"title": title, "addItem": addItem,"complete":completed, "id":id}
    if id !=0:
        response = requests.patch(url, json=jsonForms)
    else:
        response = requests.post(url, json=jsonForms)
    print(response)
    if response.status_code == 200 and id == 0:
        st.toast("Tarefa adicionada com sucesso!")
    elif response.status_code == 208:
        modal_response208(title)
    elif response.status_code == 409:
       st.session_state.show_toast = "Tarefa não adicionada!"
       st.rerun()
       
                    
def changeState(id, complete):
    processRequest(url=f"http://127.0.0.1:5000/completeTask/{id}", id=id, completed=complete)
    if response.status_code == 200:
        st.toast(f"Tarefa '{title}', atualizada com sucesso!")

def deleteTask(id, title):
    response = requests.put(url=f"http://127.0.0.1:5000/deleteTask/{id}")
    if response.status_code == 200:
        st.toast(f"Tarefa '{title}', excluída com sucesso!")
        
        
# Functions end

# Session start

if "show_toast" not in st.session_state:
    st.session_state.show_toast = None

if st.session_state.show_toast:
    st.toast(st.session_state.show_toast)
    st.session_state.show_toast = None
# Session start end

space, col1, space = st.columns([1,3,1])

with col1:
    with st.form("To do List"):
        st.header("To do List")
        title = st.text_input(" ",placeholder="Insira o titulo da sua tarefa")
        submit_button = st.form_submit_button("Enviar", width="stretch")
        if submit_button:
            processRequest(title, url='http://127.0.0.1:5000/')
        
    with st.container(border=True, autoscroll=True, height=300):
        st.header("Tarefas:")
        response = requests.get("http://127.0.0.1:5000/loadItems")
        if response.status_code == 404:
            st.write("Sem tarefas a fazer")
        elif response.status_code == 200:
            items = response.json()['items']
            for item in items:
                title = item[0]
                id = item[1]
                complete = item[2]
                with st.container(border=True, horizontal=True):
                    if complete == 1:                
                        st.html(f"<strong style='color:#4cc94c'>{id}</strong> <span class='itemP' style='color: #4cc94c'> {title}</span>")
                    else:
                        st.html(f"<strong>{id}</strong> <span class='itemP'> {title}</span>")
                       
                    delete  = st.button(label="",icon=":material/delete:", type="tertiary", key=f"exclude{id}", on_click = deleteTask, args=(id, title))
                    complete = st.button(label="",icon=":material/check:", type="tertiary", key=f"complete{id}", on_click= changeState, args=(id, complete))