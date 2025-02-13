import streamlit as st
from db_utils import get_connection
st.set_page_config(page_title="Find item", layout="wide",initial_sidebar_state="collapsed")
st.title("Enter the name of the item to be search")
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




with st.form(key='finding_item'):
    item_to_find=st.text_input('Enter the name of the item to search')
    button_status=st.form_submit_button('Find item')

if (button_status):
    cursor.execute('select box_number from boxes where item_name = %s',(item_to_find,))
    data=cursor.fetchone()
    if(data):
        st.write(f'Item: "{item_to_find}" found in box number: "{data[0]}"')
    else:
        st.write('No entries found')





if st.button('Back to home 🏠'):
    st.switch_page('Home.py')
