import streamlit as st
from db_utils import get_connection
st.set_page_config(page_title="Delete item", layout="wide",initial_sidebar_state="collapsed")
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

with st.form(key='deleting_item'):
    box_to_delete_from=st.number_input('Enter the box number',min_value=1)
    item_to_delete=st.text_input('Enter item name to delete')
    button_status=st.form_submit_button('Delete item')

if(button_status):
    cursor.execute('select * from boxes where box_number= %s and item_name= %s',(box_to_delete_from,item_to_delete))
    result=cursor.fetchone()
    if (result):
        st.write(f'Item: {item_to_delete} deleted from box number: {box_to_delete_from}')
        cursor.execute('delete from boxes where box_number = (%s) and item_name=(%s)',(box_to_delete_from,item_to_delete))
        conn.commit()
    else:
        st.write('Item or box number invalid')


if st.button('Back to home 🏠'):
    st.switch_page('Home.py')