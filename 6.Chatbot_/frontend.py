import streamlit as st
from backend import workflow
from langchain_core.messages import HumanMessage

CONFIG = {'configurable': {'thread_id': '1'}}

# PAGE CONFIG-
st.set_page_config(
    page_title='Chatbot',
    page_icon="🤖",
    layout="centered"
)

st.title('🤖 Chatbot')


#CHAT HISTORY-
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []


#we load the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.write(message['content'])



user_input = st.chat_input(placeholder="Ask me anything...")

if user_input:

    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)

    response = workflow.invoke({'messages': HumanMessage(content= user_input)}, config= CONFIG)
    ai_message = response['messages'][-1].content

    st.session_state['message_history'].append({'role':'assistant', 'content': ai_message})
    with st.chat_message('assistant'):
        st.text(ai_message)


