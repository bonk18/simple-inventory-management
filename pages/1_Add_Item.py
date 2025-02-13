import streamlit as st
from db_utils import get_connection
st.set_page_config(page_title="Add item", layout="wide",initial_sidebar_state="collapsed")
st.title("Add details of the item to be added")
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


conn=get_connection()
cursor=conn.cursor()


st.sidebar.title("📌 Navigation")

if st.sidebar.button("🏠 Home", key="home"):
    st.switch_page("Home.py")

if st.sidebar.button("📦 Add Item", key="add_item"):
    st.switch_page('Pages/1_Add_Item.py')

if st.sidebar.button("🔍 Find Item", key="find_item"):
    st.switch_page('Pages/2_Find_Item.py')

if st.sidebar.button("📋 View Items", key="view_items"):
    st.switch_page('Pages/3_View_items.py')
    
if st.sidebar.button("🗑️ Delete Item",key='delete_item'):
    st.switch_page('Pages/4_Delete_item.py')


with st.form(key='adding_item'):
    box_number=st.number_input('Enter the box number for the item',min_value=1,step=1)
    item_name=st.text_input('Enter the name of the item')
    button_status=st.form_submit_button('Add item')
if(button_status):
    cursor.execute('INSERT INTO boxes (box_number,item_name) values (%s, %s)',(box_number,item_name))
    conn.commit()
    st.write(f'Item: {item_name} added to box number: {box_number}')
    st.balloons()




if st.button('Back to home 🏠'):
    st.switch_page('Home.py')