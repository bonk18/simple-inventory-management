import streamlit as st
st.set_page_config(page_title='Welcome to the box inventory management app',layout='wide',initial_sidebar_state="collapsed")
st.title('Welcome to the box inventory management app')
st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {display: none;}
        .custom-button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 8px;
        }
        .custom-button:hover {
            background-color: #45a049;
        }
    </style>
    """, unsafe_allow_html=True)





st.sidebar.title("📌 Navigation")

if st.sidebar.button("🏠 Home", key="home"):
    st.switch_page("Home")

if st.sidebar.button("📦 Add Item", key="add_item"):
    st.switch_page('Add_Item')

if st.sidebar.button("🔍 Find Item", key="find_item"):
    st.switch_page('Find_Item')

if st.sidebar.button("📋 View Items", key="view_items"):
    st.switch_page('View_items')

if st.sidebar.button("🗑️ Delete Item",key='delete_item'):
    st.switch_page('Delete_item')





col1,col2,col3,col4=st.columns(4)
with col1:
    if st.button('📦 Add item'):
        st.st.switch_page('Add_Item')
with col2:
    if st.button('🔍 Find item'):
        st.switch_page('Find_Item')
with col3:
    if st.button('📋 View items'):
        st.switch_page('View_items')
with col4:
    if st.button('🗑️ Delete Item'):
        st.switch_page('Delete_item')