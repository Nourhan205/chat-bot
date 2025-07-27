import streamlit as st

# st.title("Chatbot")
# st.header("this is a chatbot")
# st.subheader("sub header")
# st.text("text")
# st.markdown("markdown")


# x=st.text_input("Enter a query")
# if st.button("submit"):
#     st.write("the answer to the question",x,"is cairo")  


# st.feedback("thumbs")


# st.sidebar.title("sidebar")
# col1,col2 =st.sidebar.columns(2)

# with col1:
#     st.button("click me on the left")


# with col2:
#     st.button("click me on the right")


st.title(" chatbot")
if "chat_history" not in st.session_state:
    st.session_state.chat_history =[]

user_input=st.text_input("you:")

if user_input:
    bot_response=f"u said :{user_input}"
    st.session_state.chat_history.append(("you",user_input))
    st.session_state.chat_history.append(("bot",bot_response))

for speaker,message in st.session_state.chat_history:
    if speaker =="you":
        st.markdown(f"👱🏿:{message}")
    
    
    if speaker =="bot":
        st.markdown(f"🤖:{message}")